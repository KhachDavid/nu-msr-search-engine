#!/bin/bash
cd ~/nu-msr-search-engine/
source /home/david/nu-msr-search-engine/venv/bin/activate
cd
python3 ~/nu-msr-search-engine/get_files.py katana
cd ~/nu-msr-search-engine/
git add .
git commit -m "Update files"
git push origin main
deactivate
