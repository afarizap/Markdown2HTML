#!/usr/bin/python3
""" Start a script that takes an argument 2 strings """
from sys import argv, stderr
from shutil import copyfile


if __name__ == "__main__":
    """ Check existence of README and return respectively errors """
    if len(argv) < 3:
        stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        exit(1)
    try:
        copyfile(argv[1], argv[2])
        exit(0)
    except IOError:
        stderr.write("Missing {}\n".format(argv[1]))        
        exit(1)
