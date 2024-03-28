from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_types
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
