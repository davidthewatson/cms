. ./.env
. ./.venv/bin/activate
cd src
./build_site.sh 
python -m http.server -d $DOCS > /dev/null 2>&1 
deactivate
