import unittest

from markdown_to_html_node import markdown_to_html_node
from htmlnode import HTMLNode
from parentnode import ParentNode

def debug_compare(node1, node2, path="root"):
    if node1.tag != node2.tag:
        print(f"Tag mismatch at {path}: {node1.tag} != {node2.tag}")
    if node1.value != node2.value:
        print(f"Value mismatch at {path}: {node1.value} != {node2.value}")
    if node1.props != node2.props:
        print(f"Props mismatch at {path}: {node1.props} != {node2.props}")
    if node1.children != node2.children:
        print(f"Children mismatch at {path}")
        if node1.children and node2.children:
            for i, (c1, c2) in enumerate(zip(node1.children, node2.children)):
                debug_compare(c1, c2, f"{path}[{i}]")

class TestMarkdownToHTMLNode(unittest.TestCase):

    def test_header_block_one_hash(self):
        markdown = "# This is a heading.\n\n"
        html_node = markdown_to_html_node(markdown)
        expected_output = HTMLNode(tag="div", value=None, children=[HTMLNode(tag="h1", value=None, children=[HTMLNode(tag=None, value="This is a heading.", children=None, props=None)], props=None)], props=None)
        self.assertEqual(html_node, expected_output)

    def test_header_block_multiple_hashes(self):
        markdown = "### This is a heading.\n\n"
        html_node = markdown_to_html_node(markdown)
        expected_output = HTMLNode(tag="div", value=None, children=[HTMLNode(tag="h3", value=None, children=[HTMLNode(tag=None, value="This is a heading.", children=None, props=None)], props=None)], props=None)
        self.assertEqual(html_node, expected_output)

    def test_header_inline_formatting(self):
        markdown = "# This is a heading with **bold formatting** inline.\n\n"
        html_node = markdown_to_html_node(markdown)
        expected_output = HTMLNode(tag="div", value=None, children=[HTMLNode(tag="h1", value=None, children=[HTMLNode(tag=None, value="This is a heading with ", children=None, props=None), HTMLNode(tag="b", value="bold formatting", children=None, props=None), HTMLNode(tag=None, value=" inline.", children=None, props=None)], props=None)], props=None)
        self.assertEqual(html_node, expected_output)
   
    def test_code_block(self):
        markdown = "```This is a code block```\n\n"
        html_node = markdown_to_html_node(markdown)
        expected_output = HTMLNode(tag="div", value=None, children=[HTMLNode(tag="pre", value=None, children=[HTMLNode(tag="code", value="This is a code block", children=None, props=None)], props=None)], props=None)
        self.assertEqual(html_node, expected_output)

    def test_code_block_with_inline_formatting_to_ignore(self):
        markdown = "```This is a code block with **inline** *formatting* that should be ![ignored].```\n\n"
        html_node = markdown_to_html_node(markdown)
        expected_output = HTMLNode(tag="div", value=None, children=[HTMLNode(tag="pre", value=None, children=[HTMLNode(tag="code", value="This is a code block with **inline** *formatting* that should be ![ignored].", children=None, props=None)], props=None)], props=None)
        self.assertEqual(html_node, expected_output)

    def test_quote_block(self):
        markdown = ">This is a quote block.\n>This is another quote.\n\n"
        html_node = markdown_to_html_node(markdown)
        expected_output = HTMLNode(tag="div", value=None, children=[HTMLNode(tag="blockquote", value=None, children=[HTMLNode(tag=None, value="This is a quote block.\nThis is another quote.", children=None, props=None)], props=None)], props=None)
        self.assertEqual(html_node, expected_output)

    def test_quote_block_inline_formatting(self):
        markdown = ">This is a quote block.\n>This is another **really important** quote.\n\n"
        html_node = markdown_to_html_node(markdown)
        expected_output = HTMLNode(tag="div", value=None, children=[HTMLNode(tag="blockquote", value=None, children=[HTMLNode(tag=None, value="This is a quote block.\nThis is another ", children=None, props=None), HTMLNode(tag="b", value="really important", children=None, props=None), HTMLNode(tag=None, value=" quote.", children=None, props=None)], props=None)], props=None)
        self.assertEqual(html_node, expected_output)

    def test_unordered_list_block(self):
        markdown = "* This is the first list item in a list block\n* This is a list item\n* This is another list item\n\n"
        html_node = markdown_to_html_node(markdown)
        expected_output = HTMLNode(tag="div", value=None, children=[HTMLNode(tag="ul", value=None, children=[HTMLNode(tag="li", value=None, children=[HTMLNode(tag=None, value="This is the first list item in a list block", children=None, props=None)], props=None), HTMLNode(tag="li", value=None, children=[HTMLNode(tag=None, value="This is a list item", children=None, props=None)], props=None), HTMLNode(tag="li", value=None, children=[HTMLNode(tag=None, value="This is another list item", children=None, props=None)], props=None)], props=None)], props=None)
        self.assertEqual(html_node, expected_output)

    def test_unordered_list_block_inline_formatting(self):
        markdown = "* This is the first list item in a list block\n* This is a list item with *italics* inline\n* This is another list item\n\n"
        html_node = markdown_to_html_node(markdown)
        expected_output = HTMLNode(tag="div", value=None, children=[HTMLNode(tag="ul", value=None, children=[HTMLNode(tag="li", value=None, children=[HTMLNode(tag=None, value="This is the first list item in a list block", children=None, props=None)], props=None), HTMLNode(tag="li", value=None, children=[HTMLNode(tag=None, value="This is a list item with ", children=None, props=None), HTMLNode(tag="i", value="italics", children=None, props=None), HTMLNode(tag=None, value=" inline", children=None, props=None)], props=None), HTMLNode(tag="li", value=None, children=[HTMLNode(tag=None, value="This is another list item", children=None, props=None)], props=None)], props=None)], props=None)
        self.assertEqual(html_node, expected_output)

    def test_ordered_list_block(self):
        markdown = "1. This is an ordered list.\n2. This is the second item in the list.\n\n"
        html_node = markdown_to_html_node(markdown)
        expected_output = HTMLNode(tag="div", value=None, children=[HTMLNode(tag="ol", value=None, children=[HTMLNode(tag="li", value=None, children=[HTMLNode(tag=None, value="This is an ordered list.", children=None, props=None)], props=None), HTMLNode(tag="li", value=None, children=[HTMLNode(tag=None, value="This is the second item in the list.", children=None, props=None)], props=None)], props=None)], props=None)
        self.assertEqual(html_node, expected_output)

    def test_ordered_list_block_inline_formatting(self):
        markdown = "1. This is an ordered list.\n2. This is the second item in the list.\n3. This [contains a link](https://some.link) and is the third item in the list.\n\n"
        html_node = markdown_to_html_node(markdown)
        expected_output = HTMLNode(tag="div", value=None, children=[HTMLNode(tag="ol", value=None, children=[HTMLNode(tag="li", value=None, children=[HTMLNode(tag=None, value="This is an ordered list.", children=None, props=None)], props=None), HTMLNode(tag="li", value=None, children=[HTMLNode(tag=None, value="This is the second item in the list.", children=None, props=None)], props=None), HTMLNode(tag="li", value=None, children=[HTMLNode(tag=None, value="This ", children=None, props=None), HTMLNode(tag="a", value="contains a link", children=None, props={'href': 'https://some.link'}), HTMLNode(tag=None, value=" and is the third item in the list.", children=None, props=None)], props=None)], props=None)], props=None)
        self.assertEqual(html_node, expected_output)

    def test_paragraph_block(self):
        markdown = "This is another paragaph of text that contains **bold formatting,** and *italic formatting* and text with `code formatting` and text with ![image formatting](https://i.imgur.com/8HJoyoy.jpeg) and text with [link formatting](https://github.com/SamW94)."
        html_node = markdown_to_html_node(markdown)
        expected_output = HTMLNode(tag="div", value=None, children=[HTMLNode(tag="p", value=None, children=[HTMLNode(tag=None, value="This is another paragaph of text that contains ", children=None, props=None), HTMLNode(tag="b", value="bold formatting,", children=None, props=None), HTMLNode(tag=None, value=" and ", children=None, props=None), HTMLNode(tag="i", value="italic formatting", children=None, props=None), HTMLNode(tag=None, value=" and text with ", children=None, props=None), HTMLNode(tag="code", value="code formatting", children=None, props=None), HTMLNode(tag=None, value=" and text with ", children=None, props=None), HTMLNode(tag="img", value="", children=None, props={'src': 'https://i.imgur.com/8HJoyoy.jpeg', 'alt': 'image formatting'}), HTMLNode(tag=None, value=" and text with ", children=None, props=None), HTMLNode(tag="a", value="link formatting", children=None, props={'href': 'https://github.com/SamW94'}), HTMLNode(tag=None, value=".", children=None, props=None)], props=None)], props=None)
        self.assertEqual(html_node, expected_output)

    def test_multiple_different_blocks(self):
        markdown = "# This is a heading\n\n```This is a code block```\n\n"
        html_node = markdown_to_html_node(markdown)
        expected_output = HTMLNode(tag="div", value=None, children=[HTMLNode(tag="h1", value=None, children=[HTMLNode(tag=None, value="This is a heading", children=None, props=None)], props=None), HTMLNode(tag="pre", value=None, children=[HTMLNode(tag="code", value="This is a code block", children=None, props=None)], props=None)], props=None)
        self.assertEqual(html_node, expected_output)

    def test_multiple_blocks_with_formatting_inline(self):
        markdown = "# This is a heading with 1 # symbol\n\n```This is a code block```\n\n>This is a quote block.\n>This is another quote.\n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item\n\n1. This is an *ordered* list.\n2. This is the **second** item in the list.\n\nThis is another paragaph of text that contains **bold formatting,** and *italic formatting* and text with `code formatting` and text with ![image formatting](https://i.imgur.com/8HJoyoy.jpeg) and text with [link formatting](https://github.com/SamW94)."
        html_node = markdown_to_html_node(markdown)
        expected_output = HTMLNode(tag="div", value=None, children=[HTMLNode(tag="h1", value=None, children=[HTMLNode(tag=None, value="This is a heading with 1 # symbol", children=None, props=None)], props=None), HTMLNode(tag="pre", value=None, children=[HTMLNode(tag="code", value="This is a code block", children=None, props=None)], props=None), HTMLNode(tag="blockquote", value=None, children=[HTMLNode(tag=None, value="This is a quote block.\nThis is another quote.", children=None, props=None)], props=None), HTMLNode(tag="ul", value=None, children=[HTMLNode(tag="li", value=None, children=[HTMLNode(tag=None, value="This is the first list item in a list block", children=None, props=None)], props=None), HTMLNode(tag="li", value=None, children=[HTMLNode(tag=None, value="This is a list item", children=None, props=None)], props=None), HTMLNode(tag="li", value=None, children=[HTMLNode(tag=None, value="This is another list item", children=None, props=None)], props=None)], props=None), HTMLNode(tag="ol", value=None, children=[HTMLNode(tag="li", value=None, children=[HTMLNode(tag=None, value="This is an ", children=None, props=None), HTMLNode(tag="i", value="ordered", children=None, props=None), HTMLNode(tag=None, value=" list.", children=None, props=None)], props=None), HTMLNode(tag="li", value=None, children=[HTMLNode(tag=None, value="This is the ", children=None, props=None), HTMLNode(tag="b", value="second", children=None, props=None), HTMLNode(tag=None, value=" item in the list.", children=None, props=None)], props=None)], props=None), HTMLNode(tag="p", value=None, children=[HTMLNode(tag=None, value="This is another paragaph of text that contains ", children=None, props=None), HTMLNode(tag="b", value="bold formatting,", children=None, props=None), HTMLNode(tag=None, value=" and ", children=None, props=None), HTMLNode(tag="i", value="italic formatting", children=None, props=None), HTMLNode(tag=None, value=" and text with ", children=None, props=None), HTMLNode(tag="code", value="code formatting", children=None, props=None), HTMLNode(tag=None, value=" and text with ", children=None, props=None), HTMLNode(tag="img", value="", children=None, props={'src': 'https://i.imgur.com/8HJoyoy.jpeg', 'alt': 'image formatting'}), HTMLNode(tag=None, value=" and text with ", children=None, props=None), HTMLNode(tag="a", value="link formatting", children=None, props={'href': 'https://github.com/SamW94'}), HTMLNode(tag=None, value=".", children=None, props=None)], props=None)], props=None)
        self.assertEqual(html_node, expected_output)

if __name__ == "__main__":
    unittest.main()
