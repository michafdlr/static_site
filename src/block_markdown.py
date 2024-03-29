block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered_list"
block_type_ordered_list = "ordered_list"


def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    blocks = [block.strip() for block in blocks if block.strip()!=""]
    return blocks

def block_to_blocktype(block):
    if block.startswith("#"):
        text = block
        while text.startswith("#"):
            text = text.lstrip("#")
        if text.startswith(" "):
            return block_type_heading
        else:
            return block_type_paragraph
    if block.startswith("```") and block.endswith("```"):
        return block_type_code
    if block.startswith(">"):
        for line in block.split("\n"):
            if not line.startswith(">"):
                return block_type_paragraph
        return block_type_quote
    if block.startswith("* ") or block.startswith("- "):
        for line in block.split("\n"):
            if not line.startswith("* ") and not line.startswith("- "):
                return block_type_paragraph
        return block_type_unordered_list
    if block.startswith("1."):
        counter = 1
        for line in block.split("\n"):
            if not line.startswith(f"{counter}."):
                return block_type_paragraph
            counter += 1
        return block_type_ordered_list
    return block_type_paragraph
