import unittest

from textnode import TextNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        node3 = TextNode("This is a text node", "italic")
        node4 = TextNode("Another text", "bold", "www.google.de")
        node5 = TextNode("Another text", "bold", "www.google.de")
        self.assertEqual(node, node2)
        self.assertNotEqual(node, node3)
        self.assertEqual(node4, node5)

if __name__ == "__main__":
    unittest.main()
