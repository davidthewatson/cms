#!/usr/bin/env python3

import os
import glob

from dotenv import load_dotenv

load_dotenv()
SRC = os.environ['SRC']
DIRS = ['write', 'read', 'reflect']

def main():
    for DIR in DIRS:    
        tmpl = open(f'{SRC}/{DIR}/_index.tpl')
        html = tmpl.readlines()
        tmpl.close()
        lis = []
        for md in glob.glob(f'{SRC}/{DIR}/**/**[!404|!index]*.md', recursive=True):
            pos = md.rfind('/')
            title_chunks = md[pos+1:-3].split('_') or md[:-3]
            title = ' '.join(title_chunks).title()
            print(title)
            href = f'<li><a href="{md[44:-3].replace("src/", "")}.html">{title}</a></li>'
            print(href)
            lis.append(href)
        lis.sort()
        ul = ''.join(lis)
        html += f'<ul>{ul}</ul>'
        f = open(f'{SRC}/{DIR}/index.md', 'w')
        f.writelines(html)
        f.close()


if __name__ == '__main__':
    main()
