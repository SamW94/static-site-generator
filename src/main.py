from copy_from_static_to_public import copy_from_static_to_public
from generate_pages_recursively import generate_pages_recursive

def main():
    source_dir = "static"
    destination_dir = "public"
    copy_from_static_to_public(source_dir, destination_dir)
    generate_pages_recursive("content", "template.html", "public")

if __name__ == "__main__":
    main()
