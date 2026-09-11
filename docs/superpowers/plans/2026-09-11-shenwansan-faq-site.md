# 沈万三常见问题网站 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 将原 Blogger 常见问题页面完整整理为响应式静态网站，并发布到 `https://jl7007.github.io/shenwansan/`。

**Architecture:** 使用原生 HTML、CSS 和少量 JavaScript 构建单页 FAQ。图片保存在仓库中，视频使用 Blogger 播放器嵌入并提供原页面备用链接；GitHub Actions 负责发布 GitHub Pages。

**Tech Stack:** HTML5、CSS3、原生 JavaScript、Python `unittest`、GitHub Actions、GitHub Pages

## Global Constraints

- 保留原页面全部文字、6 张图片和 4 个视频入口。
- 页面必须在禁用 JavaScript 时仍能阅读全部核心内容。
- 不使用前端框架、第三方 JavaScript 或远程字体。
- 桌面和手机宽度下不得出现水平滚动。
- 公开地址为 `https://jl7007.github.io/shenwansan/` 或 GitHub 返回的等效 Pages 地址。

## Exact Media Map

Download these image URLs without changing their order:

1. `assets/images/tutorial-2fa-1.png` ← `https://blogger.googleusercontent.com/img/a/AVvXsEgZUIj2gjM0bZkEea1gAsWAnU6-HSPUfiRBk611XI2-QePuw2rorbzYpjPr_fQZ5g4hFzieS6l5HUUVNSgJVWjEvwTnOgKMJAxukBS-W5BJTxQuShXUicWCLhWiQmshX_ix1oaM32wJyL4rjwjeZZ6F95YQ1G7x-e8v4AXULKNHCPowCXcFUYCA-YmXsIgb`
2. `assets/images/tutorial-2fa-2.png` ← `https://blogger.googleusercontent.com/img/a/AVvXsEhgsvp1eVtLRIaeV8OhrTZ5Cuhygz79EP5SuiPG7FDe9AcGqNEtwngsM8KhPZpr_SOp48jJ4I9yuTshJ9WA3YMfw67mBKCvxEtEhoGMP5I6tJf7DD3AM5h0IdYwj7uJCoqPwoJ66Jdgl2HO7lE6tionHLyeQk0R6ZCI5byXFhh44aN4-nsxIw4Od8uHYyYh`
3. `assets/images/tutorial-2fa-3.png` ← `https://blogger.googleusercontent.com/img/a/AVvXsEhwkS_eEB1rkMN7UFgKFsnfWvI38angWHvt2UNBH8HK7ChjQl0GEkxbKyDhwV1czYvqIBpZeuDGmTjcLs5c1o6oEBZvyUpi4X4kQQtfcnWKXhUhUWqAl7V_YjImFEqF6sXsIUlr521QaWx6G1f60LkKcQ0KfhVSqM1MN_Q3msCdX4LH7L8hPyh1Iw-AfDhW`
4. `assets/images/network-error-1.png` ← `https://blogger.googleusercontent.com/img/a/AVvXsEhdfYOAM03vryIFTyJy64t4uQF6ulo0ulLfPJ8lMvlJ6zilh6ERsSqn0O0vydJghtg3KZAq3PxO9tdqbNUYYij9QKELj0m9Lbf1n5zGThQmUbZ7OySNDXazudwNsRjGpa-quqToIvfee5saFHTqD_o7W9y63GavPUAsUaq-wIOZGkqNHwAGHd6Nl06mG84D`
5. `assets/images/network-error-2.png` ← `https://blogger.googleusercontent.com/img/a/AVvXsEhR4LLrQbN2JRKPPZ8ajREGsfdhROS6zdYJ2XvJvAqM7zdiX96PDzEn3wztoEwgZOFOe_echOg2VseT4lSWzkTuOkFnEyzin-giudIFzzH4-ZLWlhokV6K_s9YSl9EY2I8WPSjCeF0xzhOLy-jKj7xNEKMGU6HUb_5ZYcwnY0HWlQ07uudLc-oJcWCl9JYS`
6. `assets/images/outlook-login.png` ← `https://blogger.googleusercontent.com/img/a/AVvXsEhXK-Em_iv1-MfH_H5Uj9C06W3ILAUC9jKd1KQSyj33FgT9_vC1QthhXnaRneTCvjsYuKqcvWLXVJcrDhdB8Ta1DPUnMEStnSrZR2aF4gGjHy8mepsH-3CZLqM9xxPanz0VRlV4vV0iaO5VxZ7KQafw5o6IreDGbq5soN89zBrldFd4iRvPhBbJnA6MWMLJ`

