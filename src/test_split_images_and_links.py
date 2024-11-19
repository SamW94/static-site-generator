from split_images_and_links import split_nodes_image, split_nodes_link
from textnode import TextNode, TextType
import unittest

class TextSplitImagesAndLinks(unittest.TestCase):

    def test_no_markdown_links(self):
        node = TextNode("This text has no links or images in it.", TextType.TEXT)
        new_nodes_list = split_nodes_link([node])
        expected_output = [TextNode("This text has no links or images in it.", TextType.TEXT)]
        self.assertEqual(new_nodes_list, expected_output)

    def test_no_markdown_images(self):
        node = TextNode("This text has no links or images in it.", TextType.TEXT)
        new_nodes_list = split_nodes_image([node])
        expected_output = [TextNode("This text has no links or images in it.", TextType.TEXT)]
        self.assertEqual(new_nodes_list, expected_output)

    def test_empty_string_links(self):
        node = TextNode("", TextType.TEXT)
        new_nodes_list = split_nodes_link([node])
        expected_output = [TextNode("", TextType.TEXT)]
        self.assertEqual(new_nodes_list, expected_output)

    def test_empty_string_images(self):
        node = TextNode("", TextType.TEXT)
        new_nodes_list = split_nodes_image([node])
        expected_output = [TextNode("", TextType.TEXT)]
        self.assertEqual(new_nodes_list, expected_output)

    def test_markdown_links_single(self):
        node = TextNode("This is text with a link [to boot dev](https://boot.dev)", TextType.TEXT)
        new_nodes_list = split_nodes_link([node])
        expected_output = [TextNode("This is text with a link ", TextType.TEXT), TextNode("to boot dev", TextType.LINK, "https://boot.dev")]
        self.assertEqual(new_nodes_list, expected_output)

    def test_markdown_images_single(self):
        node = TextNode("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif)", TextType.TEXT)
        new_nodes_list = split_nodes_image([node])
        expected_output = [TextNode("This is text with a ", TextType.TEXT), TextNode("rick roll", TextType.IMAGE, "https://i.imgur.com/aKaOqIh.gif")]
        self.assertEqual(new_nodes_list, expected_output)

    def test_markdown_links_multiple(self):
        node = TextNode("This is text with a link [to boot dev](https://boot.dev) and [to YouTube](https://www.youtube.com/@bootdotdev)", TextType.TEXT)
        new_nodes_list = split_nodes_link([node])
        expected_output = [TextNode("This is text with a link ", TextType.TEXT), TextNode("to boot dev", TextType.LINK, "https://boot.dev"), TextNode(" and ", TextType.TEXT), TextNode("to YouTube", TextType.LINK, "https://www.youtube.com/@bootdotdev")]
        self.assertEqual(new_nodes_list, expected_output)

    def test_markdown_images_multiple(self):
        node = TextNode("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)", TextType.TEXT)
        new_nodes_list = split_nodes_image([node])
        expected_output = [TextNode("This is text with a ", TextType.TEXT), TextNode("rick roll", TextType.IMAGE, "https://i.imgur.com/aKaOqIh.gif"), TextNode(" and ", TextType.TEXT), TextNode("obi wan", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg")]
        self.assertEqual(new_nodes_list, expected_output)

    def test_markdown_links_multiple_adjacent(self):
        node = TextNode("Here are two links adjacent to one another: [link1](https://url1.test)[link2](https://url2.test)", TextType.TEXT)
        new_nodes_list = split_nodes_link([node])
        expected_output = [TextNode("Here are two links adjacent to one another: ", TextType.TEXT), TextNode("link1", TextType.LINK, "https://url1.test"), TextNode("link2", TextType.LINK, "https://url2.test")]
        self.assertEqual(new_nodes_list, expected_output)

    def test_markdown_images_multiple_adjacent(self):
        node = TextNode("Here are two images adjacent to one another: ![image1](https://image1.test)![image2](https://image2.test)", TextType.TEXT)
        new_nodes_list = split_nodes_image([node])
        expected_output = [TextNode("Here are two images adjacent to one another: ", TextType.TEXT), TextNode("image1", TextType.IMAGE, "https://image1.test"), TextNode("image2", TextType.IMAGE, "https://image2.test")]
        self.assertEqual(new_nodes_list, expected_output)

if __name__ == "__main__":
    unittest.main()