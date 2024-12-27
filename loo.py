import mistune

from glob import glob
from dotenv import load_dotenv
from os import environ, path, sep
from typing import Optional

markdown = mistune.create_markdown(plugins=['strikethrough', 'table', 'task_lists', 'url', 'footnotes'])

load_dotenv()

SRC = environ['SRC']
DOCS = environ['DOCS']
STATIC = environ['STATIC']

markdown_glob = '*.md'
recurse_directory_tree = '**'
files_glob = path.join(SRC, recurse_directory_tree, markdown_glob)
input_file_paths = glob(files_glob, recursive=True)

def get_mid_path(path: str) -> str:
    parts = path.split(sep)
    print(part for part in parts)
    return sep.join(parts[1:-1])

def render_markdown(markdown_text):
    markdown = mistune.create_markdown(plugins=['strikethrough', 'table', 'task_lists', 'url', 'footnotes'])
    html = markdown(markdown_text)
    return html

for input_file_path in input_file_paths:
    diff_path = get_mid_path(input_file_path)
    base_name_with_extension = path.basename(input_file_path)
    base_name = path.splitext(base_name_with_extension)[0]
    print(DOCS, diff_path, f'{base_name}.html')
    output_filename = path.join(DOCS, diff_path, f'{base_name}.html')
    with open(input_file_path, 'r') as input_file, open(output_filename, 'w') as output_file:
        input_file_markdown = input_file.read()
        output_file_html = render_markdown(input_file_markdown)
        print(f'Content of {input_file}:\n\n{input_file_markdown}\n\n')
        print(f'Content of {output_file}:\n\n{output_file_html}\n\n')
        output_file.write(output_file_html)
