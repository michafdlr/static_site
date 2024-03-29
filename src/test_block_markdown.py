import unittest

from block_markdown import (
    markdown_to_blocks,
    block_to_blocktype
)

class TestBlockMarkdown(unittest.TestCase):
    def test_markdown_to_blocks(self):
        text = """This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
        """
        self.assertListEqual(
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items"
            ],
            markdown_to_blocks(text)
        )
    def test_block_to_blocktype(self):
        block_heading = "## headingtext"
        block_code = "```here comes the code```"
        block_quote = ">first line\n>second line"
        block_unordered_list = "* first item\n* second item\n* third item"
        block_ordered_list = "1. first item\n2. second item\n3. third item"
        block_paragraph = "This is a #normal paragraph\n where only x\n>y\nand 1.stuff"

        self.assertEqual("heading", block_to_blocktype(block_heading))
        self.assertEqual("code", block_to_blocktype(block_code))
        self.assertEqual("quote", block_to_blocktype(block_quote))
        self.assertEqual("unordered_list", block_to_blocktype(block_unordered_list))
        self.assertEqual("ordered_list", block_to_blocktype(block_ordered_list))
        self.assertEqual("paragraph", block_to_blocktype(block_paragraph))


if __name__ == "__main__":
    unittest.main()
