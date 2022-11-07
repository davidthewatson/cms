#!/usr/bin/env bash

trap ctrl_c INT


function ctrl_c ()
{
    echo "Exiting..."
    python ./resumemd2html.py 
    wkhtmltopdf -B 3cm -L 2cm  -R 2cm -T 2cm http://localhost:8000/cv/dw/index.html $DOCS/cv/dw/index.pdf
    exit 2
}

# you should source .env from you siteroot such that it is defined before running this script
echo $SITEROOT

while inotifywait -r -e close_write -e move -e create -e delete $SRC $STATIC
do
#    rm -rf $DOCS/*
    cp -rf $STATIC/* $DOCS/.
    echo "$STATIC/* $DOCS/."
    
    python ./make_index.py
    python ./md2html.py
    python ./resumemd2html.py 
    python ./resumemd2htmlww.py
    wkhtmltopdf -B 3cm -L 2cm -R 2cm -T 2cm http://localhost:8000/cv/ww/index.html $DOCS/cv/ww/index.pdf
    wkhtmltopdf -B 3cm -L 2cm  -R 2cm -T 2cm http://localhost:8000/cv/dw/index.html $DOCS/cv/dw/index.pdf

    echo "HTML STATS"
    find $DOCS -name "*.html"
    find $DOCS -name "*.html" | wc -l
done

