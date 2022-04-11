#!/usr/bin/env python3

# Convert markdown to plain text from https://stackoverflow.com/a/54923798

from markdown import Markdown
from io import StringIO
import glob
import html


import markdown # pip install markdown
from bs4 import BeautifulSoup # pip install beautifulsoup4

def md_to_text(md):
    html = markdown.markdown(md)
    soup = BeautifulSoup(html, features='html.parser')
    return soup.get_text()

def example():
    md = '**A** [B](http://example.com) <!-- C -->'
    text = md_to_text(md)
    print(text)
    # Output: A B

def main():
    print('Rendering plain text')
    for md in glob.glob('src/**/**[!404]*.md', recursive=True):
        f = open(md, 'r')
        txt = md_to_text(f.read())
        new_name = md.replace('src', 'docs')
        new_name = new_name.replace('md', 'txt')
        print(new_name)
        n = open(new_name, 'w')
        n.write(txt)

if __name__ == '__main__':
    main()
