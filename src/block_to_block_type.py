import re

def validate_ordered_list_helper_function(text):
    lines = text.split("\n")
    for i, line in enumerate(lines):
        expected_number = i + 1
        if not re.match(rf"^{expected_number}\. ", line):
            return False
    return True

def block_to_block_type(block):
    if re.match(r"^#{1,6} .+", block):
        return "heading"
    if re.match(r"^```[\s\S]*```$", block):
        return "code"
    if re.match(r"^(>.*(\n|$))*$", block):
        return "quote"
    if re.match(r"^([*-] .*(\n|$))*$", block):
        return "unordered_list"
    if block.startswith("1. "):
        if validate_ordered_list_helper_function(block) == True:
            return "ordered_list"
        else: 
            return "paragraph"
    else:
        return "paragraph"
