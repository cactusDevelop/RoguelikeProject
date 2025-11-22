@echo off
cd /d "%~dp0"

call .venv\Scripts\activate
pip install -q -r requirements.txt

python src\main.py

pause