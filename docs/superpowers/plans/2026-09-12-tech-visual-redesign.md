# Tech Visual Redesign Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 将网站首页标题改为“使用教程”，删除旧介绍文案，并把整站升级为深色 AI 科技馆视觉，同时保留全部教程、图片、视频和交互。

**Architecture:** 保持现有单页静态站结构与原生 `details`/JavaScript 交互，仅修改 HTML 文案和 CSS 视觉层。测试继续使用 Python `unittest` 检查核心内容与媒体资源，并新增对新标题和已删除文案的回归断言。

**Tech Stack:** HTML5、CSS3、原生 JavaScript、Python `unittest`、GitHub Pages

## Global Constraints

- 页面主标题必须为“使用教程”，浏览器标题必须为“使用教程｜沈万三”。
- 页面中不得再出现“把账号使用、验证码、售后与故障处理集中到一个页面。遇到问题时，先按分类找到对应答案。”。
- 保留现有 6 张教程图片、4 个本地 MP4 视频、FAQ 内容、快捷入口和展开/收起功能。
- 不引入外部图片、字体、CSS 框架或 JavaScript 依赖。
- 视觉使用深海军蓝/黑底、青色和电紫色光效、网格、玻璃卡片；正文必须保持清晰可读。
- 保留 760px 移动端断点、键盘焦点状态和 `prefers-reduced-motion` 支持。

---

## File Structure

- `index.html`：页面语义结构、标题和教程内容；只改浏览器标题、主题色、主标题并删除旧介绍段落。
- `styles.css`：整站视觉系统；重建颜色变量、背景、网格、光效、玻璃卡片和响应式样式。
- `tests/test_site.py`：静态站回归测试；新增标题与旧文案删除断言，继续验证所有媒体。

### Task 1: 锁定新标题与文案要求

**Files:**
- Modify: `tests/test_site.py`
- Test: `tests/test_site.py`

**Interfaces:**
- Consumes: UTF-8 编码的 `index.html`。
- Produces: `test_hero_uses_tutorial_title_without_old_intro()` 回归测试。

- [ ] **Step 1: 写入失败测试**

```python
    def test_hero_uses_tutorial_title_without_old_intro(self):
        html = (ROOT / "index.html").read_text(encoding="utf-8")
        self.assertIn("<title>使用教程｜沈万三</title>", html)
        self.assertIn("<h1>使用教程</h1>", html)
        self.assertNotIn(
            "把账号使用、验证码、售后与故障处理集中到一个页面。"
            "遇到问题时，先按分类找到对应答案。",
            html,
        )
```

- [ ] **Step 2: 运行测试并确认失败**

Run: `C:\Users\lijia40\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe -m unittest tests/test_site.py -v`

Expected: 新测试因旧标题仍存在而失败，其他媒体和结构测试通过。

- [ ] **Step 3: 提交测试基线**

```powershell
git add tests/test_site.py
git commit -m "test: define tutorial hero copy"
```

### Task 2: 更新页面标题和主题元数据

**Files:**
- Modify: `index.html`
- Test: `tests/test_site.py`

**Interfaces:**
- Consumes: Task 1 的标题与文案断言。
- Produces: 新浏览器标题、新 H1、深色主题色，且不存在旧 `hero-copy` 段落。

- [ ] **Step 1: 修改页面头部与 Hero**

将对应 HTML 改为：

```html
<meta name="theme-color" content="#050816">
<title>使用教程｜沈万三</title>
```

Hero 内容改为：

```html
<p class="eyebrow">快速上手 · 问题自查 · 视频教程</p>
<h1>使用教程</h1>
<div class="hero-actions" aria-label="内容快速入口">
```

删除整个 `<p class="hero-copy">...</p>` 元素，其余内容不变。

- [ ] **Step 2: 运行测试并确认通过**

Run: `C:\Users\lijia40\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe -m unittest tests/test_site.py -v`

Expected: 所有测试显示 `OK`。

- [ ] **Step 3: 提交文案变更**

