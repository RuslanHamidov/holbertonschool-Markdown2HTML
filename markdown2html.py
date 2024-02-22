#!/usr/bin/python3

'''Script that takes an argument 2 strings:
First argument is the name of the Markdown file
Second argument is the output file name
script converts the markdown file to HTML
The script will convert the following markdown syntax:
- Headers: Any number of #s at the start of a line
- Unordered listing: Lines that start with a dash (-)
- Ordered listing: Lines that start with a star (*)
- Text in double asterisks (**) is bold
- Text in double underscores (__) is italic
- Text in double brackets (()) is hashed
- Text in double parentheses (()) is case insensitive
The script will convert the markdown file to HTML and write it to the output file
If the markdown file does not exist, the script will print Missing <filename> and exit with a status code of 1
If the output file already exists, it will be overwritten
The script will exit with a status code of 0 upon success

Usage: ./markdown2html.py README.md README.html 
'''

import os
import sys
import re

with open(sys.argv[1], "r") as readme_file:
  text = readme_file.read()
  
  def toHtml(textfile):
    hashes = re.findall(r'(#+)\s*(.*)', textfile)
    html_content = ""
    for hash_count, title in hashes:
        hash_level = len(hash_count)
        html_content += f"<h{hash_level}>{title.strip()}</h{hash_level}>\n"
    return html_content
  
  html = toHtml(text)
  
if __name__ == "__main__":
  args = sys.argv
  if len(args) < 3:
      sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
      exit(1)

  if not os.path.exists(args[1]):
     sys.stderr.write("Missing " + args[1] +"\n")
     exit(1)
     
  with open(sys.argv[2], 'w') as html_file:
    html_file.write(html)
  
  exit(0)

