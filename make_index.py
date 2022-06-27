#!/usr/bin/env python3

import os
import glob

from dotenv import load_dotenv

load_dotenv()
SRC = os.environ['SRC']

def main():
    s = ''
    html = '### essays\n\n'
    lis = []
    for md in glob.glob(f'{SRC}/**/**[!404|!index]*.md', recursive=True):
        pos = md.rfind('/')
        title_chunks = md[pos+1:-3].split('_') or md[:-3]
        title = ' '.join(title_chunks).title()
        print(title)
        href= f'<li><a href="{md[29:-3].replace("src/", "")}.html">{title}</a></li>'
        lis.append(href)
    lis.sort()
    ul = ''.join(lis)
    html += f'<ul>{ul}</ul>'
    f = open(f'{SRC}/essays/index.md', 'w')
    f.writelines(html)
    f.close()

if __name__ == '__main__':
    main()