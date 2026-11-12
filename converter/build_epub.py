#!/usr/bin/env python3
"""Convert UTF-8 Markdown to a compact EPUB 3 using Pandoc.

Usage: python converter/build_epub.py input.md output.epub --title "Book title"
Requires Pandoc 3.x on PATH. No Python packages required.
"""
import argparse
import re
import shutil
import subprocess
import tempfile
from pathlib import Path
from zipfile import ZipFile

HERE = Path(__file__).resolve().parent


def parse_pipe_table(lines, start):
    """Adapt simple GFM tables; leave complex tables for Pandoc."""
    if start + 2 >= len(lines):
        return None

    def cells(line):
        return [c.strip() for c in re.split(r'(?<!\\)\|', line.strip().strip('|'))]

    header, alignment = cells(lines[start]), cells(lines[start + 1])
    if len(header) < 3 or len(header) != len(alignment):
        return None
    if not all(re.fullmatch(r':?-{3,}:?', c) for c in alignment):
        return None
    i, rows = start + 2, []
    while i < len(lines) and lines[i].lstrip().startswith('|'):
        row = cells(lines[i])
        if len(row) != len(header):
            return None
        rows.append(row)
        i += 1
    if not rows:
        return None
    output = []
    for row in rows:
        output.append('**' + row[0] + '**')
        output.extend('**' + k + '：**' + v for k, v in zip(header[1:], row[1:]))
        output.append('')
    return i, '\n\n'.join(output).rstrip()


def adapt_markdown(source):
    lines = source.splitlines()
    output, i = [], 0
    in_fence = False
    while i < len(lines):
        text = lines[i]
        if re.match(r'^\s*(`{3,}|~{3,})', text):
            in_fence = not in_fence
        if not in_fence and text.lstrip().startswith('|'):
            table = parse_pipe_table(lines, i)
            if table:
                i, converted = table
                output.extend([converted, ''])
                continue
        output.append(text)
        i += 1
    return '\n'.join(output) + '\n'


def validate_epub(path):
    with ZipFile(path) as archive:
        names = archive.namelist()
        assert names[0] == 'mimetype', 'EPUB mimetype must be first'
        assert archive.read('mimetype') == b'application/epub+zip'
        assert 'META-INF/container.xml' in names
        assert any(name.endswith('.opf') for name in names)
        assert any(name.endswith('.xhtml') for name in names)
        assert archive.testzip() is None, 'Invalid EPUB ZIP contents'


def build(input_path, output_path, title, identifier=None):
    if not shutil.which('pandoc'):
        raise RuntimeError('Pandoc is required: https://pandoc.org/installing.html')
    source = input_path.read_text(encoding='utf-8')
    if not source.strip():
        raise ValueError('Input Markdown file is empty')
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='corner-epub-') as temp:
        temp = Path(temp)
        converted = temp / 'adapted.md'
        converted.write_text(adapt_markdown(source), encoding='utf-8')
        temp_epub = temp / 'book.epub'
        command = [
            'pandoc', str(converted), '--from=gfm', '--to=epub3',
            '--standalone', '--toc', '--toc-depth=3', '--split-level=2',
            '--css', str(HERE / 'reader.css'),
            '--metadata', f'title={title}',
            '--metadata', 'lang=zh-CN',
            '--output', str(temp_epub),
        ]
        if identifier:
            command.extend(['--metadata', f'identifier={identifier}'])
        subprocess.run(command, check=True, capture_output=True, text=True)
        validate_epub(temp_epub)
        shutil.copyfile(temp_epub, output_path)
    return output_path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input', type=Path)
    parser.add_argument('output', type=Path)
    parser.add_argument('--title', required=True)
    parser.add_argument('--identifier')
    args = parser.parse_args()
    result = build(args.input, args.output, args.title, args.identifier)
    print(f'EPUB ready: {result} ({result.stat().st_size} bytes)')


if __name__ == '__main__':
    main()
