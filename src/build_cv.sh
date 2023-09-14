python ./resumemd2htmldw.py
python ./resumemd2htmlww.py
wkhtmltopdf -T 2cm -L 3.5cm -R 1cm http://localhost:8000/cv/dw/index.html $DOCS/cv/dw/index.pdf
wkhtmltopdf http://localhost:8000/cv/ww/index.html $DOCS/cv/ww/index.pdf
