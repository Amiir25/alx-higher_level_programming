#!/usr/bin/python3
"""
5-text_indentation.py

This module provides a function that prints a text with
two new lines after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    Prints a text with two new lines after each '.', ? and : characters
    and ignores the sapce right after these characters.

    Args:
        text (str): The text to be printed

    Raises:
        TypeError: if the input text is not a stirng
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = ""
    i = 0

    while i < len(text):
        result += text[i]

        if text[i] in ['.', '?', ':']:
            result += "\n\n"

            i += 1
            while i < len(text) and text[i] == ' ':
                i += 1

            continue

        i += 1

    print(result.rstrip(), end='')


if __name__ == "__main__":
    import doctest
    doctest.testfile("5-text_indentation.txt")
