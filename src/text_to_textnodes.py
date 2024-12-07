from textnode import TextNode, TextType
from split_nodes_delimiter import split_nodes_delimiter
from split_images_and_links import split_nodes_image, split_nodes_link

def text_to_textnodes(text):
    text_nodes = [TextNode(text, TextType.TEXT)]
    split_node = split_nodes_delimiter(text_nodes, "**", TextType.BOLD)
    split_node = split_nodes_delimiter(split_node, "*", TextType.ITALIC)
    split_node = split_nodes_delimiter(split_node, "`", TextType.CODE)
    split_node = split_nodes_image(split_node)
    final_nodes = split_nodes_link(split_node)
    return final_nodes
