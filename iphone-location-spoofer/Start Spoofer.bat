@echo off
title iPhone Location Spoofer
rem Double-click this file to start everything.
cd /d "%~dp0"

echo Starting the connection bridge in a new window...
echo Click YES if Windows asks for permission.
powershell -NoProfile -Command "Start-Process cmd -Verb RunAs -ArgumentList '/k title Connection bridge - leave open && py -3.13 -m pymobiledevice3 remote tunneld'"

echo Waiting for the bridge to get ready...
timeout /t 10 /nobreak >nul

py -3.13 spoof.py
pause
