import unittest

from htmlnode import HTMLNode, LeafNode

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

        leafnode1 = LeafNode("p", "This is a paragraph of text.")
        leafnode2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})

        self.assertEqual(node.props_to_html(),
                         ' href="https://www.google.com" target="_blank"'
                         )
        self.assertEqual(node2.props_to_html(),
                         ' href="https://www.google.com" target="not_blank" something="other"'
                         )

        self.assertEqual(
            leafnode1.to_html(),
            '<p>This is a paragraph of text.</p>'
        )
        self.assertEqual(
            leafnode2.to_html(),
            '<a href="https://www.google.com">Click me!</a>'
        )




if __name__ == "__main__":
    unittest.main()
