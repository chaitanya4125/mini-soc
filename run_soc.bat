@echo off
title MINI SOC - Complete System
color 0A
cls

echo ============================================
echo     MINI SOC - Windows Complete Launcher
echo ============================================
echo.

REM Check Python
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python not found! Install Python 3.x
    pause
    exit
)

echo [*] Starting SOC System...
echo.

REM Start log generator
echo [1/3] Starting Log Generator...
start "Log Generator" cmd /k "title Log Generator && python log_generator.py && pause"

REM Wait for initial logs
echo [*] Waiting for initial events...
timeout /t 3 /nobreak >nul

REM Start SOC monitor
echo [2/3] Starting SOC Monitor...
start "SOC Monitor" cmd /k "title SOC Monitor && python soc_monitor.py && pause"

REM Wait briefly
timeout /t 2 /nobreak >nul

REM Start HTTP server
echo [3/3] Starting Dashboard Server...
start "SOC Server" cmd /k "title Dashboard Server && python server.py && pause"

REM Wait for server
timeout /t 2 /nobreak >nul

REM Open browser
echo.
echo [*] Opening Dashboard...
start http://localhost:8000/dashboard.html

echo.
echo ============================================
echo   ALL COMPONENTS STARTED SUCCESSFULLY!
echo ============================================
echo.
echo   Log Generator - Creating security events
echo   SOC Monitor   - Detecting threats
echo   Dashboard     - http://localhost:8000/dashboard.html
echo.
echo   Close windows to stop the system
echo ============================================
echo.
pause