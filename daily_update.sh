#!/bin/bash
cd ~/nu-msr-search-engine/
source /home/david/nu-msr-search-engine/venv/bin/activate
python3 get_files.py katana
git add .
git commit -m "Update files"
git push origin main

