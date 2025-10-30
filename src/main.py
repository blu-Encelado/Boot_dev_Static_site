from textnode import *
from blocktype import markdown_to_html_node
from extract_markdown import extract_title
import os
import shutil

print("initialize main.py")
public = "./public"
static = "./static"
content = "./content/index.md"
template = "./template.html"
content_dir = "./content"

def main():
    path_exists = os.path.exists(public)
    if path_exists:
        shutil.rmtree(public)
    
    os.mkdir(public)
    path_to_public = os.path.abspath(public)

    
    static_items_list = os.listdir(static)
    if len(static_items_list) > 0:
        for item in static_items_list:

            path_to_item = os.path.abspath(static) + f"/{item}"
            is_dir = os.path.isdir(path_to_item)
            if not is_dir:
                shutil.copy(path_to_item, path_to_public)
            else:
                shutil.copytree(path_to_item, path_to_public + f"/{item}")        
    else:
        raise Exception(f"No Object in {static}")   
    
    generating_pages_recursive(content_dir, template, public)


def generating_page(from_path, template_path, dest_path):
    
    #print(f"Generating page from '{from_path}' \nto '{dest_path}'")

    open_content = open(from_path, "r").read()

    html_content = markdown_to_html_node(open_content).to_html()
    page_title = extract_title(open_content)
    open_template = open(template_path).read()

    mod_template = open_template.replace("{{ Title }}", page_title)
    final_template = mod_template.replace("{{ Content }}", html_content)
    if not os.path.exists(dest_path):
        os.makedirs(dest_path)
    dest_file = open(dest_path + "/index.html", "w").write(final_template)


def generating_pages_recursive(dir_path_content, template_path, dest_dir_path):
    abs_dir_path_content = os.path.abspath(dir_path_content)
    abs_template_path = os.path.abspath(template_path)
    abs_dir_path_destination = os.path.abspath(dest_dir_path)
    if os.path.isdir(abs_dir_path_content):
        content_dir = os.listdir(abs_dir_path_content)
        for item in content_dir:
            path_to_item = abs_dir_path_content + f"/{item}"
            if os.path.isfile(path_to_item):
                r = "/".join(os.path.relpath(abs_dir_path_content).split("/")[1:])
                
                dest_path = os.path.join(abs_dir_path_destination, r)
                print(dest_path)
                generating_page(path_to_item, abs_template_path, dest_path)
            else:
                generating_pages_recursive(path_to_item, template_path, dest_dir_path)
    


if __name__ == "__main__":
    main()
