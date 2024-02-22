#!/usr/bin/python3
""" 
Write a script markdown2html.py that takes an argument 2 strings:
First argument is the name of the Markdown file
Second argument is the output file name 
"""

import os
import sys
import re


  
if __name__ == "__main__":
  '''
  Starting point of script
  '''
  args = sys.argv
  if len(args) < 3:
      sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
      exit(1)

  if not os.path.exists(args[1]):
     sys.stderr.write("Missing " + args[1] +"\n")
     exit(1)
     
  with open(sys.argv[1], "r") as readme_file:
    '''
    Opening readme
    '''
    text = readme_file.read()
  
  def toHtml(textfile):
    '''
    To parse file from readme to HTML
    '''
    hashes = re.findall(r'(#+)\s*(.*)', textfile)
    

    html_content = ""
    for hash_count, title in hashes:
        hash_level = len(hash_count)
        html_content += f"<h{hash_level}>{title.strip()}</h{hash_level}>\n"
    '''
    adding to html
    '''
    lines_with_dashes = [line.strip() for line in text if '-' in line]

    if lines_with_dashes:
        html_list = "<ul>\n" + '\n'.join([f"<li>{line}</li>" for line in lines_with_dashes]) + "\n</ul>"

    return html_content
  
  html = toHtml(text)
     
  with open(sys.argv[2], 'w') as html_file:
    html_file.write(html)
  
  exit(0)

