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