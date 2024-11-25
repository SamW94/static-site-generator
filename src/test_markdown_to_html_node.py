import unittest

from markdown_to_html_node import markdown_to_html_node
from htmlnode import HTMLNode

class TestMarkdownToHTMLNode(unittest.TestCase):

    def test_header_block_one_hash(self):
        markdown = "# This is a heading.\n\n"
        html_node = markdown_to_html_node(markdown)
        expected_output = HTMLNode(tag="div", value=None, children=[HTMLNode(tag="h1", value="This is a heading.", props=None)], props=None)
        self.assertEqual(html_node, expected_output)

    def test_header_block_multiple_hashes(self):
        markdown = "### This is a heading.\n\n"
        html_node = markdown_to_html_node(markdown)
        expected_output = HTMLNode(tag="div", value=None, children=[HTMLNode(tag="h3", value="This is a heading.", props=None)], props=None)
        self.assertEqual(html_node, expected_output)
        
    def test_code_block(self):
        markdown = "```This is a code block```\n\n"
        html_node = markdown_to_html_node(markdown)
        expected_output = HTMLNode(tag="div", value=None, children=[HTMLNode(tag="pre", value=None, children=[HTMLNode(tag="code", value="This is a code block", children=None, props=None)], props=None)], props=None)
        self.assertEqual(html_node, expected_output)

    def test_quote_block(self):
        markdown = ">This is a quote block.\n>This is another quote.\n\n"
        html_node = markdown_to_html_node(markdown)
        expected_output = HTMLNode(tag="div", value=None, children=[HTMLNode(tag="blockquote", value="This is a quote block.\nThis is another quote.", children=None, props=None)], props=None)
        self.assertEqual(html_node, expected_output)

    def test_unordered_list_block(self):
        markdown = "* This is the first list item in a list block\n* This is a list item\n* This is another list item\n\n"
        html_node = markdown_to_html_node(markdown)
        expected_output = HTMLNode(tag="div", value=None, children=[HTMLNode(tag="ul", value=None, children=[HTMLNode(tag="li", value="This is the first list item in a list block", children=None, props=None), HTMLNode(tag="li", value="This is a list item", children=None, props=None), HTMLNode(tag="li", value="This is another list item", children=None, props=None)], props=None)], props=None)
        self.assertEqual(html_node, expected_output)

    def test_ordered_list_block(self):
        markdown = "1. This is an ordered list.\n2. This is the second item in the list.\n\n"
        html_node = markdown_to_html_node(markdown)
        expected_output = HTMLNode(tag="div", value=None, children=[HTMLNode(tag="ol", value=None, children=[HTMLNode(tag="li", value="This is an ordered list.", children=None, props=None), HTMLNode(tag="li", value="This is the second item in the list.", children=None, props=None)], props=None)], props=None)
        self.assertEqual(html_node, expected_output)

    def test_paragraph_block(self):
        markdown = "This is another paragaph of text that contains **bold formatting,** and *italic formatting* and text with `code formatting` and text with ![image formatting](https://i.imgur.com/8HJoyoy.jpeg) and text with [link formatting](https://github.com/SamW94)."
        html_node = markdown_to_html_node(markdown)
        expected_output = HTMLNode(tag="div", value=None, children=[HTMLNode(tag="p", value="This is another paragaph of text that contains **bold formatting,** and *italic formatting* and text with `code formatting` and text with ![image formatting](https://i.imgur.com/8HJoyoy.jpeg) and text with [link formatting](https://github.com/SamW94).", children=None, props=None)], props=None)
        self.assertEqual(html_node, expected_output)

    def test_multiple_different_blocks(self):
        markdown = "# This is a heading\n\n```This is a code block```\n\n"
        html_node = markdown_to_html_node(markdown)
        expected_output = HTMLNode(tag="div", value=None, children=[HTMLNode(tag="h1", value="This is a heading", children=None, props=None), HTMLNode(tag="pre", value=None, children=[HTMLNode(tag="code", value="This is a code block", children=None, props=None)], props=None)], props=None)
        self.assertEqual(html_node, expected_output)

    def test_multiple_blocks_with_formatting_inline(self):
        markdown = "# This is a heading with 1 # symbol\n\n```This is a code block```\n\n>This is a quote block.\n>This is another quote.\n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item\n\n1. This is an *ordered* list.\n2. This is the **second** item in the list.\n\nThis is another paragaph of text that contains **bold formatting,** and *italic formatting* and text with `code formatting` and text with ![image formatting](https://i.imgur.com/8HJoyoy.jpeg) and text with [link formatting](https://github.com/SamW94)."
        html_node = markdown_to_html_node(markdown)
        expected_output = HTMLNode(tag="div", value=None, children=[HTMLNode(tag="h1", value="This is a heading with 1 # symbol", children=None, props=None), HTMLNode(tag="pre", value=None, children=[HTMLNode(tag="code", value="This is a code block", children=None, props=None)], props=None), HTMLNode(tag="blockquote", value="This is a quote block.\nThis is another quote.", children=None, props=None), HTMLNode(tag="ul", value=None, children=[HTMLNode(tag="li", value="This is the first list item in a list block", children=None, props=None), HTMLNode(tag="li", value="This is a list item", children=None, props=None), HTMLNode(tag="li", value="This is another list item", children=None, props=None)], props=None), HTMLNode(tag="ol", value=None, children=[HTMLNode(tag="li", value="This is an *ordered* list.", children=None, props=None), HTMLNode(tag="li", value="This is the **second** item in the list.", children=None, props=None)], props=None), HTMLNode(tag="p", value="This is another paragaph of text that contains **bold formatting,** and *italic formatting* and text with `code formatting` and text with ![image formatting](https://i.imgur.com/8HJoyoy.jpeg) and text with [link formatting](https://github.com/SamW94).", children=None, props=None)], props=None)
        self.assertEqual(html_node, expected_output)

if __name__ == "__main__":
    unittest.main()
