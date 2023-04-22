#!/usr/bin/env python3

# Convert markdown to plain text from https://stackoverflow.com/a/54923798

import os
import glob
import markdown

from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()
SRC = os.environ['SRC']
DOCS = os.environ['DOCS']


def md_to_text(md):
    html = markdown.markdown(md)
    soup = BeautifulSoup(html, features='html.parser')
    return soup.get_text()


def main():
    print('Rendering plain text')
    for md in glob.glob(f'{SRC}/**/**[!404]*.md', recursive=True):
        f = open(md, 'r')
        txt = md_to_text(f.read())
        new_name = md.replace('src', 'docs')  # assuming name is src -> docs here, need to revisit
        new_name = new_name.replace('md', 'txt')
        print(new_name)
        n = open(new_name, 'w')
        n.write(txt)


if __name__ == '__main__':
    main()
