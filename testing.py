#!/usr/bin/python3
""" 
Write a script markdown2html.py that takes an argument 2 strings:
First argument is the name of the Markdown file
Second argument is the output file name 
"""

import os
import sys
import re

def parse_section(section_text):
    headings = re.findall(r'(#+)\s*(.*)', section_text)
    html_content = ""
    if headings:
        for hash_count, title in headings:
            hash_level = len(hash_count)
            html_content += f"<h{hash_level}>{title.strip()}</h{hash_level}>\n"

    lines_with_dashes = re.findall(r'(-+)\s*(.*)', section_text)
    if lines_with_dashes:
        html_content += "<ul>\n"
        for _, words in lines_with_dashes:
            html_content += f"    <li>{words.strip()}</li>\n"
        html_content += "</ul>\n"
    
    lines_with_stars = re.findall(r'(\*+)\s*(.*)', section_text) 
    if lines_with_stars:
        html_content += "<ol>\n"
        for _, words in lines_with_stars:
            html_content += f"    <li>{words.strip()}</li>\n"
        html_content += "</ol>\n"
        
    paragraphs = re.split(r"\n\s*\n", section_text.strip())
    if not headings and not lines_with_dashes:
        for paragraph in paragraphs:
            html_paragraph = paragraph.replace('\n', '<br>')
            html_content += f"<p>{html_paragraph}</p>\n"
    
    
    for i, line in enumerate(section_text):
                # Search ** ** and replace by <b> </b>
        line = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', line)
                
                # Search __ __ and replace by <em> </em>
        line = re.sub(r'__(.*?)__', r'<em>\1</em>', line)
    
    """ lines_with_double_stars = re.findall(r'(\*\*+)\s*(.*)', section_text)
    for _, word in lines_with_double_stars:
        html_content += f"<b>{word.strip('*')}</b>\n"
    
    lines_with_underline = re.findall(r'(__+)\s*(.*)', section_text) 
    for _, word in lines_with_underline:
      html_content += f"<em>{word.strip(_)}</em>\n" """
    
    return html_content

if __name__ == "__main__":
    args = sys.argv
    if len(args) != 3:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        exit(1)

    input_file = args[1]
    output_file = args[2]

    if not os.path.exists(input_file):
        sys.stderr.write(f"Missing {input_file}\n")
        exit(1)

    with open(input_file, "r") as readme_file:
        text = readme_file.read()

    sections = re.split(r'(#{1,6}\s+.*)', text)  # Split text into sections based on headings

    html_content = ""
    for section_text in sections:
        if section_text.strip():  # Skip empty sections
            html_content += parse_section(section_text)

    with open(output_file, 'w') as html_file:
        html_file.write(html_content)

    exit(0)

