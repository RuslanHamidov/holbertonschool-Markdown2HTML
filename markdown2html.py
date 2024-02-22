#!/usr/bin/python3



''' python3 -c 'print(__import__("my_module").__doc__)' '''


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