Use these four iframe sources:

1. `https://www.blogger.com/video.g?token=AD6v5dwbDZHNSC812gLbKg64aLnD8mv5e_i6VAGIElh9x8OCpWIkTLbxSr0_pi7nXlavLlPlF4XSUbAqJx-t5vil-qiUHQCYbYQKjuRdNwTWNeDeh8t6v7JuPjHqooN56gRuN4XGx4g&origin=shenwansa.blogspot.com`
2. `https://www.blogger.com/video.g?token=AD6v5dypbg6GY0o84G1xa6UPwpk0pq6JPdgfVFiZILoOrbjAp1uTj4GKprL_qkO0tlsVD8juVlgvoHd5BIA01fTYvnMsUA9_OUAW9-tTn3RaQpnzt2oAhOo-1hlxQAtrCbSzxrolGsE&origin=shenwansa.blogspot.com`
3. `https://www.blogger.com/video.g?token=AD6v5dyvS74x-ucUl-Eu3rSCwfxnvNQg1CRzGuR6ZqyMxaRCsJRnf_92UdJvkHGBHaDEsxbqieMhYromC8DYXdkRxUR_ofoF6equyTaE4S2e8cNH2jy77C-ZYka8xau5PC803NaSp9e9&origin=shenwansa.blogspot.com`
4. `https://www.blogger.com/video.g?token=AD6v5dyRstz8j3GYJmdRVY2VIaEXLEHVUGmbuYt7TvNzExpn3_7B37ySzgdtQyp-PCAInJ_ps49BekQB12VCrnzvhDn7T2zsBYrcaK0R-lbmc0MvGL6EQ2-Ir8SujlOo0Ee6w7r_t7uF&origin=shenwansa.blogspot.com`

---

### Task 1: 内容完整性测试与本地媒体

**Files:**
- Create: `tests/test_site.py`
- Create: `assets/images/tutorial-2fa-1.png`
- Create: `assets/images/tutorial-2fa-2.png`
- Create: `assets/images/tutorial-2fa-3.png`
- Create: `assets/images/network-error-1.png`
- Create: `assets/images/network-error-2.png`
- Create: `assets/images/outlook-login.png`

**Interfaces:**
- Consumes: 原 Blogger 页面中的 6 个图片 URL。
- Produces: 可由 `index.html` 通过相对路径引用的 6 个本地图片文件，以及后续任务共用的完整性测试。

- [ ] **Step 1: Write the failing test**

在 `tests/test_site.py` 中使用 `html.parser.HTMLParser` 统计页面结构，并断言两个主章节、至少 12 个 FAQ、6 张本地图片、4 个视频 iframe 和 4 个备用链接存在；同时断言所有本地图片文件非空。

- [ ] **Step 2: Run test to verify it fails**

Run: `python -m unittest tests/test_site.py -v`

Expected: FAIL，因为 `index.html` 和图片文件尚未创建。

- [ ] **Step 3: Download the six exact source images**

使用 HTTP 请求下载设计文档对应的 6 个 `blogger.googleusercontent.com` 图片 URL，并依序保存为上述文件名。下载后检查每个响应为 200、内容类型以 `image/` 开头且文件大小大于 1 KB。

- [ ] **Step 4: Re-run the media portion of the test**

Run: `python -m unittest tests.test_site.SiteTests.test_local_images_exist -v`

Expected: PASS。

- [ ] **Step 5: Commit**

```bash
git add tests/test_site.py assets/images
git commit -m "test: define FAQ content contract"
```

