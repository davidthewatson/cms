#!/usr/bin/env python3

# Convert markdown to HTML

import os
import markdown

from pathlib import Path
from staticjinja import Site
from dotenv import load_dotenv

load_dotenv()
SRC = os.environ['SRC']
DOCS = os.environ['DOCS']
markdowner = markdown.Markdown(output_format="html5")


def site_context(template):
    markdown_content = Path(template.filename).read_text()
    return {"post_content_html": markdowner.convert(markdown_content)}


def render_site(site, template, **kwargs):
    out = site.outpath / Path(template.name).with_suffix(".html")
    os.makedirs(out.parent, exist_ok=True)
    site.get_template("_base.html").stream(**kwargs).dump(str(out), encoding="utf-8")

site = Site.make_site(
    searchpath=f"{SRC}",
    outpath=f"{DOCS}",
    contexts=[(r".*\.md", site_context)],
    rules=[(r".*\.md", render_site)]
)


site.render()
