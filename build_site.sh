#!/usr/bin/env bash
 
while inotifywait -r -e close_write -e move -e create src/ static/
do
    rm -rf docs/*
    cp -rf static/* docs/.

    python ./make_index.py

    python ./md2html.py
    python ./md2txt.py
    python ./html2pdf.py

    echo "HTML STATS"
    find ./docs -name "*.html"
    find ./docs -name "*.html" | wc -l
    echo "TEXT STATS"
    find ./docs -name "*.txt"
    find ./docs -name "*.txt" | wc -l
    echo "PDF STATS"
    find ./docs -name "*.pdf"
    find ./docs -name "*.pdf" | wc -l
done

