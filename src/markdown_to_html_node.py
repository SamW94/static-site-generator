import re
from markdown_to_blocks import markdown_to_blocks
from block_to_block_type import block_to_block_type
from parentnode import ParentNode
from leafnode import LeafNode
from text_to_textnodes import text_to_textnodes
from text_node_to_html import text_node_to_html

def text_to_children(block):
    textnodes_list = text_to_textnodes(block)
    leaf_nodes = []
    for textnode in textnodes_list:
        leaf_nodes.append(text_node_to_html(textnode))
    return leaf_nodes


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    child_nodes = []
    for block in blocks:
        block_type = block_to_block_type(block)
        
        if block_type == "heading":
            hash_count = block[0:6].count("#")
            block = block[hash_count::].strip()
            children = text_to_children(block)
            parent_node = ParentNode(tag=f"h{hash_count}", children=children)
            child_nodes.append(parent_node)

        if block_type == "code":
            parent_node = ParentNode(tag="pre", children=[LeafNode(value=block.replace("```", "").strip(), tag="code")])
            child_nodes.append(parent_node)

        if block_type == "quote":
            regex = r'^\s*>\s?(.*)$'
            symbols_removed_block = re.sub(regex, r'\1', block, flags=re.MULTILINE)
            children = text_to_children(symbols_removed_block)
            parent_node = ParentNode(tag=f"blockquote", children=children)
            child_nodes.append(parent_node)

        if block_type == "unordered_list":
            list_items = block.split("\n")
            ul_children = []
            for list_item in list_items:
                regex = r'^[\*\- ]'
                cleaned_item = re.sub(regex, "", list_item, count=1).strip()
                item_children = text_to_children(cleaned_item)
                li_node = ParentNode(tag="li", children=item_children)
                ul_children.append(li_node)
            parent_node = ParentNode(tag="ul", children=ul_children)
            child_nodes.append(parent_node)

        if block_type == "ordered_list":
            list_items = block.split("\n")
            ol_children = []
            for list_item in list_items:
                cleaned_item = list_item.lstrip("0123456789. ").strip()
                item_children = text_to_children(cleaned_item)
                li_node = ParentNode(tag="li", children=item_children)
                ol_children.append(li_node)
            parent_node = ParentNode(tag="ol", children=ol_children)
            child_nodes.append(parent_node)

        if block_type == "paragraph":
            children = text_to_children(block)
            parent_node = ParentNode(tag="p", children=children)
            child_nodes.append(parent_node)
    
    return ParentNode(tag="div", children=child_nodes)
