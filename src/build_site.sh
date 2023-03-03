/!/usr/bin/env bash

trap ctrl_c INT


function ctrl_c ()
{
    echo "Exiting..."
#    python ./resumemd2html.py 
#    wkhtmltopdf -B 2.54cm -L 2.54cm  -R 2.54cm -T 2.54cm http://localhost:8000/cv/dw/index.html $DOCS/cv/dw/index.pdf
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
    python ./resumemd2htmldw.py
    python ./resumemd2htmlww.py
    wkhtmltopdf http://localhost:8000/cv/dw/index.html $DOCS/cv/dw/index.pdf
    wkhtmltopdf http://localhost:8000/cv/ww/index.html $DOCS/cv/ww/index.pdf
    codespell --skip glossary.md $SRC *.md
    find $SRC -name "*.md" -exec proselint {} \; | cut -c 50- > /tmp/proselint.txt 
done

