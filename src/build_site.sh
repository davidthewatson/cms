#!/usr/bin/env bash

# you should source .env from you siteroot such that it is defined before running this script
echo $SITEROOT

rm -rf $DOCS/*
cp -rf $STATIC/* $DOCS/.
echo "$STATIC/* $DOCS/."
    
python3.12 ./md2html.py
codespell .$SRC *.md
find $SRC -name "*.md" -exec proselint {} \; | cut -c 50- > /tmp/proselint.txt 

