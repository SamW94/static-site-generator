from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            split_node = (node.text).split(delimiter)
            
            if len(split_node) % 2 == 0:
                raise Exception("Unbalanced delimiters in text")
            
            for index, segment in enumerate(split_node):
                if index % 2 == 0:
                    new_nodes.append(TextNode(segment, TextType.TEXT))
                else:
                    new_nodes.append(TextNode(segment, text_type))
    return new_nodes
