#!/usr/bin/python3
"""Add all arguments to a Python list then saves them to a file."""
import sys   #enables use of sys.argv built in function

if __name__ == "__main__": 
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

    try:
        items = load_from_json_file("add_item.json")   #if file exixst set object to var items
    except FileNotFoundError:   #if file is not found...
        items = []   #create an empty list
    items.extend(sys.argv[1:])   #extend or add multiple items that are arguments to python script
    save_to_json_file(items, "add_item.json")   #writes python objects to json file
