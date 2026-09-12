from html.parser import HTMLParser
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
IMAGE_PATHS = [
    "assets/images/tutorial-2fa-1.png",
    "assets/images/tutorial-2fa-2.png",
    "assets/images/tutorial-2fa-3.png",
    "assets/images/network-error-1.png",
    "assets/images/network-error-2.png",
    "assets/images/outlook-login.png",
]

VIDEO_PATHS = [
    "assets/videos/product-plus-login.mp4",
    "assets/videos/phone-verification.mp4",
    "assets/videos/qq-email-register.mp4",
    "assets/videos/free-to-plus-upgrade.mp4",
]


class SiteParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()
        self.faq_count = 0
        self.local_images = []
        self.video_elements = []
        self.video_sources = []
        self.video_fallbacks = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get("id"):
            self.ids.add(attrs["id"])
        classes = set(attrs.get("class", "").split())
        if tag == "details" and "faq-card" in classes:
            self.faq_count += 1
        if tag == "img" and "tutorial-image" in classes:
            self.local_images.append(attrs.get("src", ""))
        if tag == "video" and "tutorial-video" in classes:
            self.video_elements.append(attrs)
        if tag == "source" and "video-source" in classes:
            self.video_sources.append(attrs.get("src", ""))
        if tag == "a" and "video-fallback" in classes:
            self.video_fallbacks.append(attrs.get("href", ""))


class SiteTests(unittest.TestCase):
    def parse_site(self):
        index = ROOT / "index.html"
        self.assertTrue(index.exists(), "index.html must exist")
        parser = SiteParser()
        parser.feed(index.read_text(encoding="utf-8"))
        return parser

    def test_required_structure_and_media(self):
        parser = self.parse_site()
        self.assertTrue({"top", "warranty-plus", "direct-plus"}.issubset(parser.ids))
        self.assertGreaterEqual(parser.faq_count, 12)
        self.assertEqual(parser.local_images, IMAGE_PATHS)
        self.assertEqual(len(parser.video_elements), 4)
        self.assertEqual(parser.video_sources, VIDEO_PATHS)
        self.assertEqual(len(parser.video_fallbacks), 4)
        html = (ROOT / "index.html").read_text(encoding="utf-8")
        self.assertNotIn("blogger.com/video.g", html)

    def test_required_topics_are_present(self):
        html = (ROOT / "index.html").read_text(encoding="utf-8")
        required_topics = (
            "如何使用质保 30 天成品 PLUS 卡密",
            "如何增加 GPT 密码以及 2FA 保护",
            "是否需要接国外手机验证码",
            "售后客服找谁",
            "可以用多久",
            "是否可以退货退款",
            "省心服务",
            "购买之后找不到卡密",
            "当前节点网络不畅",
            "CC Switch",
            "登录 Outlook 邮箱",
            "如何注册 GPT 账号",
            "GPT Free 如何升级为 PLUS",
        )
        for topic in required_topics:
            self.assertIn(topic, html)

    def test_hero_uses_tutorial_title_without_old_intro(self):
        html = (ROOT / "index.html").read_text(encoding="utf-8")
        self.assertIn("<title>使用教程｜沈万三</title>", html)
        self.assertIn("<h1>使用教程</h1>", html)
        self.assertNotIn(
            "把账号使用、验证码、售后与故障处理集中到一个页面。"
            "遇到问题时，先按分类找到对应答案。",
            html,
        )

    def test_local_images_exist(self):
        for relative_path in IMAGE_PATHS:
            image = ROOT / relative_path
            self.assertTrue(image.exists(), f"missing {relative_path}")
            self.assertGreater(image.stat().st_size, 1024, f"empty {relative_path}")

    def test_local_videos_exist(self):
        for relative_path in VIDEO_PATHS:
            video = ROOT / relative_path
            self.assertTrue(video.exists(), f"missing {relative_path}")
            self.assertGreater(video.stat().st_size, 1024, f"empty {relative_path}")

    def test_supporting_files_and_pages_workflow_exist(self):
        for relative_path in ("styles.css", "script.js", ".github/workflows/pages.yml"):
            self.assertTrue((ROOT / relative_path).exists(), f"missing {relative_path}")
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("https://jl7007.github.io/shenwansan/", readme)


if __name__ == "__main__":
    unittest.main()
