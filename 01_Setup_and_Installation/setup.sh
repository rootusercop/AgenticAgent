#!/bin/bash

# Agentic AI Workshop - Automated Setup Script
# Sessions 11 & 12

set -e  # Exit on error

echo "=================================="
echo "🚀 Agentic AI Workshop Setup"
echo "=================================="
echo ""

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Step 1: Check Python
echo "Step 1: Checking Python installation..."
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version)
    echo -e "${GREEN}✓ Python found: $PYTHON_VERSION${NC}"
else
    echo -e "${RED}✗ Python 3 not found. Please install Python 3.8 or higher.${NC}"
    exit 1
fi

# Step 2: Create virtual environment
echo ""
echo "Step 2: Creating virtual environment..."
if [ -d "agentic_ai_env" ]; then
    echo -e "${YELLOW}! Virtual environment already exists. Skipping...${NC}"
else
    python3 -m venv agentic_ai_env
    echo -e "${GREEN}✓ Virtual environment created${NC}"
fi

# Step 3: Install Python dependencies
echo ""
echo "Step 3: Installing Python dependencies..."
source agentic_ai_env/bin/activate

# Upgrade pip first
pip install --upgrade pip > /dev/null 2>&1

# Install from requirements.txt
if [ -f "01_Setup_and_Installation/requirements.txt" ]; then
    pip install -r 01_Setup_and_Installation/requirements.txt
    echo -e "${GREEN}✓ Python packages installed${NC}"
else
    echo -e "${YELLOW}! requirements.txt not found, installing packages individually...${NC}"
    pip install langchain==0.1.0 langchain-community==0.0.13 ollama==0.1.6 python-dotenv==1.0.0 duckduckgo-search==4.1.1 wikipedia==1.4.0
    echo -e "${GREEN}✓ Python packages installed${NC}"
fi

# Step 4: Check Ollama installation
echo ""
echo "Step 4: Checking Ollama installation..."
if command -v ollama &> /dev/null; then
    OLLAMA_VERSION=$(ollama --version 2>&1 | head -n 1)
    echo -e "${GREEN}✓ Ollama found: $OLLAMA_VERSION${NC}"

    # Check if Ollama server is running
    echo ""
    echo "Step 5: Checking Ollama server..."
    if curl -s http://localhost:11434/api/version > /dev/null 2>&1; then
        echo -e "${GREEN}✓ Ollama server is running${NC}"
    else
        echo -e "${YELLOW}! Ollama server not running. Starting it...${NC}"
        echo -e "${YELLOW}  (Keep this terminal open or run 'ollama serve' in another terminal)${NC}"
        ollama serve &
        sleep 3
        if curl -s http://localhost:11434/api/version > /dev/null 2>&1; then
            echo -e "${GREEN}✓ Ollama server started${NC}"
        else
            echo -e "${RED}✗ Could not start Ollama server${NC}"
            echo -e "${YELLOW}  Please run 'ollama serve' manually in another terminal${NC}"
        fi
    fi

    # Check if Llama 3.2 model is downloaded
    echo ""
    echo "Step 6: Checking Llama 3.2 model..."
    if ollama list | grep -q "llama3.2"; then
        echo -e "${GREEN}✓ Llama 3.2 model found${NC}"
    else
        echo -e "${YELLOW}! Llama 3.2 model not found. Downloading (~4.7GB)...${NC}"
        echo -e "${YELLOW}  This may take several minutes depending on your internet speed.${NC}"
        ollama pull llama3.2
        echo -e "${GREEN}✓ Llama 3.2 model downloaded${NC}"
    fi
else
    echo -e "${RED}✗ Ollama not found${NC}"
    echo ""
    echo -e "${YELLOW}================================================${NC}"
    echo -e "${YELLOW}MANUAL INSTALLATION REQUIRED:${NC}"
    echo -e "${YELLOW}================================================${NC}"
    echo ""
    echo "Please install Ollama manually:"
    echo "1. Visit: https://ollama.ai"
    echo "2. Download the installer for your OS"
    echo "3. Install Ollama (takes ~2 minutes)"
    echo "4. Re-run this script"
    echo ""
    echo -e "${YELLOW}After installing Ollama, run these commands:${NC}"
    echo "  ollama serve                    # Start server"
    echo "  ollama pull llama3.2           # Download model"
    echo "  ./01_Setup_and_Installation/setup.sh  # Re-run this script"
    echo ""
    exit 1
fi

# Step 7: Test installation
echo ""
echo "Step 7: Testing installation..."
python3 -c "from langchain_community.llms import Ollama; print('✓ LangChain integration works')" 2>/dev/null && echo -e "${GREEN}✓ Python packages work correctly${NC}" || echo -e "${RED}✗ Python package test failed${NC}"

# Final summary
echo ""
echo "=================================="
echo -e "${GREEN}✅ Setup Complete!${NC}"
echo "=================================="
echo ""
echo "Next steps:"
echo "1. Activate the virtual environment:"
echo "   source agentic_ai_env/bin/activate"
echo ""
echo "2. Test your setup:"
echo "   ollama run llama3.2 'Hello! What is agentic AI?'"
echo ""
echo "3. Run Session 11 examples:"
echo "   cd 02_Session_11_Materials/Workshop_Code"
echo "   python 01_simple_agent.py"
echo ""
echo "4. Run Session 12 workshops:"
echo "   cd 03_Session_12_Materials/Workshop_Code"
echo "   python workshop1_admission_system.py"
echo ""
echo "Happy Building! 🚀"
echo ""
