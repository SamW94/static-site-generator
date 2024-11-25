from markdown_to_blocks import markdown_to_blocks
from block_to_block_type import block_to_block_type

def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        if block_to_block_type(block) == "heading" and block[0:6].count("#") == 1:
            return block[1::].strip()
        else:
            raise Exception("Markdown file does not contain a valid title.")
