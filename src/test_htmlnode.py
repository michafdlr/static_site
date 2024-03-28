import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

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

        leafnode1 = LeafNode("p", "This is a paragraph of text.")
        leafnode2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})

        self.assertEqual(
            leafnode1.to_html(),
            '<p>This is a paragraph of text.</p>'
        )
        self.assertEqual(
            leafnode2.to_html(),
            '<a href="https://www.google.com">Click me!</a>'
        )

        parentnode1 = ParentNode(
                "p",
                [
                    LeafNode("b", "Bold text"),
                    LeafNode(None, "Normal text"),
                    LeafNode("i", "italic text"),
                    LeafNode(None, "Normal text"),
                ],
            )

        parentnode2 = ParentNode(
                "p",
                [
                    LeafNode("b", "Bold text"),
                    LeafNode(None, "Normal text"),
                    LeafNode("i", "italic text"),
                    LeafNode(None, "Normal text"),
                ],
                {
            "href": "https://www.google.com",
            "target": "_blank"
            }
            )

        parentnode3 = ParentNode(
            children=[
                    LeafNode("b", "Bold text"),
                    LeafNode(None, "Normal text"),
                    LeafNode("i", "italic text"),
                    LeafNode(None, "Normal text"),
                ]
        )
        parentnode4 = ParentNode(
            tag = "p"
        )

        parentnode5 = ParentNode(
                "p",
                [
                    parentnode1,
                    LeafNode(None, "Normal text"),
                    LeafNode("i", "italic text"),
                    LeafNode(None, "Normal text"),
                ],
                {
            "href": "https://www.google.com",
            "target": "_blank"
            }
            )

        self.assertEqual(
            parentnode1.to_html(),
            '<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>'
        )

        self.assertEqual(
            parentnode2.to_html(),
            '<p href="https://www.google.com" target="_blank"><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>'
        )

        self.assertRaises(ValueError, parentnode3.to_html)

        self.assertRaises(ValueError, parentnode4.to_html)

        self.assertEqual(
            parentnode5.to_html(),
            '<p href="https://www.google.com" target="_blank"><p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>Normal text<i>italic text</i>Normal text</p>'
        )




if __name__ == "__main__":
    unittest.main()
