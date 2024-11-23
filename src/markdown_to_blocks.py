def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    new_list = [block.strip() for block in blocks if block.strip() != ""]
    return new_list
