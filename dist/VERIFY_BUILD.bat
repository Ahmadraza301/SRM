@echo off
title Build Verification Script
color 0B

echo.
echo ========================================
echo   Build Verification Script
echo ========================================
echo.

echo Checking dist folder contents...
echo.

if exist "dist\dashboard.exe" (
    echo ✓ dashboard.exe - Found
) else (
    echo ✗ dashboard.exe - Missing
)

if exist "dist\report.exe" (
    echo ✓ report.exe - Found
) else (
    echo ✗ report.exe - Missing
)

if exist "dist\rms.db" (
    echo ✓ rms.db - Found
    for %%A in ("dist\rms.db") do echo   Size: %%~zA bytes
) else (
    echo ✗ rms.db - Missing
)

if exist "dist\images" (
    echo ✓ images folder - Found
    dir /b "dist\images\*.png" >nul 2>&1
    if %errorlevel%==0 (
        echo   Contains PNG files
    )
    dir /b "dist\images\*.jpg" >nul 2>&1
    if %errorlevel%==0 (
        echo   Contains JPG files
    )
) else (
    echo ✗ images folder - Missing
)

if exist "dist\LAUNCHER.bat" (
    echo ✓ LAUNCHER.bat - Found
) else (
    echo ✗ LAUNCHER.bat - Missing
)

if exist "dist\README.md" (
    echo ✓ README.md - Found
) else (
    echo ✗ README.md - Missing
)

if exist "dist\FIXES_SUMMARY.md" (
    echo ✓ FIXES_SUMMARY.md - Found
) else (
    echo ✗ FIXES_SUMMARY.md - Missing
)

echo.
echo ========================================
echo   Verification Complete
echo ========================================
echo.

echo To test the executables:
echo 1. Navigate to the dist folder
echo 2. Run LAUNCHER.bat
echo 3. Or run dashboard.exe directly
echo.

pause
