. ./.env
. ./.venv/bin/activate
cd src
./build_site.sh 
python -m http.server -d $DOCS  
deactivate
