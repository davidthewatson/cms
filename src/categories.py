import os
import glob
import markdown

from dotenv import load_dotenv

load_dotenv()
SRC = os.environ['SRC']
DIRS = ['about', 'reading', 'writing', 'reflecting']
others = DIRS
others.remove('about')
def main():
    for DIR in DIRS:
        html = ''
        if DIR != 'about':
            html = f'### '
            for other in others:
                if DIR != other:
                    html += f'[{other}](/{other}/) '
                else:
                    html += f'{other} ' 
            html += '\n\n'
        lis = []
        for md in sorted(glob.glob(f'{SRC}/{DIR}/**/**[!404|!index]*.md', recursive=True)):
            pos = md.rfind('/')
            title_chunks = md[pos+1:-3].split('_') or md[:-3]
            title = ' '.join(title_chunks).title()
            href = f'<li><a href="{md[44:-3].replace("src/", "")}.html">{title}</a></li>'
            lis.append(href)
        if DIR != 'about':
            lis.sort()
            ul = ''.join(lis)
            html += f'<ul>{ul}</ul>'
            f = open(f'{SRC}/{DIR}/index.md', 'w')
            f.writelines(html)
            f.close()


if __name__ == '__main__':
    main()
"""

# Get the path to the parent directory
parent_dir = os.path.dirname(os.path.realpath(__file__))

# Create a list of all the subdirectories in the parent directory
subdirs = [os.path.join(parent_dir, subdir) for subdir in os.listdir(parent_dir) if os.path.isdir(os.path.join(parent_dir, subdir))]

# Create a Markdown file for each subdirectory
for subdir in subdirs:
    # Create a new Markdown file
    index_file = open(os.path.join(subdir, "dog.md"), "w")

    # Write the header for the Markdown file
    index_file.write(f"# {subdir[subdir.rfind('/')+1:].title()}\n\n")

    # Get a list of all the Markdown files in the subdirectory
    markdown_files = [os.path.join(subdir, markdown_file) for markdown_file in os.listdir(subdir) if markdown_file.endswith(".md")]

    # Write a link for each Markdown file in the Markdown file
    for markdown_file in sorted(markdown_files):
        pos = markdown_file.rfind('/')
        title_chunks = markdown_file[pos+1:-3].split('_') or markdown_file[:-3]
        title = ' '.join(title_chunks).title()
        print(title)
        href = f'<li><a href="{markdown_file[44:-3].replace("src/", "")}.html">{title}</a></li>'
        print(href)
        index_file.write(href)
        #index_file.write("* [{}]({})\n".format(os.path.basename(markdown_file), markdown_file))

    # Close the Markdown file
    index_file.close()

"""
