from split_nodes_delimiter import split_nodes_delimiter
from textnode import TextNode, TextType
import unittest

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_code_text_type(self):
        node = TextNode("This textnode contains a `code block` within.", TextType.TEXT)
        new_nodes_list = split_nodes_delimiter([node], "`", TextType.CODE)
        expected_output_list = [TextNode("This textnode contains a ", TextType.TEXT), TextNode("code block", TextType.CODE), TextNode(" within.", TextType.TEXT)]
        self.assertEqual(new_nodes_list, expected_output_list)

    def test_bold_text_type(self):
        node = TextNode("This textnode contains **bold text** within.", TextType.TEXT)
        new_nodes_list = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected_output_list = [TextNode("This textnode contains ", TextType.TEXT), TextNode("bold text", TextType.BOLD), TextNode(" within.", TextType.TEXT)]
        self.assertEqual(new_nodes_list, expected_output_list)  

    def test_italics_text_type(self):
        node = TextNode("This textnode contains *italic text* within.", TextType.TEXT)
        new_nodes_list = split_nodes_delimiter([node], "*", TextType.ITALIC)
        expected_output_list = [TextNode("This textnode contains ", TextType.TEXT), TextNode("italic text", TextType.ITALIC), TextNode(" within.", TextType.TEXT)]
        self.assertEqual(new_nodes_list, expected_output_list)  

    def test_multiple_delimiters(self):
        node = TextNode("This textnode contains a `code block` within. Here is a `second code block` just because.", TextType.TEXT)
        new_nodes_list = split_nodes_delimiter([node], "`", TextType.CODE)
        expected_output_list = [TextNode("This textnode contains a ", TextType.TEXT), TextNode("code block", TextType.CODE), TextNode(" within. Here is a ", TextType.TEXT), TextNode("second code block", TextType.CODE), TextNode(" just because.", TextType.TEXT)]
        self.assertEqual(new_nodes_list, expected_output_list)

    def test_missing_closing_delimiters(self):
        node = TextNode("This textnode is missing a `closing delimiter!", TextType.TEXT)
        new_nodes_list = split_nodes_delimiter([node], "`", TextType.CODE)
        expected_output_list = [TextNode("This textnode is missing a `closing delimiter!", TextType.TEXT)]
        self.assertEqual(new_nodes_list, expected_output_list)

    def test_with_delimiters_at_start(self):
        node = TextNode("`The code block` comes first this time.", TextType.TEXT)
        new_nodes_list = split_nodes_delimiter([node], "`", TextType.CODE)
        expected_output_list = [TextNode("", TextType.TEXT), TextNode("The code block", TextType.CODE), TextNode(" comes first this time.", TextType.TEXT)]
        self.assertEqual(new_nodes_list, expected_output_list)

    def test_with_delimiters_at_end(self):
        node = TextNode("Here's a textnode with the `code block at the end.`", TextType.TEXT)
        new_nodes_list = split_nodes_delimiter([node], "`", TextType.CODE)
        expected_output_list = [TextNode("Here's a textnode with the ", TextType.TEXT), TextNode("code block at the end.", TextType.CODE), TextNode("", TextType.TEXT)]
        self.assertEqual(new_nodes_list, expected_output_list)

if __name__ == "__main__":
    unittest.main()