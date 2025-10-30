import re

def extract_markdown_images(text):
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def markdown_to_blocks(markdown):
    blocks = []
    split = markdown.split(f"\n\n")
    for string in split:
        if string == "":
            continue
        new = string.strip()
        blocks.append(new)

    return blocks

def extract_title(markdown):
    lines = markdown.split("\n")
    
    for line in lines:
        if line == "":
            continue
        clean_markdown = line.strip()
        if clean_markdown.startswith("#") and clean_markdown[1] == " ": 
            title = clean_markdown[1:].strip()
            break
        else:
            raise ValueError("Syntax Error in h1 Title Missing")
    
    return title