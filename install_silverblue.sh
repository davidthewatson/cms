cd ../cms/src
sudo dnf install python wkhtmltopdf inotify-tools
python -m venv .venv
source .venv/bin/activate
# pip install wheel
# python setup.py bdist_wheel
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
deactivate