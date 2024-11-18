import re

def extract_markdown_images(text):
    alt_text_and_url_tuples = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    if alt_text_and_url_tuples:
        return alt_text_and_url_tuples
    else: 
        return "There is no text formatted as a markdown image."

def extract_markdown_links(text):
    alt_text_and_url_tuples = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    if alt_text_and_url_tuples:
        return alt_text_and_url_tuples
    else:
        return "There is no text formatted as a markdown link."
