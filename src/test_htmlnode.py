import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):

    def test_tag_and_value_only(self):
        node = HTMLNode(tag="p", value="This is sample text that should be inside a paragraph tag.")
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, "This is sample text that should be inside a paragraph tag.")
        self.assertIsNone(node.children)
        self.assertIsNone(node.props)

    def test_props_to_html_no_props(self):
        node = HTMLNode()
        self.assertIsNone(node.tag)
        self.assertIsNone(node.value)
        self.assertIsNone(node.children)
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html_single(self):
        node = HTMLNode(props={"class": "bold"})
        self.assertIsNone(node.tag)
        self.assertIsNone(node.value)
        self.assertIsNone(node.children)
        self.assertEqual(node.props_to_html(), ' class="bold"')

    def test_props_to_html_multiple_props(self):
        node = HTMLNode(props={"href": "https://google.com", "target": "_blank"})
        self.assertIsNone(node.tag)
        self.assertIsNone(node.value)
        self.assertIsNone(node.children)
        self.assertEqual(node.props_to_html(), ' href="https://google.com" target="_blank"')

    def test_node_with_children(self):
        child1 = HTMLNode(tag="p", value="Child 1")
        child2 = HTMLNode(tag="p", value="Child 2")
        parent = HTMLNode(tag="div", children=[child1, child2])
        # Test parent properties
        self.assertEqual(parent.tag, "div")
        self.assertEqual(len(parent.children), 2)
        self.assertIsNone(parent.props)
        self.assertIsNone(parent.value)
    
        # Test children properties
        self.assertEqual(parent.children[0].tag, "p")
        self.assertEqual(parent.children[0].value, "Child 1")
        self.assertEqual(parent.children[1].tag, "p")
        self.assertEqual(parent.children[1].value, "Child 2")


    def test_complete_node(self):
        child_node1 = HTMLNode(tag="p", value="This is sample text that should be inside a paragraph tag.")
        child_node2 = HTMLNode(tag="p", value="This is also sample text that should be inside a paragraph tag.") 
        parent_node = HTMLNode(
            tag="p", 
            value="This is a parent node with children.", 
            children=[child_node1, child_node2], 
            props={"class": "bold"}
        )

        # Test parent node properties
        self.assertEqual(parent_node.tag, "p")
        self.assertEqual(parent_node.value, "This is a parent node with children.")
        self.assertEqual(len(parent_node.children), 2)
        self.assertEqual(parent_node.props, {"class": "bold"})
        self.assertEqual(parent_node.props_to_html(), ' class="bold"')

        # Test children properties
        self.assertEqual(parent_node.children[0].tag, "p")
        self.assertEqual(parent_node.children[0].value, "This is sample text that should be inside a paragraph tag.")
        self.assertEqual(parent_node.children[1].tag, "p")
        self.assertEqual(parent_node.children[1].value, "This is also sample text that should be inside a paragraph tag.")

    def test_props_edge_cases(self):
        node = HTMLNode(props={
            "empty": "",
            "special@char": "value!@#$",
            "number": 42,
    })
        
        # Test object key-value pairs in self.props
        self.assertEqual(node.props["empty"], "")
        self.assertEqual(node.props["special@char"], "value!@#$")
        self.assertEqual(node.props["number"], 42)

        # Test props_to_html function
        self.assertEqual(node.props_to_html(), ' empty="" special@char="value!@#$" number="42"')

        # Additional assertions for default values
        self.assertIsNone(node.tag)
        self.assertIsNone(node.value)
        self.assertIsNone(node.children)

if __name__ == "__main__":
    unittest.main()