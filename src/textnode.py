from enum import Enum

class Text_Type(Enum):
    PLAIN = "text(plain)"
    BOLD = "**Bold text**"
    ITALIC = "_Italic text_"
    CODE = "`Code text`"
    LINKS = "[anchor text](url)"
    IMAGES = "![alt text](url)"


class TextNode():
    def __init__(self, TEXT, TEXT_TYPE, URL):
        self.text = TEXT
        self.text_type = TEXT_TYPE
        self.url = URL

    def __eq__(self, other):
        return self == other

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"