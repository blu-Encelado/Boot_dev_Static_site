from textnode import *
import os
import shutil

print("initialize main.py")
public = "./public"
static = "./static"

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
        



if __name__ == "__main__":
    main()
