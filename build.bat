@echo off

echo =====================================
echo Cleaning previous builds...
echo =====================================

if exist build rmdir /s /q build
if exist dist rmdir /s /q dist

echo.
echo =====================================
echo Building Professional Billing Software
echo =====================================

pyinstaller ^
--clean ^
main.spec

echo.
echo =====================================
echo Build Completed
echo =====================================

pause