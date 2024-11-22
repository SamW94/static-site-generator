import unittest
import split_images_and_links
import split_nodes_delimiter
from textnode import TextNode, TextType
from leafnode import LeafNode
from main import text_node_to_html, text_to_textnodes

class TestTextNodeToHTML(unittest.TestCase):

    def test_normaltext_conversion(self):
        text_node = TextNode("Normal text", TextType.TEXT)
        html_node = text_node_to_html(text_node)
        self.assertIsNone(html_node.tag)
        self.assertIsNone(html_node.props)
        self.assertEqual(html_node.value, "Normal text")
        # Test to_html
        self.assertEqual(html_node.to_html(), "Normal text")

    def test_bold_conversion(self):
        text_node = TextNode("Bold text", TextType.BOLD)
        html_node = text_node_to_html(text_node)
        self.assertIsNone(html_node.props)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "Bold text")
        # Test to_html
        self.assertEqual(html_node.to_html(), "<b>Bold text</b>")

    def test_italic_conversion(self):
        text_node = TextNode("Italic text", TextType.ITALIC)
        html_node = text_node_to_html(text_node)
        self.assertIsNone(html_node.props)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "Italic text")
        # Test to_html
        self.assertEqual(html_node.to_html(), "<i>Italic text</i>")

    def test_code_conversion(self):
        text_node = TextNode("Code text", TextType.CODE)
        html_node = text_node_to_html(text_node)
        self.assertIsNone(html_node.props)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "Code text")
        # Test to_html
        self.assertEqual(html_node.to_html(), "<code>Code text</code>")

    def test_link_conversion(self):
        text_node = TextNode("Link text", TextType.LINK, "https://localhost:8888")
        html_node = text_node_to_html(text_node)
        self.assertEqual(html_node.props, {"href": "https://localhost:8888"})
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "Link text")
        # Test to_html
        self.assertEqual(html_node.to_html(), '<a href="https://localhost:8888">Link text</a>')

    def test_image_conversion(self):
        text_node = TextNode("", TextType.IMAGE, "https://image.url", "alt_text")
        html_node = text_node_to_html(text_node)
        self.assertEqual(html_node.props, {"src": "https://image.url", "alt": "alt_text"})
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        # Test to_html
        self.assertEqual(html_node.to_html(), '<img src="https://image.url" alt="alt_text" />')

    def test_invalid_text_type(self):
        with self.assertRaises(AttributeError):
            TextNode("Invalid text type", TextType.NOTVALID)

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
