#!/usr/bin/python3
""""function that writes python object to json file"""
import json

def save_to_json_file(my_obj, filename):
    """writes a python object to text file using python"""
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
