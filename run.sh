cd src
source .env
source .venv/bin/activate
python -m http.server -d $DOCS > /dev/null 2>&1 &
./build_site.sh > /dev/null 2>&1 &
