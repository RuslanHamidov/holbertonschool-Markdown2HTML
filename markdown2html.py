#!/usr/bin/python3


"""
  python3 -c 'print(__import__("my_module").__doc__)'

"""

import sys

if __name__ == "__main__":
  args = sys.argv
  if len(args) != 2:
      sys.stdout.write("Usage: ./markdown2html.py README.md README.html ")