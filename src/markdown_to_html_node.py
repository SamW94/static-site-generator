import re
from markdown_to_blocks import markdown_to_blocks
from block_to_block_type import block_to_block_type
from parentnode import ParentNode
from leafnode import LeafNode

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    child_nodes = []
    for block in blocks:
        block_type = block_to_block_type(block)
        
        if block_type == "heading":
            hash_count = block[0:6].count("#")
            leaf_node = LeafNode(value=block[hash_count::].strip(), tag=f"h{hash_count}")
            child_nodes.append(leaf_node)

        if block_type == "code":
            parent_node = ParentNode(tag="pre", children=[LeafNode(value=block.replace("```", "").strip(), tag="code")])
            child_nodes.append(parent_node)

        if block_type == "quote":
            regex = r'(^|\n)>(?=\S)'
            symbols_removed = re.sub(regex, r'\1', block)
            leaf_node = LeafNode(value=symbols_removed.strip(), tag="blockquote")
            child_nodes.append(leaf_node)

        if block_type == "unordered_list":
            list_items = block.split("\n")
            ul_children = []
            for list_item in list_items:
                ul_children.append(LeafNode(value=list_item[1::].strip(), tag="li"))
            parent_node = ParentNode(tag="ul", children=ul_children)
            child_nodes.append(parent_node)


        if block_type == "ordered_list":
            list_items = block.split("\n")
            ol_children = []
            for list_item in list_items:
                ol_children.append(LeafNode(value=list_item[2::].strip(), tag="li"))
            parent_node = ParentNode(tag="ol", children=ol_children)
            child_nodes.append(parent_node)

        if block_type == "paragraph":
            leaf_node = LeafNode(value=block, tag="p")
            child_nodes.append(leaf_node)
    
    return ParentNode(tag="div", children=child_nodes)
