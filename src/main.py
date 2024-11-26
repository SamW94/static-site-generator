from copy_from_static_to_public import copy_from_static_to_public
from generate_page import generate_page

def main():
    source_dir = "static"
    destination_dir = "public"
    copy_from_static_to_public(source_dir, destination_dir)
    generate_page("content/index.md", "template.html", "public/index.html")

if __name__ == "__main__":
    main()
