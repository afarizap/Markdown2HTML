#!/usr/bin/python3
""" Start a script that takes an argument 2 strings """
from sys import argv, stderr


if __name__ == "__main__":
    """ Check existence of README and return respectively errors """
    if len(argv) < 2:
        print("Usage: ./markdown2html.py README.md README.html")
        exit(1)
    try:
        with open(argv[1]) as f:
            exit(0)
    except IOError:
        print("Missing {}".format(argv[1]))
        exit(1)

