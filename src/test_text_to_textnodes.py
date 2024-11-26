import unittest
from text_to_textnodes import text_to_textnodes
from split_nodes_delimiter import split_nodes_delimiter
from textnode import TextNode, TextType

class TestTextToTextNodes(unittest.TestCase):
    
    def test_text_no_formatting(self):
        text = "This is text with no special formatting."
        text_nodes = text_to_textnodes(text)
        expected_output = [TextNode("This is text with no special formatting.", TextType.TEXT)]
        self.assertEqual(text_nodes, expected_output)

    def test_text_bold_formatting(self):
        text = "This is text with **bold formatting.**"
        text_nodes = text_to_textnodes(text)
        expected_output = [TextNode("This is text with ", TextType.TEXT), TextNode("bold formatting.", TextType.BOLD,), TextNode("", TextType.TEXT)]
        self.assertEqual(text_nodes, expected_output)

    def test_text_italic_formatting(self):
        text = "This is text with *italic formatting.*"
        text_nodes = text_to_textnodes(text)
        expected_output = [TextNode("This is text with ", TextType.TEXT), TextNode("italic formatting.", TextType.ITALIC), TextNode("", TextType.TEXT)]
        self.assertEqual(text_nodes, expected_output)

    def test_text_code_formatting(self):
        text = "This is text with `code formatting.`"
        text_nodes = text_to_textnodes(text)
        expected_output = [TextNode("This is text with ", TextType.TEXT), TextNode("code formatting.", TextType.CODE), TextNode("", TextType.TEXT)]
        self.assertEqual(text_nodes, expected_output)

    def test_text_image_formatting(self):
        text = "This is text with ![image formatting](https://i.imgur.com/8HJoyoy.jpeg)."
        text_nodes = text_to_textnodes(text)
        expected_output = [TextNode("This is text with ", TextType.TEXT), TextNode("image formatting", TextType.IMAGE, "https://i.imgur.com/8HJoyoy.jpeg"), TextNode(".", TextType.TEXT)]
        self.assertEqual(text_nodes, expected_output)

    def test_text_link_formatting(self):
        text = "This is text with [link formatting](https://github.com/SamW94)."
        text_nodes = text_to_textnodes(text)
        expected_output = [TextNode("This is text with ", TextType.TEXT), TextNode("link formatting", TextType.LINK, "https://github.com/SamW94"), TextNode(".", TextType.TEXT)]
        self.assertEqual(text_nodes, expected_output)

    def test_text_all_formats(self):
        text = "This is text with no special formatting. This is text with **bold formatting.** This is text with *italic formatting.* This is text with `code formatting.` This is text with ![image formatting](https://i.imgur.com/8HJoyoy.jpeg). This is text with [link formatting](https://github.com/SamW94)."
        text_nodes = text_to_textnodes(text)
        expected_output = [TextNode("This is text with no special formatting. This is text with ", TextType.TEXT), TextNode("bold formatting.", TextType.BOLD), TextNode(" This is text with ", TextType.TEXT), TextNode("italic formatting.", TextType.ITALIC), TextNode(" This is text with ", TextType.TEXT), TextNode("code formatting.", TextType.CODE), TextNode(" This is text with ", TextType.TEXT), TextNode("image formatting", TextType.IMAGE, "https://i.imgur.com/8HJoyoy.jpeg"), TextNode(". This is text with ", TextType.TEXT), TextNode("link formatting", TextType.LINK, "https://github.com/SamW94"), TextNode(".", TextType.TEXT)]
        self.assertEqual(text_nodes, expected_output)

    def test_adjacent_delimiters(self):
        text = "Here are some adjacent delimiters: **bold***italic*`code`![image formatting](https://i.imgur.com/8HJoyoy.jpeg)[link formatting](https://github.com/SamW94)"
        text_nodes = text_to_textnodes(text)
        expected_output = [TextNode("Here are some adjacent delimiters: ", TextType.TEXT), TextNode("bold", TextType.BOLD), TextNode("", TextType.TEXT), TextNode("italic", TextType.ITALIC), TextNode("", TextType.TEXT), TextNode("code", TextType.CODE), TextNode("image formatting", TextType.IMAGE, "https://i.imgur.com/8HJoyoy.jpeg"), TextNode("link formatting", TextType.LINK, "https://github.com/SamW94")]
        self.assertEqual(text_nodes, expected_output)

    def test_invalid_delimiters(self):
        text = "This is text with an _invalid delimiter_."
        text_nodes = text_to_textnodes(text)
        expected_output = [TextNode("This is text with an _invalid delimiter_.", TextType.TEXT)]
        self.assertEqual(text_nodes, expected_output)

    def test_nested_delimiter(self):
        text = "This is text with **bold text with an *italics* word nested in it.**"
        text_nodes = text_to_textnodes(text)
        expected_output = [TextNode("This is text with ", TextType.TEXT), TextNode("bold text with an *italics* word nested in it.", TextType.BOLD), TextNode("", TextType.TEXT)]
        self.assertEqual(text_nodes, expected_output)

    def test_missing_closing_delimiter(self):
        text = "This has **bold text but no closing delimiter."
        text_nodes = text_to_textnodes(text)
        expected_output = [TextNode("This has **bold text but no closing delimiter.", TextType.TEXT)]
        self.assertEqual(text_nodes, expected_output)

    def test_malformed_image(self):
        text = "This has a ![missing bracket](https://i.imgur.com/ASapCmz.png"
        text_nodes = text_to_textnodes(text)
        expected_output = [TextNode("This has a ![missing bracket](https://i.imgur.com/ASapCmz.png", TextType.TEXT)]
        self.assertEqual(text_nodes, expected_output)

if __name__ == '__main__':
    unittest.main()