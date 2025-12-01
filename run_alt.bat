@echo off
echo Installing dependencies...
py -m pip install -r requirements.txt
echo.
echo Starting Flask server...
py app.py
pause


