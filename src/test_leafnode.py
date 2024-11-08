import unittest

from leafnode import LeafNode

class TetLeafNode(unittest.TestCase):

    def test_nones(self):
        node = LeafNode(tag="p", value="This is a paragraph of text.")
        self.assertIsNone(node.children)
        self.assertIsNone(node.props)

    def test_to_html_no_props(self):
        node = LeafNode(tag="p", value="This is a paragraph of text.")
        self.assertIsNone(node.children)
        self.assertIsNone(node.props)
        self.assertEqual(node.to_html(), "<p>This is a paragraph of text.</p>")

    def test_to_html_with_props(self):
        node = LeafNode(tag="a", value="Click me!", props={"href": "https://www.google.com"})
        self.assertIsNone(node.children)
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_value_error(self):
        with self.assertRaises(ValueError):
            LeafNode(tag="p", value=None)

    def test_raw_text(self):
        node = LeafNode(tag=None, value="Just some text.")
        self.assertEqual(node.to_html(), "Just some text.")


if __name__ == "__main__":
    unittest.main()