"""
Session 11 - Workshop Example 4
Agent with Conversation Memory

What this demonstrates:
- Llama 3.2 remembering conversation history
- ConversationBufferMemory
- Context-aware responses
"""

# Suppress urllib3 NotOpenSSLWarning on macOS
import warnings
warnings.filterwarnings('ignore', message='.*OpenSSL.*')

from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
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
print("SESSION 11 - EXAMPLE 4: Agent with Memory")
print("=" * 60)
print("\nDemonstrating conversation memory with Llama 3.2")
print("-" * 60)

# Step 1: Initialize Llama 3.2
print(f"\n{Colors.BLUE}[1/3] Initializing Llama 3.2...{Colors.RESET}")
llm = Ollama(
    model="llama3.2",
    temperature=0.7
    # Note: stop parameter removed for conversational agent compatibility
)
print(f"{Colors.CYAN}✓ Llama 3.2 ready{Colors.RESET}")

# Step 2: Create memory
print(f"\n{Colors.BLUE}[2/3] Setting up conversation memory...{Colors.RESET}")
memory = ConversationBufferMemory()
print(f"{Colors.CYAN}✓ Memory initialized{Colors.RESET}")
print(f"{Colors.BLUE}   This will store our entire conversation!{Colors.RESET}")

# Step 3: Create conversational chain with memory
print(f"\n{Colors.BLUE}[3/3] Creating conversational chain with memory...{Colors.RESET}")

# Create a custom prompt template
template = """You are a friendly AI assistant having a conversation with a human.
You have memory of the entire conversation, so you can remember what the user told you earlier.

When the user tells you something personal (like their name or interests), simply acknowledge it warmly.
When the user asks you to recall something they told you, use the conversation history to answer.

Current conversation:
{history}
Human: {input}
AI:"""

PROMPT = PromptTemplate(
    input_variables=["history", "input"],
    template=template
)

# Create the conversation chain
conversation = ConversationChain(
    llm=llm,
    memory=memory,
    prompt=PROMPT,
    verbose=False  # Set to False for cleaner output
)
print(f"{Colors.CYAN}✓ Conversational chain ready with memory!{Colors.RESET}")

print("\n" + "=" * 60)
print("Agent with Memory Ready!")
print("=" * 60)
print("\nTry this conversation to see memory in action:")
print("  1. 'My name is [Your Name]'")
print("  2. 'I'm interested in machine learning'")
print("  3. 'What is my name?'  ← Agent remembers!")
print("  4. 'Can you recommend ML resources based on my interest?'")
print("\nType 'quit' to exit, 'memory' to see conversation history")
print("=" * 60 + "\n")

# Interactive loop
conversation_count = 0

while True:
    user_input = input("You: ")

    if user_input.lower() in ['quit', 'exit', 'q']:
        print("\n" + "=" * 60)
        print(f"{Colors.MAGENTA}{Colors.BOLD}FINAL CONVERSATION HISTORY{Colors.RESET}")
        print("=" * 60)
        print(f"{Colors.BLUE}{memory.buffer}{Colors.RESET}")
        print("\nGoodbye! 👋\n")
        break

    if user_input.lower() == 'memory':
        print("\n" + "=" * 60)
        print(f"{Colors.MAGENTA}{Colors.BOLD}CURRENT CONVERSATION HISTORY{Colors.RESET}")
        print("=" * 60)
        print(f"{Colors.BLUE}{memory.buffer if memory.buffer else 'No conversation yet'}{Colors.RESET}")
        print("=" * 60 + "\n")
        continue

    if not user_input.strip():
        continue

    conversation_count += 1
    print(f"\n{Colors.MAGENTA}[Turn {conversation_count}] Agent thinking...{Colors.RESET}\n")

    try:
        response = conversation.predict(input=user_input)
        print(f"\n{Colors.BLUE}Agent: {response}{Colors.RESET}\n")
        print("-" * 60 + "\n")
    except Exception as e:
        print(f"\n{Colors.RED}❌ Error: {str(e)}{Colors.RESET}\n")
