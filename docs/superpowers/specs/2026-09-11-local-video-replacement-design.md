# 本地教程视频替换设计

## 目标

将网站中 4 个 Blogger 嵌入播放器替换为用户提供的本地教程视频，使页面不再依赖 Blogger 视频服务，并保持桌面与移动浏览器的稳定播放。

## 视频映射与格式

| 页面教程 | 输入文件 | 网站文件 | 处理方式 |
| --- | --- | --- | --- |
| 成品 PLUS 登录方法 | `成品PLUS登录方法.mp4` | `assets/videos/product-plus-login.mp4` | 直接复制，保留 H.264/AAC 原始媒体流。 |
| 境外手机号接码教程 | `国外手机号接码教程.mp4` | `assets/videos/phone-verification.mp4` | 转码为 H.264/AAC MP4，保留 1280×720 分辨率，确保通用浏览器兼容。 |
| QQ 邮箱注册 GPT 账号 | `QQ 邮箱注册 GPT 账号.mov` | `assets/videos/qq-email-register.mp4` | 无损重新封装为 MP4，保留 H.264/AAC 原始媒体流。 |
| GPT Free 升级为 PLUS | `GPT Free 升级为 PLUS.mp4` | `assets/videos/free-to-plus-upgrade.mp4` | 直接复制，保留 H.264/AAC 原始媒体流。 |

四个视频合计约 20.4 MB；每个文件远低于 GitHub 普通仓库 100 MiB 的单文件上限，也远低于 GitHub Pages 1 GB 的站点上限。

## 页面改动

- 保持每个教程的标题、位置和说明不变。
- 将每个 `.video-frame` 内的 `<iframe>` 替换为原生 `<video>` 元素。
- 视频启用 `controls`、`preload="metadata"`、`playsinline` 和 `controlsList="nodownload"`；用户可在浏览器中全屏、播放和拖动进度。
- 将“前往原页面观看”链接改为“直接打开视频”，指向仓库内相对视频文件，作为播放器不可用时的备用入口。
- 删除所有 `blogger.com/video.g` 地址；网站的视频内容仅来自这四个本地文件。

## 验证与发布

- 逐个解码验证输出文件，确认视频与音频流可读取。
- 自动测试改为验证 4 个本地 MP4、4 个 `<video>` 元素，以及页面中不存在 Blogger 视频地址。
- 本地 HTTP 服务检查页面和每个视频资源均返回 200。
- 提交并推送 `main` 分支，等待现有 GitHub Pages 工作流成功后验证公开页面。

## 异常处理

- 任何视频转换或解码失败时，不推送不完整媒体；保留已验证的视频文件并报告具体失败项。
- 若 GitHub 推送因文件大小或网络问题失败，保持本地提交不变，并按失败原因重试或调整媒体处理。
