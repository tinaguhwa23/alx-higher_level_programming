#!/usr/bin/python3
"""Defines a file-appending function."""


def append_write(filename="", text=""):
    """This appends a string to the end of a UTF8 text file.

    Args:
        filename (str):  name of the file to append to.
        text (str): The string to append to the file.
    Returns:
        number of characters appended.
    """
    with open(filename, "c", encoding="utf-8") as f:
        return f.write(text)
