#!/usr/bin/python3


""" text indentation module """


def text_indentation(text):
    """Prints a text with 2 new lines after: ., ? and :.

    Args:
        text (str): text to print.

    Raises:
        TypeError: if text is not a string.
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    else:
        text = text.replace(".", ".\n\n")
        text = text.replace(":", ":\n\n")
        text = text.replace("?", "?\n\n")
        print(text, end="")
