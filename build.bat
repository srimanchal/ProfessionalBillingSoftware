@echo off

echo ======================================
echo Cleaning old builds...
echo ======================================

if exist build rmdir /s /q build
if exist dist rmdir /s /q dist

echo.
echo ======================================
echo Building Professional Billing Software
echo ======================================

pyinstaller ^
--noconfirm ^
--clean ^
--windowed ^
--icon=assets\icons\app.ico ^
--name="Professional Billing Software" ^
--collect-all PySide6 ^
--add-data "assets;assets" ^
--add-data "config;config" ^
app\main.py

echo.
echo ======================================
echo Build Completed
echo ======================================
pause