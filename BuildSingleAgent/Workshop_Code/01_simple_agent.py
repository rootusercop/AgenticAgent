"""
Session 11 - Workshop Example 1
Simple Conversational Agent with Llama 3.2 via Ollama

What this demonstrates:
- Using Meta's Llama 3.2 model through Ollama
- Basic prompt templates
- Simple LLM interaction
"""

# Suppress urllib3 NotOpenSSLWarning on macOS
import warnings
warnings.filterwarnings('ignore', message='.*OpenSSL.*')

from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate

# ANSI color codes for better visibility on white backgrounds
class Colors:
    BLUE = '\033[94m'      # Blue - for info
    CYAN = '\033[96m'      # Cyan - for success/checkmarks
    MAGENTA = '\033[95m'   # Magenta - for headers
    RED = '\033[91m'       # Red - for errors
    BOLD = '\033[1m'       # Bold text
    RESET = '\033[0m'      # Reset to default

print("=" * 60)
print("SESSION 11 - EXAMPLE 1: Simple Conversational Agent")
print("=" * 60)
print("\nUsing: Meta's Llama 3.2 8B model via Ollama")
print("-" * 60)

# Step 1: Initialize Llama 3.2 through Ollama
print(f"\n{Colors.BLUE}[1/3] Connecting to Llama 3.2 via Ollama...{Colors.RESET}")
llm = Ollama(
    model="llama3.2",  # Meta's Llama 3.2 model
    temperature=0.7
)
print(f"{Colors.CYAN}✓ Connected to Llama 3.2{Colors.RESET}")

# Step 2: Create prompt template
print(f"\n{Colors.BLUE}[2/3] Creating prompt template...{Colors.RESET}")
template = """You are a helpful AI assistant specializing in agentic AI.

Question: {question}

Answer:"""

prompt = PromptTemplate(
    template=template,
    input_variables=["question"]
)
print(f"{Colors.CYAN}✓ Prompt template created{Colors.RESET}")

# Step 3: Create chain
print(f"\n{Colors.BLUE}[3/3] Creating LLM chain...{Colors.RESET}")
chain = prompt | llm
print(f"{Colors.CYAN}✓ Chain ready{Colors.RESET}")

print("\n" + "=" * 60)
print("Agent is ready! Type 'quit' to exit")
print("=" * 60 + "\n")

# Interactive loop
while True:
    user_input = input("You: ")

    if user_input.lower() in ['quit', 'exit', 'q']:
        print("\nGoodbye! 👋\n")
        break

    if not user_input.strip():
        continue

    try:
        print(f"\n{Colors.MAGENTA}🤖 Agent (thinking with Llama 3.2)...{Colors.RESET}\n")
        response = chain.invoke({"question": user_input})
        print(f"{Colors.BLUE}Agent: {response}{Colors.RESET}\n")
        print("-" * 60 + "\n")
    except Exception as e:
        print(f"{Colors.RED}❌ Error: {str(e)}{Colors.RESET}\n")
        print("Please try again.\n")


