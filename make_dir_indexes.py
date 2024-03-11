import os
import glob
from dotenv import load_dotenv

load_dotenv()
SRC = os.environ['SRC']
DOCS = os.environ['DOCS']

markdown_files = glob.glob(os.path.join(SRC, "**.md"))
print(markdown_files)
index_file = open("index.md", "w")

index_file.write("# Welcome!\n\n")

for markdown_file in sorted(markdown_files):
    if markdown_file.find('index') > -1:
        continue
    file_name = os.path.basename(markdown_file)
    title = file_name[:-3].title().replace('_', ' ')
    file_name = file_name.replace('.md', '.html')
    index_file.write(f"* [{title}]({file_name})\n")

index_file.close()
