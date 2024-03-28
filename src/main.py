from textnode import TextNode
from htmlnode import HTMLNode

def main():
    textnode = TextNode("This is a text node", "bold", "https://www.boot.dev")
    htmlnode = HTMLNode(
            tag="p", value="test text", props={
            "href": "https://www.google.com",
            "target": "_blank"}
            )
    return textnode, htmlnode

if __name__ == "__main__":
    print(main())
