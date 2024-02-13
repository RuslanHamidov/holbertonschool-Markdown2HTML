#!/usr/bin/python3


"""
  python3 -c 'print(__import__("my_module").__doc__)'

"""
import os
import sys

if __name__ == "__main__":
  args = sys.argv
  if len(args) < 2:
      sys.stderr("Usage: ./markdown2html.py README.md README.html\n")
      exit(1)

  if not os.path.exists(args[1]):
     sys.stderr("Missing" + args[1] +"\n")
     exit(1)

  exit(0)

