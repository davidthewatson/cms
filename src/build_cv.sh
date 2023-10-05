#!/usr/bin/env bash

# you should source .env from you siteroot such that it is defined before running this script
echo $SITEROOT

while inotifywait -r -e close_write -e move -e create -e delete $SRCDW $STATIC
do
#    rm -rf $DOCS/*
    cp -rf $STATIC/* $DOCS/.
    echo "$STATIC/* $DOCS/."

    python ./resumemd2htmldw.py
    python ./resumemd2htmlww.py
    wkhtmltopdf -T 2cm -L 3.5cm -R 1cm http://localhost:8000/cv/dw/index.html $DOCS/cv/dw/index.pdf
    wkhtmltopdf http://localhost:8000/cv/ww/index.html $DOCS/cv/ww/index.pdf
done