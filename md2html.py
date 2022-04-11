#!/usr/bin/env python3

# Convert markdown to HTML

import os
from pathlib import Path

import markdown

from staticjinja import Site

markdowner = markdown.Markdown(output_format="html5")


def site_context(template):
    markdown_content = Path(template.filename).read_text()
    return {"post_content_html": markdowner.convert(markdown_content)}

def render_site(site, template, **kwargs):
    # i.e. posts/post1.md -> build/posts/post1.html
    out = site.outpath / Path(template.name).with_suffix(".html")
    print(out)
    # Compile and stream the result
    os.makedirs(out.parent, exist_ok=True)
    site.get_template("_base.html").stream(**kwargs).dump(str(out), encoding="utf-8")
print('rendering site')

site = Site.make_site(
    searchpath="src",
    outpath="docs",
    contexts=[(r".*\.md", site_context)],
    rules=[(r".*\.md", render_site)],
)

site.render()