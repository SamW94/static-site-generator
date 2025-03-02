from copy_from_static_to_public import copy_from_static_to_public
from generate_pages_recursively import generate_pages_recursive
import sys

def main():
    if len(sys.argv) < 2:
        basepath = "/"
    else:
        basepath = sys.argv[1]
    source_dir = "static"
    destination_dir = "docs"
    directory_path_content = "content"
    template_path = "./template.html"
    copy_from_static_to_public(source_dir, destination_dir)
    generate_pages_recursive(directory_path_content, template_path, destination_dir, basepath)

if __name__ == "__main__":
    main()
