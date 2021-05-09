#!/usr/bin/python3
""" Copy file form arg 1 and name it with arg 2 value """
from sys import argv, stderr


if __name__ == "__main__":
    """ Copy files or exit and error to stderr """
    if len(argv) < 3:
        stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        exit(1)
    try:
        copyfile(argv[1], argv[2])
        exit(0)
    except:
        stderr.write("Missing {}\n".format(argv[1]))        
        exit(1)
