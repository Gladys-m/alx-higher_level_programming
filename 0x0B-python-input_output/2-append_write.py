#!/usr/bin/python3
"""consists of a function that appends a string to text file"""

def append_write(filename="", text=""):
    """appends a string at the end of a UTF8 text file
    Args:
        filename(str): file to append to
        text(str): text to append
    Returns:
        number of characters added
    """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
