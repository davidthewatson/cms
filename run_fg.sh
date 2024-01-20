#! /bin/bash
cd src
source .env
source .venv/bin/activate
./build_site.sh 
python3.12 -m http.server -d $DOCS > /dev/null 2>&1 
deactivate
