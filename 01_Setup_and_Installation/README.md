# Setup and Installation Guide

## 🚀 Quick Start

### Automated Setup (Recommended)

**Mac/Linux:**
```bash
cd 01_Setup_and_Installation
./setup.sh
```

**Windows:**
```cmd
cd 01_Setup_and_Installation
setup.bat
```

### Verify Setup

After installation, verify everything works:

```bash
python verify_setup.py
```

This will check:
- ✅ Python version (3.8+)
- ✅ All required packages
- ✅ Ollama installation
- ✅ Ollama server status
- ✅ Llama 3.2 model
- ✅ Integration test

---

## 📋 What Gets Installed

### Python Packages

All packages are listed in `requirements.txt`:

**Core Framework:**
- `langchain==0.1.0` - Agent framework
- `langchain-community==0.0.13` - Community integrations
- `ollama==0.1.6` - Ollama Python client

**Tools:**
- `duckduckgo-search==4.1.1` - Web search capability
- `wikipedia==1.4.0` - Wikipedia integration

**Utilities:**
- `python-dotenv==1.0.0` - Environment variable management

**Optional (for production):**
- `redis==5.0.1` - Caching
- `psycopg2-binary==2.9.9` - PostgreSQL
- `fastapi==0.109.0` - API framework
- `uvicorn==0.27.0` - ASGI server
- `pytest==7.4.3` - Testing

### Ollama + Llama 3.2

**Ollama** is a tool that makes it easy to run large language models locally:
- Download: https://ollama.ai
- Size: ~500MB
- Platforms: Mac, Windows, Linux

**Llama 3.2** is Meta's open-source language model:
- Model: llama3.2 (8B parameters)
- Size: ~4.7GB
- Install: `ollama pull llama3.2`

---

## 🔧 Manual Installation

If the automated setup doesn't work, follow these steps:

### 1. Install Python 3.8+

**Mac:**
```bash
brew install python3
```

**Windows:**
- Download from https://www.python.org/downloads/
- During installation, check "Add Python to PATH"

**Linux (Ubuntu/Debian):**
```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
```

### 2. Create Virtual Environment

```bash
# Create virtual environment
python3 -m venv agentic_ai_env

# Activate it
# Mac/Linux:
source agentic_ai_env/bin/activate
# Windows:
agentic_ai_env\Scripts\activate
```

### 3. Install Python Packages

```bash
# Option 1: Install from requirements.txt (recommended)
pip install -r requirements.txt

# Option 2: Install individually
pip install langchain==0.1.0
pip install langchain-community==0.0.13
pip install ollama==0.1.6
pip install python-dotenv==1.0.0
pip install duckduckgo-search==4.1.1
pip install wikipedia==1.4.0
```

### 4. Install Ollama

**All Platforms:**
1. Visit https://ollama.ai
2. Download installer for your OS
3. Run installer (takes ~2 minutes)

**Verify installation:**
```bash
ollama --version
```

### 5. Download Llama 3.2 Model

```bash
# This downloads ~4.7GB
ollama pull llama3.2

# Verify
ollama list
# Should show: llama3.2
```

### 6. Start Ollama Server

```bash
# Start the server (keep this running)
ollama serve

# By default runs on: http://localhost:11434
```

### 7. Test Installation

**Test Ollama:**
```bash
ollama run llama3.2 "Hello! What is agentic AI?"
```

**Test Python integration:**
```bash
python -c "from langchain_community.llms import Ollama; print('✓ Success!')"
```

**Run full verification:**
```bash
python verify_setup.py
```

---

## 🐛 Troubleshooting

### Problem: Python not found

**Solution:**
```bash
# Check if Python is installed
python3 --version

# If not found, install Python 3.8+
# Mac: brew install python3
# Windows: https://www.python.org/downloads/
# Linux: sudo apt install python3
```

### Problem: pip not found

**Solution:**
```bash
# Mac/Linux
python3 -m ensurepip --upgrade

# Windows (run as administrator)
python -m ensurepip --upgrade
```

### Problem: "Connection refused" or "Can't connect to Ollama"

**Solution:**
```bash
# Make sure Ollama server is running
ollama serve

# Check if it's listening
curl http://localhost:11434/api/version

# On Windows, use:
# curl.exe http://localhost:11434/api/version
```

### Problem: "Model 'llama3.2' not found"

**Solution:**
```bash
# Pull the model
ollama pull llama3.2

# Verify it's downloaded
ollama list
```

### Problem: "Out of memory" or slow responses

**Solution:**
- Llama 3.2 8B needs ~8GB RAM
- Close other applications
- Use a smaller model:
  ```bash
  ollama pull llama3.2:1b  # 1B parameter model
  ```

### Problem: Import errors (ModuleNotFoundError)

**Solution:**
```bash
# Make sure virtual environment is activated
source agentic_ai_env/bin/activate  # Mac/Linux
agentic_ai_env\Scripts\activate     # Windows

# Reinstall packages
pip install --upgrade -r requirements.txt
```

### Problem: urllib3 SSL warning

**Solution:**
This is just a warning and won't affect functionality. To fix:
```bash
pip install --upgrade urllib3 certifi
```

### Problem: Setup script permission denied (Mac/Linux)

**Solution:**
```bash
chmod +x setup.sh
./setup.sh
```

---

## 📊 System Requirements

### Minimum Requirements

- **OS:** macOS 10.15+, Windows 10+, or Linux (Ubuntu 20.04+)
- **Python:** 3.8 or higher
- **RAM:** 8GB (for Llama 3.2 8B)
- **Disk Space:** 10GB free (5GB for model, 5GB for dependencies)
- **Internet:** Required for initial download (~5GB)

### Recommended Requirements

- **RAM:** 16GB or more
- **CPU:** 4+ cores
- **Disk Space:** 20GB free
- **GPU:** Optional (speeds up inference, but not required)

---

## 🎯 Next Steps

After successful installation:

### 1. Test Your Setup
```bash
python verify_setup.py
```

### 2. Run Session 11 Examples
```bash
cd ../02_Session_11_Materials/Workshop_Code
python 01_simple_agent.py
```

### 3. Run Session 12 Workshops
```bash
cd ../03_Session_12_Materials/Workshop_Code
python workshop1_admission_system.py
```

---

## 📞 Getting Help

If you're still having issues:

1. **Check the verification output:**
   ```bash
   python verify_setup.py
   ```

2. **Review the main documentation:**
   - `Setup_Guide_and_Installation.md`
   - Main `README.md` in project root

3. **Check Ollama status:**
   ```bash
   ollama list
   curl http://localhost:11434/api/version
   ```

4. **Verify Python packages:**
   ```bash
   pip list | grep langchain
   pip list | grep ollama
   ```

---

## 🔄 Updating

To update to the latest versions:

```bash
# Activate virtual environment
source agentic_ai_env/bin/activate  # Mac/Linux
agentic_ai_env\Scripts\activate     # Windows

# Update Python packages
pip install --upgrade -r requirements.txt

# Update Ollama models
ollama pull llama3.2
```

---

## 🗑️ Uninstalling

To remove everything:

```bash
# Remove virtual environment
rm -rf agentic_ai_env  # Mac/Linux
rmdir /s agentic_ai_env  # Windows

# Uninstall Ollama
# Mac: Drag Ollama from Applications to Trash
# Windows: Use "Add or Remove Programs"
# Linux: Follow Ollama uninstall instructions

# Remove Ollama models (optional)
rm -rf ~/.ollama  # Mac/Linux
rmdir /s %USERPROFILE%\.ollama  # Windows
```

---

Happy Building! 🚀
