#!/usr/bin/env python3
"""
Agentic AI Workshop - Setup Verification Script
Checks that all dependencies are properly installed
"""

import sys
import subprocess
import urllib.request
import json

# Colors for terminal output
GREEN = '\033[0;32m'
YELLOW = '\033[1;33m'
RED = '\033[0;31m'
BLUE = '\033[0;34m'
NC = '\033[0m'  # No Color


def print_header(text):
    """Print a formatted header"""
    print(f"\n{BLUE}{'=' * 50}{NC}")
    print(f"{BLUE}{text}{NC}")
    print(f"{BLUE}{'=' * 50}{NC}\n")


def check_python_version():
    """Check Python version"""
    print("Checking Python version...")
    version = sys.version_info
    if version.major == 3 and version.minor >= 8:
        print(f"{GREEN}✓ Python {version.major}.{version.minor}.{version.micro} - OK{NC}")
        return True
    else:
        print(f"{RED}✗ Python 3.8+ required. Found: {version.major}.{version.minor}.{version.micro}{NC}")
        return False


def check_package(package_name, import_name=None):
    """Check if a Python package is installed"""
    if import_name is None:
        import_name = package_name.replace('-', '_')

    try:
        __import__(import_name)
        print(f"{GREEN}✓ {package_name} - OK{NC}")
        return True
    except ImportError:
        print(f"{RED}✗ {package_name} - NOT FOUND{NC}")
        return False


def check_ollama_installation():
    """Check if Ollama is installed"""
    print("\nChecking Ollama installation...")
    try:
        result = subprocess.run(['which', 'ollama'],
                               capture_output=True,
                               text=True,
                               check=False)
        if result.returncode == 0:
            print(f"{GREEN}✓ Ollama - INSTALLED{NC}")
            return True
        else:
            print(f"{RED}✗ Ollama - NOT FOUND{NC}")
            print(f"{YELLOW}  Install from: https://ollama.ai{NC}")
            return False
    except Exception as e:
        print(f"{RED}✗ Error checking Ollama: {e}{NC}")
        return False


def check_ollama_server():
    """Check if Ollama server is running"""
    print("\nChecking Ollama server...")
    try:
        with urllib.request.urlopen('http://localhost:11434/api/version', timeout=2) as response:
            data = json.loads(response.read().decode())
            print(f"{GREEN}✓ Ollama server - RUNNING{NC}")
            print(f"  Version: {data.get('version', 'unknown')}")
            return True
    except Exception:
        print(f"{YELLOW}! Ollama server - NOT RUNNING{NC}")
        print(f"{YELLOW}  Start with: ollama serve{NC}")
        return False


def check_llama_model():
    """Check if Llama 3.2 model is downloaded"""
    print("\nChecking Llama 3.2 model...")
    try:
        result = subprocess.run(['ollama', 'list'],
                               capture_output=True,
                               text=True,
                               check=False)
        if 'llama3.2' in result.stdout:
            print(f"{GREEN}✓ Llama 3.2 model - DOWNLOADED{NC}")
            return True
        else:
            print(f"{RED}✗ Llama 3.2 model - NOT FOUND{NC}")
            print(f"{YELLOW}  Download with: ollama pull llama3.2{NC}")
            return False
    except Exception as e:
        print(f"{RED}✗ Error checking model: {e}{NC}")
        return False


def test_ollama_integration():
    """Test Ollama integration with LangChain"""
    print("\nTesting Ollama + LangChain integration...")
    try:
        from langchain_community.llms import Ollama
        llm = Ollama(model="llama3.2")
        response = llm.invoke("Say 'Hello' in one word.")
        print(f"{GREEN}✓ Integration test - PASSED{NC}")
        print(f"  Response: {response[:50]}...")
        return True
    except Exception as e:
        print(f"{RED}✗ Integration test - FAILED{NC}")
        print(f"  Error: {str(e)[:100]}")
        return False


def main():
    """Run all verification checks"""
    print_header("🔍 Agentic AI Workshop - Setup Verification")

    results = []

    # Python version
    results.append(check_python_version())

    # Python packages
    print("\nChecking Python packages...")
    packages = [
        ('langchain', 'langchain'),
        ('langchain-community', 'langchain_community'),
        ('ollama', 'ollama'),
        ('python-dotenv', 'dotenv'),
        ('duckduckgo-search', 'duckduckgo_search'),
        ('wikipedia', 'wikipedia'),
    ]

    for package, import_name in packages:
        results.append(check_package(package, import_name))

    # Ollama checks
    ollama_installed = check_ollama_installation()
    results.append(ollama_installed)

    if ollama_installed:
        ollama_running = check_ollama_server()
        results.append(ollama_running)

        model_downloaded = check_llama_model()
        results.append(model_downloaded)

        # Only test integration if server is running and model is downloaded
        if ollama_running and model_downloaded:
            results.append(test_ollama_integration())

    # Summary
    print_header("📊 Verification Summary")

    total_checks = len(results)
    passed_checks = sum(results)

    if passed_checks == total_checks:
        print(f"{GREEN}✅ All checks passed! ({passed_checks}/{total_checks}){NC}")
        print(f"\n{GREEN}You're ready to start the workshop!{NC}\n")
        print("Next steps:")
        print("1. cd 02_Session_11_Materials/Workshop_Code")
        print("2. python 01_simple_agent.py")
        return 0
    else:
        print(f"{YELLOW}⚠️  Some checks failed ({passed_checks}/{total_checks} passed){NC}\n")
        print("Please fix the issues above before starting the workshop.")
        print("\nQuick fixes:")
        print("- Install missing packages: pip install -r 01_Setup_and_Installation/requirements.txt")
        print("- Install Ollama: https://ollama.ai")
        print("- Start Ollama server: ollama serve")
        print("- Download model: ollama pull llama3.2")
        return 1


if __name__ == "__main__":
    sys.exit(main())
