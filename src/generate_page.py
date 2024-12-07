import os

from markdown_to_html_node import markdown_to_html_node
from extract_title import extract_title

def generate_page(from_path, template_path, dest_path):
    # Print a message to the console.
    print(f"Generating page from {from_path} to {dest_path} using {template_path}.")
    
    # Read the markdown file at from_path and store the contents in a variable.
    markdown_file = open(from_path, mode='r')
    try:
        markdown = markdown_file.read()
    except Exception as e:
        print(f"Failed to read markdown file: {e}.")
    markdown_file.close()

    # Read the template file at template_path and store the contents in a variable.
    template_file = open(template_path, mode='r')
    try:
        template = template_file.read()
    except Exception as e:
        print(f"Failed to read template file: {e}.")
    template_file.close()

    # Use the markdown_to_html_node function to convert the markdown file to an HTML string. Use the extract_title function to get the title of the page.
    content = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)

    # Replace the {{ Title }} and {{ Content }} placeholders in the template file with the content and title strings
    new_template = template.replace("{{ Title }}", title)
    new_template = new_template.replace("{{ Content }}", content)

    # Write the new full HTML page to a file at dest_path  
    destination_file = open(dest_path, mode='w')
    try:
        destination_file.write(new_template)
    except Exception as e:
        print(f"Failed to write to destination file: {e}")
    destination_file.close()
