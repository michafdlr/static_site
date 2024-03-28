import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_propstohtml(self):
        node = HTMLNode(
            tag="p", value="test text", props={
            "href": "https://www.google.com",
            "target": "_blank"}
            )
        node2 = HTMLNode(
            tag="p", value="test text", props={
            "href": "https://www.google.com",
            "target": "not_blank",
            "something": "other"}
            )
        self.assertEqual(node.props_to_html(),
                         ' href="https://www.google.com" target="_blank"'
                         )
        self.assertEqual(node2.props_to_html(),
                         ' href="https://www.google.com" target="not_blank" something="other"'
                         )



if __name__ == "__main__":
    unittest.main()
