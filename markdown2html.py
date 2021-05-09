#!/usr/bin/python3
""" Start a script that takes an argument 2 strings """
from sys import argv, stderr
from shutil import copyfile


if __name__ == "__main__":
    """ Check existence of README and return respectively errors """
    if len(argv) < 2:
        print("Usage: ./markdown2html.py README.md README.html")
        exit(1)
    try:
        copyfile(argv[1], argv[2])
        exit(0)
    except IOError:
        print("Missing {}".format(argv[1]), file=stderr)
        exit(1)
