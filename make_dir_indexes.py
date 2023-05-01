#!/usr/bin/env python3

import os
import glob

from dotenv import load_dotenv

load_dotenv()
SRC = os.environ['SRC']
DIRS = ['.']

def main():
    for DIR in DIRS:
        tmpl = open(f'{SRC}/{DIR}/_index.tpl')
        html = tmpl.readlines()
        tmpl.close()
        for directory in glob.glob(f'{SRC}/{DIR}/**/**', recursive=True):
            print(directory)
            if os.path.isdir(directory):
                lis = []
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
                f = open(f'{SRC}/{DIR}/{directory}/dir.md', 'w')
                f.writelines(html)
                f.close()

if __name__ == '__main__':
    main()
