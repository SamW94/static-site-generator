import unittest

from markdown_to_blocks import markdown_to_blocks


class TestMarkdownToBlocks(unittest.TestCase):

    def test_markdown_no_blocks(self):
        markdown = "This is a paragraph of text."
        blocks = markdown_to_blocks(markdown)
        expected_output = ["This is a paragraph of text."]
        self.assertEqual(blocks, expected_output)

    def test_markdown_with_heading_block(self):
        markdown = "# This is a heading\n\nThis is a paragraph of text."
        blocks = markdown_to_blocks(markdown)
        expected_output = ["# This is a heading", "This is a paragraph of text."]
        self.assertEqual(blocks, expected_output)

    def test_markdown_with_leading_whitespace(self):
        markdown =" # This is a heading\n\n This is a paragraph of text."
        blocks = markdown_to_blocks(markdown)
        expected_output = ["# This is a heading", "This is a paragraph of text."]
        self.assertEqual(blocks, expected_output)

    def test_markdown_with_trailing_whitespace(self):
        markdown ="# This is a heading      \n\n This is a paragraph of text.         "
        blocks = markdown_to_blocks(markdown)
        expected_output = ["# This is a heading", "This is a paragraph of text."]
        self.assertEqual(blocks, expected_output)

    def test_markdown_with_empty_block(self):
        markdown ="# This is a heading\n\nThis is a paragraph of text.\n\n     "
        blocks = markdown_to_blocks(markdown)
        expected_output = ["# This is a heading", "This is a paragraph of text."]
        self.assertEqual(blocks, expected_output) 

    def test_markdown_with_multiple_empty_lines(self):
        markdown ="# This is a heading\n\n This is a paragraph of text.\n\n\n\n\n\n\n\n\n\n\n"
        blocks = markdown_to_blocks(markdown)
        expected_output = ["# This is a heading", "This is a paragraph of text."]
        self.assertEqual(blocks, expected_output)

    def test_markdown_with_list_items(self):
        markdown = "# This is a heading\n\n This is a paragraph of text.\n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item"
        blocks = markdown_to_blocks(markdown)
        expected_output = ["# This is a heading", "This is a paragraph of text.", "* This is the first list item in a list block\n* This is a list item\n* This is another list item"]
        self.assertEqual(blocks, expected_output)

if __name__ == "__main__":
    unittest.main()