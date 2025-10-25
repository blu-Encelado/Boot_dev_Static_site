from textnode import *
from htmlnode import *
from text_to_html import *


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    nodes_list = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            nodes_list.append(node)
            continue
        
        split = node.text.split(delimiter)
        
        if len(split) % 2 == 0:
            raise Exception("Syntax Error")
        
        new = []

        for i, sentence in enumerate(split):
            if i % 2 == 0:
                if sentence:  
                    new.append(TextNode(sentence, TextType.TEXT))
            else:
                if sentence:
                    new.append(TextNode(sentence, text_type))

    nodes_list.extend(new)
    
    return nodes_list