```powershell
git add index.html
git commit -m "feat: rename page to tutorial guide"
```

### Task 3: 建立深色 AI 科技视觉系统

**Files:**
- Modify: `styles.css`
- Test: `tests/test_site.py`

**Interfaces:**
- Consumes: 现有 HTML 类名与结构，不新增运行时依赖。
- Produces: CSS 变量 `--bg`、`--surface`、`--cyan`、`--purple`、`--text`、`--muted`，以及覆盖现有组件类名的完整视觉样式。

- [ ] **Step 1: 替换基础设计令牌与页面背景**

使用下列核心令牌，并用径向渐变叠加线性网格构成背景：

```css
:root {
  --bg: #030711;
  --bg-deep: #01040a;
  --surface: rgba(8, 20, 36, 0.82);
  --surface-strong: rgba(10, 27, 47, 0.96);
  --cyan: #35d9ff;
  --cyan-soft: rgba(53, 217, 255, 0.14);
  --purple: #9b7cff;
  --purple-soft: rgba(155, 124, 255, 0.14);
  --text: #eaf8ff;
  --muted: #9cb3c4;
  --line: rgba(94, 211, 255, 0.18);
  --warning: #ffc857;
}
```

`body` 使用深色背景、青紫光晕和无外链字体栈；`body::before` 使用 40px 网格并降低透明度，`body::after` 添加固定扫描光带且不拦截点击。

- [ ] **Step 2: 重做 Hero 与导航组件**

Hero 使用深色渐变、青紫径向光晕和细网格；`.brand-mark`、`.source-link`、`.button` 使用发光边框与清晰悬停/焦点状态；H1 使用浅色文字与轻微青色投影，保留响应式字号。

- [ ] **Step 3: 重做内容卡片与媒体组件**

`.notice-strip`、`.section-tools`、`.faq-card`、`.video-card`、`.prerequisite-card`、`.help-card` 使用半透明深色表面、1px 冷色边框、`backdrop-filter: blur(16px)` 和阴影；展开卡片显示青色高光线。图片与视频使用深色框体并保持原始比例，提示框用青色，警告框用琥珀色。

- [ ] **Step 4: 完善可访问性和移动端**

为链接、按钮、summary 增加 `:focus-visible` 青色轮廓；在 `@media (max-width: 760px)` 下改为单列布局、缩小间距和标题；在 `@media (prefers-reduced-motion: reduce)` 中禁用动画与平滑滚动。

- [ ] **Step 5: 运行静态检查**

Run: `C:\Users\lijia40\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe -m unittest tests/test_site.py -v`

Expected: 所有测试显示 `OK`。

Run: `node --check script.js`

Expected: 无输出且退出码为 0。

Run: `git diff --check`

Expected: 无输出且退出码为 0。

- [ ] **Step 6: 提交视觉重构**

```powershell
git add styles.css
git commit -m "style: apply dark AI technology theme"
```

### Task 4: 本地验收并部署

**Files:**
- Verify: `index.html`
- Verify: `styles.css`
- Verify: `.github/workflows/pages.yml`

**Interfaces:**
- Consumes: Tasks 1–3 的通过版本。
- Produces: GitHub Pages 上可访问的新科技风页面。

- [ ] **Step 1: 启动本地服务器并检查页面响应**

Run: `C:\Users\lijia40\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe -m http.server 8000`

Expected: `http://127.0.0.1:8000/` 返回 HTTP 200，页面包含“使用教程”。

- [ ] **Step 2: 检查最终差异和仓库状态**

Run: `git status --short`

Expected: 工作区无未提交变更。

- [ ] **Step 3: 推送主分支**

```powershell
git push origin main
```

Expected: GitHub 接受推送并更新 `main`。

- [ ] **Step 4: 验证 Pages 工作流与线上内容**

检查 `pages.yml` 最新运行状态为 `completed/success`，然后打开 `https://jl7007.github.io/shenwansan/`，确认主标题为“使用教程”、旧介绍不存在、4 个视频仍可见且深色科技主题已加载。
