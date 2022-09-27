#!/usr/bin/python
"""consists of json string to python function"""
import json

def from_json_string(my_str):
    """"the python returns a python object from a json string"""
    return json.loads(my_str)
