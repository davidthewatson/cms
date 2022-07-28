#!/usr/bin/env bash

trap ctrl_c INT


function ctrl_c ()
{
    echo "Exiting..."
    python ./resumemd2html.py 
    wkhtmltopdf -B 2.54cm -L 2.54cm  -R 2.54cm -T 2.54cm http://localhost:8000/resume/index.html $DOCS/resume/index.pdf
    exit 2
}

# you should source .env from you siteroot such that it is defined before running this script
echo $SITEROOT

while inotifywait -r -e close_write -e move -e create $SRC $STATIC
do
#    rm -rf $DOCS/*
    cp -rf $STATIC/* $DOCS/.
    echo "$STATIC/* $DOCS/."
    
    python ./make_index.py
    python ./md2html.py
    python ./resumemd2html.py 
    wkhtmltopdf -B 2.54cm -L 2.54cm  -R 2.54cm -T 2.54cm http://localhost:8000/resume/index.html $DOCS/resume/index.pdf

    echo "HTML STATS"
    find $DOCS -name "*.html"
    find $DOCS -name "*.html" | wc -l
done

