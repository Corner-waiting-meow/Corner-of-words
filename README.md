# 转角遇到字 · Corner of Words

给电纸书准备的阅读内容和 RSS / OPDS 兼容性实验仓库。

目前先验证 **文石 P6+** 的订阅、全文显示与文件下载行为；尚未加入自动推送机制。

## 订阅测试地址

GitHub Pages 成功部署后：

- RSS 全文订阅：`https://corner-waiting-meow.github.io/Corner-of-words/feed.xml`
- OPDS 1.x 目录：`https://corner-waiting-meow.github.io/Corner-of-words/opds.xml`
- EPUB 直接下载：`https://corner-waiting-meow.github.io/Corner-of-words/books/test.epub`
- XHTML 直接下载：`https://corner-waiting-meow.github.io/Corner-of-words/books/test.xhtml`
- 网站首页：`https://corner-waiting-meow.github.io/Corner-of-words/`

这些是预期地址，须在 GitHub Pages 启用并完成部署之后才能访问。

## 当前文件

```text
Corner-of-words/
├── README.md
├── index.html
├── feed.xml
├── opds.xml
└── books/
    ├── test.xhtml
    └── test.epub
```

- `feed.xml`：用于测试中文标题、RSS `content:encoded` 全文与日文字符。
- `opds.xml`：OPDS 1.x 最小目录，带 XHTML 直链。
- `books/test.xhtml`：UTF-8、中文、日文、加粗显示的测试页面。
- `books/test.epub`：相同内容的 EPUB 3 测试电子书，用于对比 OPDS 下载情况。
- `index.html`：入口导航。

**OPDS 现在分别列出 XHTML 与 EPUB 两个测试项目，方便独立比较下载结果。**

## 启用 GitHub Pages

打开仓库的 **Settings → Pages**，在 **Build and deployment** 中选择 `Deploy from a branch`、`main`、`/(root)` 并保存。部署成功后在 P6+ 的网络阅读中添加订阅源。

## 隐私

这里是公开仓库。不要提交个人邮箱、私密笔记或非公开内容。提交记录的作者邮箱应保持为 GitHub 的 `users.noreply.github.com` 隐私邮箱。

## Notion 真实页面转换测试

- [Fate、Destiny、Kismet：三种命运语感与文化意象](https://corner-waiting-meow.github.io/Corner-of-words/books/fate-destiny-kismet.epub)：Notion 手记完整正文转换为 EPUB，保留标题、表格、列表、加粗和斜体。已加入 OPDS，待 P6+ 实机检查排版。
- [Notion 原页面](https://app.notion.com/p/40bab43af7a48146b750c61fdb8e953e)
