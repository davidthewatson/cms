#! /bin/bash
cd src
. .env
. .venv/bin/activate
python -m http.server -d $DOCS > /dev/null 2>&1 &
./build_site.sh 
