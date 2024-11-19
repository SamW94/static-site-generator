from textnode import TextNode, TextType
from leafnode import LeafNode
from split_images_and_links import split_nodes_image, split_nodes_link
from split_nodes_delimiter import split_nodes_delimiter

def text_node_to_html(text_node):
    if text_node.text_type == TextType.TEXT:
        return LeafNode(tag=None, value=text_node.text)
    if text_node.text_type == TextType.BOLD: 
        return LeafNode(tag="b", value=text_node.text)
    if text_node.text_type == TextType.ITALIC:
        return LeafNode(tag="i", value=text_node.text)
    if text_node.text_type == TextType.CODE:
        return LeafNode(tag="code", value=text_node.text)
    if text_node.text_type == TextType.LINK:
        return LeafNode(tag="a", value=text_node.text, props={"href": text_node.url})
    if text_node.text_type == TextType.IMAGE:
        return LeafNode(tag="img", value="", props={"src": text_node.url, "alt": text_node.alt_text})
    else:
        raise AttributeError

def text_to_textnodes(text):
    pass

def main():
    text_node_to_html()
    text_to_textnodes()

if __name__ == "__main__":
    main()
