from textnode import TextNode, TextType
import re

def get_delimiter_regex(delimiter):
    if delimiter == "**":
        return r'\*\*'
    elif delimiter == "*":
        return r'(?<!\*)\*(?!\*)'
    else: 
        return re.escape(delimiter)

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        delimiter_pattern = get_delimiter_regex(delimiter)
        delimiter_count = len(re.findall(delimiter_pattern, node.text))
        if node.text_type != TextType.TEXT or delimiter_count % 2 != 0:
            new_nodes.append(node)
        else:
            split_node = re.split(delimiter_pattern, node.text)
            for index, segment in enumerate(split_node):
                if index % 2 == 0:
                    new_nodes.append(TextNode(segment, TextType.TEXT))
                else:
                    new_nodes.append(TextNode(segment, text_type))
    return new_nodes
