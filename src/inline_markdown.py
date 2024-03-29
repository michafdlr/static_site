from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link,
    text_types
)
from extract_links import(
    extract_markdown_images,
    extract_markdown_links
)

delimiter_bold = "**"
delimiter_italic = "*"
delimiter_code = "`"

delimiters = [delimiter_bold, delimiter_italic, delimiter_code]


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type not in text_types or delimiter not in node.text or delimiter not in delimiters:
            new_nodes.append(node)
        else:
            cur_nodes = []
            text_split = node.text.split(delimiter)
            if len(text_split)%2 == 0:
                raise Exception("no matching delimiters")
            for i in range(len(text_split)):
                if text_split[i] == "":
                    continue
                if i%2==0:
                    cur_nodes.append(TextNode(text_split[i], text_type_text))
                else:
                    cur_nodes.append(TextNode(text_split[i], text_type))
            new_nodes.extend(cur_nodes)
    return new_nodes


def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type not in text_types:
            new_nodes.append(node)
        else:
            cur_nodes = []
            matches = extract_markdown_images(node.text)
            if not matches:
                if node.text != "":
                    new_nodes.append(node)
            else:
                original_text = node.text
                for image in matches:
                    cur_split = original_text.split(f"![{image[0]}]({image[1]})", 1)
                    if len(cur_split) != 2:
                        raise Exception("Invalid markdown; image section not closed")
                    if cur_split[0] != "":
                        cur_nodes.append(TextNode(cur_split[0], text_type_text))
                    cur_nodes.append(TextNode(image[0], text_type_image, image[1]))
                    original_text = cur_split[1]
                if original_text and original_text != "":
                    cur_nodes.append(TextNode(original_text,text_type_text))
                new_nodes += cur_nodes
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type not in text_types:
            new_nodes.append(node)
        else:
            cur_nodes = []
            matches = extract_markdown_links(node.text)
            if not matches:
                if node.text != "":
                    new_nodes.append(node)
            else:
                original_text = node.text
                for link in matches:
                    cur_split = original_text.split(f"[{link[0]}]({link[1]})", 1)
                    if len(cur_split) != 2:
                        raise Exception("Invalid markdown; link section not closed")
                    if cur_split[0] != "":
                        cur_nodes.append(TextNode(cur_split[0], text_type_text))
                    cur_nodes.append(TextNode(link[0], text_type_link, link[1]))
                    original_text = cur_split[1]
                if original_text and original_text != "":
                    cur_nodes.append(TextNode(original_text,text_type_text))
                new_nodes += cur_nodes
    return new_nodes

def text_to_textnodes(text):
    node = TextNode(text, text_type_text)
    new_nodes = [node]
    for text_type, delimiter in zip([text_type_bold, text_type_italic, text_type_code], delimiters):
        new_nodes = split_nodes_delimiter(new_nodes, delimiter, text_type)
    return split_nodes_link(split_nodes_image(new_nodes))

print(text_to_textnodes("This is **text** with an *italic* word and a `code block` and an ![image](https://i.imgur.com/zjjcJKZ.png) and a [link](https://boot.dev)"))
