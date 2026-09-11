# 本地教程视频替换 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 将 4 个 Blogger 视频嵌入替换为仓库中的本地 MP4 视频，并重新发布 GitHub Pages。

**Architecture:** 视频存放在 `assets/videos/`。已有 H.264/AAC MP4 直接复制，MOV 无损封装为 MP4，HEVC MP4 转为 H.264/AAC；页面使用 `<video>` 标签引用这些相对路径。

**Tech Stack:** FFmpeg、HTML5 video、Python `unittest`、GitHub Actions、GitHub Pages

## Global Constraints

- 保留四段视频内容、顺序和页面标题。
- 所有网页播放器均使用 H.264/AAC MP4，提供原生控制栏和内联播放。
- 页面中不得存在 `blogger.com/video.g`。
- 视频总大小保持远低于 1 GB，单文件保持低于 100 MiB。
- 推送到 `main` 后由现有 GitHub Pages 工作流发布。

---

### Task 1: 生成并验证网站视频文件

**Files:**
- Create: `assets/videos/product-plus-login.mp4`
- Create: `assets/videos/phone-verification.mp4`
- Create: `assets/videos/qq-email-register.mp4`
- Create: `assets/videos/free-to-plus-upgrade.mp4`

**Interfaces:**
- Consumes: `C:\Users\lijia40\Desktop\成品PLUS登录方法.mp4`、`C:\Users\lijia40\Desktop\国外手机号接码教程.mp4`、`C:\Users\lijia40\Desktop\QQ 邮箱注册 GPT 账号.mov`、`C:\Users\lijia40\Desktop\GPT Free 升级为 PLUS.mp4`。
- Produces: 4 个 `assets/videos/*.mp4` 文件，均含 H.264 视频和 AAC 音频。

- [ ] **Step 1: Create the source-video verification command**

Run:

```powershell
ffprobe -v error -show_entries stream=codec_type,codec_name -of csv=p=0 'C:\Users\lijia40\Desktop\国外手机号接码教程.mp4'
```

Expected: output includes `video,hevc` and `audio,aac`.

- [ ] **Step 2: Generate the four outputs**

Run:

```powershell
ffmpeg -y -i 'C:\Users\lijia40\Desktop\成品PLUS登录方法.mp4' -map 0 -c copy -movflags +faststart assets/videos/product-plus-login.mp4
ffmpeg -y -i 'C:\Users\lijia40\Desktop\国外手机号接码教程.mp4' -map 0:v:0 -map 0:a:0? -c:v libx264 -preset slow -crf 21 -c:a aac -b:a 128k -movflags +faststart assets/videos/phone-verification.mp4
ffmpeg -y -i 'C:\Users\lijia40\Desktop\QQ 邮箱注册 GPT 账号.mov' -map 0 -c copy -movflags +faststart assets/videos/qq-email-register.mp4
ffmpeg -y -i 'C:\Users\lijia40\Desktop\GPT Free 升级为 PLUS.mp4' -map 0 -c copy -movflags +faststart assets/videos/free-to-plus-upgrade.mp4
```

- [ ] **Step 3: Verify video codecs and decodeability**

Run:

```powershell
ffprobe -v error -select_streams v:0 -show_entries stream=codec_name -of default=nw=1 assets/videos/phone-verification.mp4
ffmpeg -v error -i assets/videos/phone-verification.mp4 -f null NUL
```

Expected: probe reports `codec_name=h264`; decode exits with code 0.

- [ ] **Step 4: Commit**

```bash
git add assets/videos
git commit -m "assets: add local tutorial videos"
```

### Task 2: Replace the embedded player markup and tests

**Files:**
- Modify: `index.html`
- Modify: `tests/test_site.py`

**Interfaces:**
- Consumes: the 4 exact relative paths created in Task 1.
- Produces: four `.tutorial-video` `<video>` elements with direct-file fallback links.

- [ ] **Step 1: Write the failing contract**

Add these assertions to `tests/test_site.py`:

```python
self.assertEqual(len(parser.video_elements), 4)
self.assertEqual(parser.video_sources, VIDEO_PATHS)
self.assertNotIn("blogger.com/video.g", html)
```

where `VIDEO_PATHS` is exactly:

```python
[
    "assets/videos/product-plus-login.mp4",
    "assets/videos/phone-verification.mp4",
    "assets/videos/qq-email-register.mp4",
    "assets/videos/free-to-plus-upgrade.mp4",
]
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python -m unittest tests/test_site.py -v`

Expected: FAIL because the page still has iframe elements.

- [ ] **Step 3: Replace every iframe with a native video element**

For each player, use this exact structure with the appropriate `src` and title:

```html
<video class="tutorial-video" controls preload="metadata" playsinline controlslist="nodownload">
  <source src="assets/videos/product-plus-login.mp4" type="video/mp4">
  你的浏览器不支持视频播放，请使用下方链接打开视频。
</video>
<a class="video-fallback" href="assets/videos/product-plus-login.mp4" target="_blank" rel="noopener noreferrer">直接打开视频</a>
```

- [ ] **Step 4: Run test to verify it passes**

Run: `python -m unittest tests/test_site.py -v`

Expected: PASS with all local-image, local-video, page-structure and workflow tests green.

- [ ] **Step 5: Commit**

```bash
git add index.html tests/test_site.py
git commit -m "feat: use local tutorial video players"
```

### Task 3: Publish and verify GitHub Pages

**Files:**
- Modify: GitHub repository branch `main`

**Interfaces:**
- Consumes: commits from Tasks 1 and 2.
- Produces: a Pages deployment serving the 4 local MP4 files.

- [ ] **Step 1: Check deployed file size and working tree**

Run:

```powershell
Get-ChildItem assets/videos | Measure-Object -Property Length -Sum
git status --short
```

Expected: total video size below 1 GB and no uncommitted website changes.

- [ ] **Step 2: Push the main branch**

Run: `git push origin main`

Expected: `main -> main` completes successfully.

- [ ] **Step 3: Verify public resources**

Run:

```powershell
Invoke-WebRequest -UseBasicParsing 'https://jl7007.github.io/shenwansan/assets/videos/product-plus-login.mp4'
Invoke-WebRequest -UseBasicParsing 'https://jl7007.github.io/shenwansan/assets/videos/phone-verification.mp4'
```

Expected: both responses return HTTP 200 and `Content-Type` beginning with `video/`.
