#!/usr/bin/env zsh
. ../.env
rm -rf $DOCS/*
cp -rf $STATIC/* $DOCS/.
    
python ./md2html.py
codespell $SRC 
find $SRC -name "*.md" -exec proselint {} \; | cut -c 50- > /tmp/proselint.txt 

