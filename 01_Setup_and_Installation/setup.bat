@echo off
REM Agentic AI Workshop - Automated Setup Script for Windows
REM Sessions 11 & 12

echo ==================================
echo Agentic AI Workshop Setup (Windows)
echo ==================================
echo.

REM Step 1: Check Python
echo Step 1: Checking Python installation...
python --version >nul 2>&1
if %ERRORLEVEL% EQU 0 (
    echo [OK] Python found
    python --version
) else (
    echo [ERROR] Python not found. Please install Python 3.8 or higher.
    echo Download from: https://www.python.org/downloads/
    pause
    exit /b 1
)

REM Step 2: Create virtual environment
echo.
echo Step 2: Creating virtual environment...
if exist "agentic_ai_env" (
    echo [SKIP] Virtual environment already exists
) else (
    python -m venv agentic_ai_env
    echo [OK] Virtual environment created
)

REM Step 3: Install Python dependencies
echo.
echo Step 3: Installing Python dependencies...
call agentic_ai_env\Scripts\activate.bat

REM Upgrade pip
python -m pip install --upgrade pip >nul 2>&1

REM Install from requirements.txt
if exist "01_Setup_and_Installation\requirements.txt" (
    pip install -r 01_Setup_and_Installation\requirements.txt
    echo [OK] Python packages installed
) else (
    echo [WARN] requirements.txt not found, installing packages individually...
    pip install langchain==0.1.0 langchain-community==0.0.13 ollama==0.1.6 python-dotenv==1.0.0 duckduckgo-search==4.1.1 wikipedia==1.4.0
    echo [OK] Python packages installed
)

REM Step 4: Check Ollama installation
echo.
echo Step 4: Checking Ollama installation...
where ollama >nul 2>&1
if %ERRORLEVEL% EQU 0 (
    echo [OK] Ollama found
    ollama --version

    REM Check if Llama 3.2 model is downloaded
    echo.
    echo Step 5: Checking Llama 3.2 model...
    ollama list | findstr /C:"llama3.2" >nul 2>&1
    if %ERRORLEVEL% EQU 0 (
        echo [OK] Llama 3.2 model found
    ) else (
        echo [WARN] Llama 3.2 model not found. Downloading (~4.7GB^)...
        echo This may take several minutes...
        ollama pull llama3.2
        echo [OK] Llama 3.2 model downloaded
    )
) else (
    echo [ERROR] Ollama not found
    echo.
    echo ================================================
    echo MANUAL INSTALLATION REQUIRED:
    echo ================================================
    echo.
    echo Please install Ollama manually:
    echo 1. Visit: https://ollama.ai
    echo 2. Download the Windows installer
    echo 3. Install Ollama (takes ~2 minutes^)
    echo 4. Re-run this script
    echo.
    echo After installing Ollama, run:
    echo   ollama serve           (Start server^)
    echo   ollama pull llama3.2   (Download model^)
    echo   setup.bat              (Re-run this script^)
    echo.
    pause
    exit /b 1
)

REM Step 6: Test installation
echo.
echo Step 6: Testing installation...
python -c "from langchain_community.llms import Ollama; print('[OK] LangChain integration works')" 2>nul
if %ERRORLEVEL% EQU 0 (
    echo [OK] Python packages work correctly
) else (
    echo [WARN] Python package test had issues
)

REM Final summary
echo.
echo ==================================
echo Setup Complete!
echo ==================================
echo.
echo Next steps:
echo 1. Activate the virtual environment:
echo    agentic_ai_env\Scripts\activate.bat
echo.
echo 2. Test your setup:
echo    ollama run llama3.2 "Hello! What is agentic AI?"
echo.
echo 3. Run Session 11 examples:
echo    cd 02_Session_11_Materials\Workshop_Code
echo    python 01_simple_agent.py
echo.
echo 4. Run Session 12 workshops:
echo    cd 03_Session_12_Materials\Workshop_Code
echo    python workshop1_admission_system.py
echo.
echo Happy Building!
echo.
pause
