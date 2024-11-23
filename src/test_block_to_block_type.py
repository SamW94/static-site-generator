import unittest

from block_to_block_type import block_to_block_type

class TextBlockToBlockType(unittest.TestCase):

    def test_paragraph(self):
        block = "This is a paragraph."
        block_type = block_to_block_type(block)
        expected_output = "paragraph"
        self.assertEqual(block_type, expected_output)
    
    def test_heading_block_one_hash(self):
        block = "# This is a heading."
        block_type = block_to_block_type(block)
        expected_output = "heading"
        self.assertEqual(block_type, expected_output)

    def test_heading_block_multiple_hashes(self):
        block = "###### This is a heading."
        block_type = block_to_block_type(block)
        expected_output = "heading"
        self.assertEqual(block_type, expected_output)

    def test_heading_block_too_many_hashes(self):
        block = "####### This is a heading."
        block_type = block_to_block_type(block)
        expected_output = "paragraph"
        self.assertEqual(block_type, expected_output)

    def test_heading_block_no_space(self):
        block = "#This is a heading."
        block_type = block_to_block_type(block)
        expected_output = "paragraph"
        self.assertEqual(block_type, expected_output)

    def test_code_block(self):
        block = "```This is a code block.```"
        block_type = block_to_block_type(block)
        expected_output = "code"
        self.assertEqual(block_type, expected_output)

    def test_code_block_invalid_number_of_backticks(self):
        block = "``This is a code block.``"
        block_type = block_to_block_type(block)
        expected_output = "paragraph"
        self.assertEqual(block_type, expected_output)

    def test_code_block_no_trailing_backticks(self):
        block = "```This is a code block."
        block_type = block_to_block_type(block)
        expected_output = "paragraph"
        self.assertEqual(block_type, expected_output)

    def test_code_block_no_leading_backticks(self):
        block = "This is a code block.```"
        block_type = block_to_block_type(block)
        expected_output = "paragraph"
        self.assertEqual(block_type, expected_output)

    def test_quote_block_one_line(self):
        block = ">This is a quote block."
        block_type = block_to_block_type(block)
        expected_output = "quote"
        self.assertEqual(block_type, expected_output)
    
    def test_quote_block_multiple_lines(self):
        block = ">This is a quote block.\n>This is another quote."
        block_type = block_to_block_type(block)
        expected_output = "quote"
        self.assertEqual(block_type, expected_output)
    
    def test_quote_block_missing_greater_than_on_one_line(self):
        block = ">This is a quote block.\n>This is another quote.\nThis is trying to be a quote."
        block_type = block_to_block_type(block)
        expected_output = "paragraph"
        self.assertEqual(block_type, expected_output)

    def test_unordered_list_block(self):
        block = "* This is an unordered list."
        block_type = block_to_block_type(block)
        expected_output = "unordered_list"
        self.assertEqual(block_type, expected_output)

    def test_unordered_list_block_multiple_lines(self):
        block = "* This is an unordered list.\n* This is another unordered list item."
        block_type = block_to_block_type(block)
        expected_output = "unordered_list"
        self.assertEqual(block_type, expected_output)

    def test_unordered_list_block_mixed_characters(self):
        block = "* This is an unordered list.\n- This is another unordered list item."
        block_type = block_to_block_type(block)
        expected_output = "unordered_list"
        self.assertEqual(block_type, expected_output)

    def test_unordered_list_block_no_space(self):
        block = "*This is an unordered list."
        block_type = block_to_block_type(block)
        expected_output = "paragraph"
        self.assertEqual(block_type, expected_output)

    def test_unordered_list_block_multiple_lines_no_space(self):
        block = "* This is an unordered list.\n-This is another unordered list item."
        block_type = block_to_block_type(block)
        expected_output = "paragraph"
        self.assertEqual(block_type, expected_output)

    def test_ordered_list_block(self):
        block = "1. This is an ordered list."
        block_type = block_to_block_type(block)
        expected_output = "ordered_list"
        self.assertEqual(block_type, expected_output)

    def test_ordered_list_block_multiple_lines(self):
        block = "1. This is an ordered list.\n2. This is the second item in the list."
        block_type = block_to_block_type(block)
        expected_output = "ordered_list"
        self.assertEqual(block_type, expected_output)

    def test_ordered_list_block_wrong_starting_number(self):
        block = "2. This is an ordered list."
        block_type = block_to_block_type(block)
        expected_output = "paragraph"
        self.assertEqual(block_type, expected_output)

    def test_ordered_list_block_wrong_second_line_number(self):
        block = "1. This is an ordered list.\n3. This is the second item in the list."
        block_type = block_to_block_type(block)
        expected_output = "paragraph"
        self.assertEqual(block_type, expected_output)

    def test_ordered_list_block_no_space(self):
        block = "1.This is an ordered list."
        block_type = block_to_block_type(block)
        expected_output = "paragraph"
        self.assertEqual(block_type, expected_output) 

    def test_ordered_list_block_multiple_lines_no_space(self):
        block = "1.This is an ordered list.\n2.This is the second item in the list."
        block_type = block_to_block_type(block)
        expected_output = "paragraph"
        self.assertEqual(block_type, expected_output)  

if __name__ == "__main__":
    unittest.main()