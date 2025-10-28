from textnode import *
from htmlnode import *
from text_to_html import *
from extract_markdown import *

def text_to_textnodes(text):
    new_nodes = [TextNode(text, TextType.TEXT)]
    delimiters ={"**": TextType.BOLD, "_": TextType.ITALIC, "`": TextType.CODE}

    for delimiter in delimiters:
        new_nodes = split_nodes_delimiter(new_nodes, delimiter, delimiters[delimiter])
    
    
    new_nodes = split_nodes_image(new_nodes)
    new_nodes = split_nodes_link(new_nodes)
    
    return new_nodes

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

def split_nodes_image(old_nodes):
    node_list = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            node_list.append(node)
            continue
        text = node.text
        image_tuple = extract_markdown_images(text)
        if len(image_tuple) == 0:
            node_list.append(node)
            continue
        
        new = []
        remainig_text = text
        for tuple in image_tuple:
            image_alt, image_link = tuple[0], tuple[1]
            sections = remainig_text.split(f"![{image_alt}]({image_link})", 1)
            if len(sections) == 2:
                left, right = sections[0], sections[1]
                new.append(left)
                new.append(tuple)
                remainig_text = right
            else:
                raise Exception("invalid markdown, image section not closed")
        if remainig_text != "":
            new.append(remainig_text)  

        new_nodes = []
        for item in new:
            if type(item) == str:
                new_nodes.append(TextNode(item, node.text_type))
            else:
                new_nodes.append(TextNode(item[0], TextType.IMAGE, item[1]))
        
        node_list.extend(new_nodes)
    return node_list


        
        

def split_nodes_link(old_nodes):
    node_list = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            node_list.append(node)
            continue
        text = node.text
        link_tuple = extract_markdown_links(text)
        if len(link_tuple) == 0:
            node_list.append(node)
            continue
        
        new = []
        remainig_text = text
        for tuple in link_tuple:
            link_alt, raw_link = tuple[0], tuple[1]
            sections = remainig_text.split(f"[{link_alt}]({raw_link})", 1)
            if len(sections) == 2:
                left, right = sections[0], sections[1]
                new.append(left)
                new.append(tuple)
                remainig_text = right
            else:
                raise Exception("invalid markdown, link section not closed")
        if remainig_text != "":
            new.append(remainig_text)  

        new_nodes = []
        for item in new:
            if type(item) == str:
                new_nodes.append(TextNode(item, node.text_type))
            else:
                new_nodes.append(TextNode(item[0], TextType.LINK, item[1]))
        
        node_list.extend(new_nodes)
    return node_list