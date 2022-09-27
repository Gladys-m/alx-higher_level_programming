#!/usr/bin/python3
"""consists of a write to UTF-8 file function"""

def write_file(filename="", text=""):
    """the funcion writes a string to a text file UTF-8
    Args:
        filename(str): Text file to write to
        text(str): the text to be written to the file

    Returns:
        Number of characters written
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return (f.write(text))
