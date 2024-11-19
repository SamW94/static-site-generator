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
    pass

if __name__ == '__main__':
    unittest.main()