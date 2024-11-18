from textnode import TextNode, TextType

# old_nodes is a list of "nodes", i.e. TextNodes
# delimiter is the symbal that will be used to (potentially) split each node into multiple nodes
# text_type 
# the function below should return a new list
# example
# node = TextNode("This is text with a `code block` word", TextType.TEXT)
# new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

# start with an empty 'new_nodes' list
# return 'new_nodes' at the end of the function

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
