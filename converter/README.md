# EPUB 转换器（第一阶段原型）

本目录将 Markdown 转为适合 P6+ 窄屏阅读的 EPUB 3。使用 Pandoc 3.x，不需要额外的 Python 包。

运行：

```bash
python converter/build_epub.py tests/sample.md test-output.epub --title "Fate、Destiny、Kismet：排版工具测试"
```

当前提供：第三轮实测的相对标题字号、紧凑无序列表、简单 GFM 宽表格的纵向化、Pandoc 自动目录、EPUB ZIP 基础校验。

**范围限制**：仅完成 Markdown → EPUB 原型；尚未接入 Notion API、GitHub Actions、版本与 OPDS 发布。表格预处理只覆盖简单的规则管道表格；复杂表格保留给 Pandoc，暂不保证小屏最佳排版。复杂嵌套列表、图片、公式、非文本块需要进一步测试。输入需是受信任的 Markdown。

本地已用 `tests/sample.md` 完成构建与 ZIP 内容检查；P6+ 实际阅读尚未回归测试。排版参照 `books/fate-destiny-kismet-compact-headings.epub`。
