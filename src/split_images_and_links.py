from textnode import TextNode, TextType
from extract_markdown_regex import extract_markdown_images, extract_markdown_links

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            original_text = node.text
            alt_text_and_url_tuples_list = extract_markdown_links(node.text)
            if alt_text_and_url_tuples_list == "There is no text formatted as a markdown link.":
                new_nodes.append(node)
            else:
                start_index = 0 
                i = 0
                while i < len(alt_text_and_url_tuples_list):
                    alt_text = alt_text_and_url_tuples_list[i][0]
                    link_url = alt_text_and_url_tuples_list[i][1]
                    first_occurence = original_text.find(f"[{alt_text}]({link_url})", start_index)
                    i += 1
                    text_segment = original_text[start_index:first_occurence]
                    if len(text_segment) > 0:
                        new_nodes.append(TextNode(text_segment, TextType.TEXT))
                    new_nodes.append(TextNode(alt_text, TextType.LINK, link_url))
                    start_index = first_occurence + len(f"[{alt_text}]({link_url})")
                if start_index < len(original_text):
                    text_segment = original_text[start_index:]
                    if len(text_segment) > 0:
                        new_nodes.append(TextNode(text_segment, TextType.TEXT))
        else: 
            new_nodes.append(node)
    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            original_text = node.text
            alt_text_and_url_tuples_list = extract_markdown_images(node.text)
            if alt_text_and_url_tuples_list == "There is no text formatted as a markdown image.":
                new_nodes.append(node)
            else:
                start_index = 0 
                i = 0
                while i < len(alt_text_and_url_tuples_list):
                    alt_text = alt_text_and_url_tuples_list[i][0]
                    image_url = alt_text_and_url_tuples_list[i][1]
                    first_occurence = original_text.find(f"![{alt_text}]({image_url})", start_index)
                    i += 1
                    text_segment = original_text[start_index:first_occurence]
                    if len(text_segment) > 0:
                        new_nodes.append(TextNode(text_segment, TextType.TEXT))
                    new_nodes.append(TextNode("", TextType.IMAGE, image_url, alt_text))
                    start_index = first_occurence + len(f"![{alt_text}]({image_url})")
                if start_index < len(original_text):
                    text_segment = original_text[start_index:]
                    if len(text_segment) > 0:
                        new_nodes.append(TextNode(text_segment, TextType.TEXT))
        else: 
            new_nodes.append(node)
    return new_nodes
