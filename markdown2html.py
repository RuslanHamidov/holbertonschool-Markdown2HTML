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
        
    lines_with_stars = re.findall(r'(*+)\s*(.*)', section_text)
    if lines_with_stars:
        html_content += "<ol>\n"
        for _, words in lines_with_stars:
            html_content += f"    <li>{words.strip()}</li>\n"
        html_content += "</ol>\n"

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

