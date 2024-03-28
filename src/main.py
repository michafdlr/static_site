from textnode import TextNode
from htmlnode import HTMLNode, LeafNode, ParentNode

def main():
    textnode = TextNode("This is a text node", "bold", "https://www.boot.dev")
    htmlnode = HTMLNode(
            tag="p", value="test text", props={
            "href": "https://www.google.com",
            "target": "_blank"}
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
    print(parentnode5.to_html())
    return

if __name__ == "__main__":
    main()
