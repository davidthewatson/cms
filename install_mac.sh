brew install codespell proselint watchman
python3.12 -m venv .venv
source .venv/bin/activate
pip install wheel
python3.12 setup.py bdist_wheel
pip install -r requirements.txt
deactivate
