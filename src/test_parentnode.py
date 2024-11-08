import unittest

from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):

    def test_no_tag(self):
        child1 = LeafNode(tag="p", value="Child 1.")
        child2 = LeafNode(tag="p", value="Child 2.")
        with self.assertRaises(TypeError):
            ParentNode(children=[child1, child2])
    
    def test_none_tag(self):
        child1 = LeafNode(tag="p", value="Child 1.")
        child2 = LeafNode(tag="p", value="Child 2.")
        with self.assertRaisesRegex(ValueError, "A parent node must have tags."):
            ParentNode(tag=None, children=[child1, child2]).to_html()

    def test_no_children(self):
        with self.assertRaises(TypeError):
            ParentNode(tag="p")

    def test_none_children(self):
        with self.assertRaisesRegex(ValueError, "A parent node must have children."):
            ParentNode(tag="p", children=None).to_html()

    def test_empty_children(self):
        with self.assertRaisesRegex(ValueError, "A parent node must have children."):
            ParentNode(tag="p", children=[]).to_html()

    def test_value_none(self):
        child1 = LeafNode(tag="p", value="Child 1.")
        child2 = LeafNode(tag="b", value="Child 2.")
        parent = ParentNode(tag="class", children=[child1, child2])

    def test_parent_node_with_children(self):
        child1 = LeafNode(tag="p", value="Child 1.")
        child2 = LeafNode(tag="b", value="Child 2.")
        parent = ParentNode(tag="class", children=[child1, child2])
        # Test parent properties
        self.assertEqual(parent.tag, "class")
        self.assertEqual(len(parent.children), 2)
        self.assertIsNone(parent.props)
        self.assertIsNone(parent.value)
        # Test child properties
        self.assertEqual(parent.children[0].tag, "p")
        self.assertEqual(parent.children[0].value, "Child 1.")
        self.assertEqual(parent.children[1].tag, "b")
        self.assertEqual(parent.children[1].value, "Child 2.")
        # Test to_html output
        self.assertEqual(parent.to_html(), "<class><p>Child 1.</p><b>Child 2.</b></class>")
        
    def test_parent_props(self):
        child1 = LeafNode(tag="p", value="Child 1.")
        child2 = LeafNode(tag="b", value="Child 2.")
        parent = ParentNode(tag="class", children=[child1, child2], props={"href": "https://google.com", "target": "_blank"})
        # Test parent properties
        self.assertEqual(parent.tag, "class")
        self.assertEqual(len(parent.children), 2)
        self.assertIsNone(parent.value)
        self.assertEqual(parent.props, {"href": "https://google.com", "target": "_blank"})
        # Test child properties
        self.assertEqual(parent.children[0].tag, "p")
        self.assertEqual(parent.children[0].value, "Child 1.")
        self.assertEqual(parent.children[1].tag, "b")
        self.assertEqual(parent.children[1].value, "Child 2.")
        # Test parent props
        self.assertEqual(parent.props_to_html(), ' href="https://google.com" target="_blank"')
        # Test to_html output
        self.assertEqual(parent.to_html(), '<class href="https://google.com" target="_blank"><p>Child 1.</p><b>Child 2.</b></class>')

    def test_child_props(self):
        child1 = LeafNode(tag="p", value="Child 1.", props={"href": "https://google.com"})
        child2 = LeafNode(tag="b", value="Child 2.", props={"target": "_blank"})
        parent = ParentNode(tag="class", children=[child1, child2])
        # Test parent properties
        self.assertEqual(parent.tag, "class")
        self.assertEqual(len(parent.children), 2)
        self.assertIsNone(parent.props)
        self.assertIsNone(parent.value)
        # Test child properties
        self.assertEqual(parent.children[0].tag, "p")
        self.assertEqual(parent.children[0].value, "Child 1.")
        self.assertEqual(parent.children[0].props, {"href": "https://google.com"})
        self.assertIsNone(parent.children[0].children)
        self.assertEqual(parent.children[1].tag, "b")
        self.assertEqual(parent.children[1].value, "Child 2.")
        self.assertEqual(parent.children[1].props, {"target": "_blank"})
        self.assertIsNone(parent.children[1].children)
        # Test child props
        self.assertEqual(parent.children[0].props_to_html(), ' href="https://google.com"')
        self.assertEqual(parent.children[1].props_to_html(), ' target="_blank"')
        # Test to_html output
        self.assertEqual(parent.to_html(), '<class><p href="https://google.com">Child 1.</p><b target="_blank">Child 2.</b></class>')

    def test_child_and_parent_props(self):
        child1 = LeafNode(tag="p", value="Child 1.", props={"target": "_blank"})
        child2 = LeafNode(tag="b", value="Child 2.")
        parent = ParentNode(tag="class", children=[child1, child2], props={"href": "https://google.com"}) 
        # Test parent properties
        self.assertEqual(parent.tag, "class")
        self.assertEqual(len(parent.children), 2)
        self.assertIsNone(parent.value)
        self.assertEqual(parent.props, {"href": "https://google.com"})
        # Test child properties
        self.assertEqual(parent.children[0].tag, "p")
        self.assertEqual(parent.children[0].value, "Child 1.")
        self.assertEqual(parent.children[0].props, {"target": "_blank"})
        self.assertIsNone(parent.children[0].children)
        self.assertEqual(parent.children[1].tag, "b")
        self.assertEqual(parent.children[1].value, "Child 2.")
        self.assertIsNone(parent.children[1].props)
        self.assertIsNone(parent.children[1].children)
        # Test parent props
        self.assertEqual(parent.props_to_html(), ' href="https://google.com"')
        # Test child props
        self.assertEqual(parent.children[0].props_to_html(), ' target="_blank"')
        # Test to_html output
        self.assertEqual(parent.to_html(), '<class href="https://google.com"><p target="_blank">Child 1.</p><b>Child 2.</b></class>')

    def test_nested_parent_node(self):
        inner_children = [LeafNode(tag="b", value="Bold text")]
        inner_parent = ParentNode("div", inner_children)
        outer_children = [inner_parent, LeafNode(tag="i", value="Italic")]
        outer_parent = ParentNode("p", outer_children)
        # Test to_html output
        self.assertEqual(outer_parent.to_html(), '<p><div><b>Bold text</b></div><i>Italic</i></p>')

if __name__ == "__main__":
    unittest.main()