### Task 2: 静态 FAQ 页面

**Files:**
- Create: `index.html`
- Create: `styles.css`
- Create: `script.js`

**Interfaces:**
- Consumes: `assets/images/*.png` 和设计文档中的内容顺序。
- Produces: 浏览器可直接打开的完整单页网站。

- [ ] **Step 1: Build semantic HTML**

创建包含以下稳定标识的 `index.html`：`#top`、`#warranty-plus`、`#direct-plus`、`.faq-card`、`.tutorial-image`、`.video-card iframe` 和 `.video-fallback`。使用 `<details><summary>` 实现 FAQ，使无 JavaScript 时也可展开。4 个 iframe 使用原 Blogger `video.g` 地址，备用链接统一指向原博客页面。

- [ ] **Step 2: Add responsive styles**

创建 `styles.css`，定义深绿色 `#12372a`、金色 `#d6a84b`、暖白 `#fbf8f1` 主题；内容最大宽度 1100px；媒体宽度 100%；视频容器使用 `aspect-ratio: 16 / 9`；在 720px 以下改为单栏并缩小标题字号。

- [ ] **Step 3: Add progressive enhancement**

创建 `script.js`，仅实现平滑定位、当前年份和“展开全部／收起全部”按钮。脚本通过修改所有 `.faq-card` 的 `open` 属性控制状态，不隐藏正文，也不依赖网络。

- [ ] **Step 4: Run structural tests**

Run: `python -m unittest tests/test_site.py -v`

Expected: 所有内容完整性、资源路径和链接测试 PASS。

- [ ] **Step 5: Commit**

```bash
git add index.html styles.css script.js
git commit -m "feat: build responsive FAQ website"
```

### Task 3: 发布配置与项目说明

**Files:**
- Create: `.github/workflows/pages.yml`
- Modify: `README.md`

**Interfaces:**
- Consumes: 仓库根目录静态网站。
- Produces: 每次推送 `main` 时可自动发布的 GitHub Pages 工作流。

- [ ] **Step 1: Add the Pages workflow**

工作流使用 `actions/checkout@v4`、`actions/configure-pages@v5`、`actions/upload-pages-artifact@v3` 和 `actions/deploy-pages@v4`；授予 `contents: read`、`pages: write`、`id-token: write`；仅在 `main` 推送和手动触发时运行。

- [ ] **Step 2: Update README**

README 写明网站用途、公开地址、本地预览命令 `python -m http.server 8000`、内容来源和媒体策略。

- [ ] **Step 3: Validate deployment files**

Run: `python -m unittest tests/test_site.py -v`

Expected: Pages 工作流存在且 README 包含公开地址，全部测试 PASS。

- [ ] **Step 4: Commit**

```bash
git add .github/workflows/pages.yml README.md tests/test_site.py
git commit -m "ci: deploy site to GitHub Pages"
```

### Task 4: 推送、启用和线上验证

**Files:**
- Modify: GitHub 仓库远端 `main` 分支

**Interfaces:**
- Consumes: 通过本地测试的提交。
- Produces: 可公开访问的 GitHub Pages 网站。

- [ ] **Step 1: Final local verification**

Run: `python -m unittest tests/test_site.py -v`

Expected: 全部测试 PASS，`git status --short` 无未提交网站变更。

- [ ] **Step 2: Push source commits**

Run: `git push origin main`

Expected: 远端 `main` 更新到本地 HEAD。

- [ ] **Step 3: Enable GitHub Pages**

在仓库 Settings → Pages 中将 Source 设为 GitHub Actions。若工作流已自动启用 Pages，则无需重复设置。

- [ ] **Step 4: Verify the deployment**

等待 Pages 工作流成功，然后访问 `https://jl7007.github.io/shenwansan/`，确认 HTTP 200、两个主章节、6 张图片、4 个播放器和备用链接可见。

- [ ] **Step 5: Report the result**

返回最终公开网址；如果 GitHub 要求用户登录确认，只说明需要在当前 GitHub 页面完成的单一步骤。
