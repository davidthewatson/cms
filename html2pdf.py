#!/usr/bin/env python3

# Convert markdown to PDF

import os
import glob
import html
import re
import subprocess

from io import StringIO
from dotenv import load_dotenv

load_dotenv()
SRC = os.environ['SRC']
DOCS = os.environ['DOCS']


def main():
    print('Rendering PDF')
    for html_file in glob.glob(f'{DOCS}/**/**[!404]*.html', recursive=True):
        print(html_file)
        url = 'http://localhost:8000' + os.path.split(html_file)[1]
        output_prefix = html_file.replace('src', 'docs')  # assuming file extension here
        output_name = output_prefix.replace('html', 'pdf') # and here - need to revisit!
        print(url, output_name)
        subprocess.run(['./subprocess_wkhtmltopdf.sh', url, output_name])
if __name__ == '__main__':
    main()


