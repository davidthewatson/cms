cd ../cms/src
sudo apt install -y wkhtmltopdf inotify-tools
python -m venv .venv
source .venv/bin/activate
pip install wheel
python setup.py bdist_wheel
pip install -r src/requirements.txt
source .env
./build_site.sh
