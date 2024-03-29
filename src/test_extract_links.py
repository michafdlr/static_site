from extract_links import extract_markdown_images, extract_markdown_links
import unittest

class TestExtractLinks(unittest.TestCase):
    def test_extract_image(self):
        extraction = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and ![another](https://i.imgur.com/dfsdkjfd.png)"
            )
        self.assertEqual(
            extraction,
            [("image", "https://i.imgur.com/zjjcJKZ.png"), ("another", "https://i.imgur.com/dfsdkjfd.png")]
        )

    def test_extract_link(self):
        extraction = extract_markdown_links(
            "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
        )
        self.assertEqual(
            extraction,
            [("link", "https://www.example.com"), ("another", "https://www.example.com/another")]
        )


if __name__ == "__main__":
    unittest.main()
