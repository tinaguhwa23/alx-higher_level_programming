#!/usr/bin/python3
"""Defines a file-writing function."""


def write_file(filename="", text=""):
    """writes a string to a UTF8 text file.

    Args:
        filename (str): The name of the file to write.
        text (str): text to write to the file.
    Returns:
         number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
