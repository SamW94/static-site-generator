import os
from generate_page import generate_page

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    for entry in os.listdir(dir_path_content):
        if os.path.isfile(f"{dir_path_content}/{entry}"):
            html_file = entry.replace(".md", ".html")
            generate_page(os.path.join(dir_path_content, entry), template_path, os.path.join(dest_dir_path, html_file), basepath)
        else:
            os.makedirs(os.path.join(dest_dir_path, entry), exist_ok=True)
            generate_pages_recursive(os.path.join(dir_path_content, entry), template_path, os.path.join(dest_dir_path, entry), basepath)
