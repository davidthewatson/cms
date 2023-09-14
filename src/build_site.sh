#!/usr/bin/env bash

# you should source .env from you siteroot such that it is defined before running this script
echo $SITEROOT

while inotifywait -r -e close_write -e move -e create -e delete $SRC $STATIC
do
#    rm -rf $DOCS/*
    cp -rf $STATIC/* $DOCS/.
    echo "$STATIC/* $DOCS/."
    
    python ./make_index.py
    python ./md2html.py
    codespell .$SRC *.md
    find $SRC -name "*.md" -exec proselint {} \; | cut -c 50- > /tmp/proselint.txt 
done

