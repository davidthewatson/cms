sudo pamac install codespell inotify-tools proselint uv
uv venv ../.venv
source ../.venv/bin/activate
uv pip install -r requirements.txt
deactivate
