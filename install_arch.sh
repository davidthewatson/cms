cd ../cms/src
sudo pamac install wkhtmltopdf-static inotify-tools
python -m venv .venv
source .venv/bin/activate
pip install wheel
python setup.py bdist_wheel
pip install -r requirements.txt
deactivate