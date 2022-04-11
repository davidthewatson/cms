#!/usr/bin/env python3

# Convert markdown to PDF

import glob
import html
import re
import subprocess

from io import StringIO


def main():
    print('Rendering PDF')
    for html_file in glob.glob('docs/**/**[!404]*.html', recursive=True):
        print(html_file)
        url = 'http://localhost:8000' + html_file.replace('docs', '')
        output_prefix = html_file.replace('src', 'docs')
        output_name = output_prefix.replace('html', 'pdf')
        print(url, output_name)
        subprocess.run(['./subprocess_wkhtmltopdf.sh', url, output_name])
if __name__ == '__main__':
    main()


