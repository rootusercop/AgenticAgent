"""
Session 11 - Workshop Example 2
Agent with Tools (Search & Wikipedia)

What this demonstrates:
- Llama 3.2 using external tools
- ReAct pattern (Reasoning + Acting)
- Tool selection and execution
"""

# Suppress urllib3 NotOpenSSLWarning on macOS
import warnings
warnings.filterwarnings('ignore', message='.*OpenSSL.*')

from langchain.agents import initialize_agent, AgentType
from langchain_community.llms import Ollama
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
import time

# ANSI color codes for better visibility on white backgrounds
class Colors:
    BLUE = '\033[94m'      # Blue - for info
    CYAN = '\033[96m'      # Cyan - for success/checkmarks
    MAGENTA = '\033[95m'   # Magenta - for headers
    RED = '\033[91m'       # Red - for errors
    BOLD = '\033[1m'       # Bold text
    RESET = '\033[0m'      # Reset to default

print("=" * 60)
print("SESSION 11 - EXAMPLE 2: Agent with Tools")
print("=" * 60)
print("\nUsing: Meta's Llama 3.2 + DuckDuckGo + Wikipedia")
print("-" * 60)

# Step 1: Initialize Llama 3.2
print(f"\n{Colors.BLUE}[1/4] Initializing Llama 3.2 via Ollama...{Colors.RESET}")
llm = Ollama(
    model="llama3.2",
    temperature=0.7,
    stop=["Observation:", "\nObservation"]  # Help prevent loops
)
print(f"{Colors.CYAN}✓ Llama 3.2 ready{Colors.RESET}")

# Step 2: Initialize tools with error handling
print(f"\n{Colors.BLUE}[2/4] Setting up tools...{Colors.RESET}")

# Wrapper function for DuckDuckGo with retry and error handling
def safe_duckduckgo_search(query: str) -> str:
    """Wrapper for DuckDuckGo search with rate limit handling."""
    search_tool = DuckDuckGoSearchRun()
    max_retries = 3
    retry_delay = 2

    for attempt in range(max_retries):
        try:
            return search_tool.run(query)
        except Exception as e:
            error_msg = str(e)
            if "Ratelimit" in error_msg or "rate" in error_msg.lower():
                if attempt < max_retries - 1:
                    print(f"\n{Colors.MAGENTA}⚠️  Rate limit hit. Waiting {retry_delay} seconds before retry {attempt + 1}/{max_retries}...{Colors.RESET}")
                    time.sleep(retry_delay)
                    retry_delay *= 2  # Exponential backoff
                else:
                    return f"{Colors.MAGENTA}⚠️  DuckDuckGo search temporarily unavailable due to rate limits. Try using Wikipedia instead, or try again in a few moments.{Colors.RESET}"
            else:
                return f"{Colors.RED}❌ Search error: {error_msg}{Colors.RESET}"
    return "❌ Search failed after multiple attempts."

from langchain.tools import Tool
search = Tool(
    name="duckduckgo_search",
    func=safe_duckduckgo_search,
    description="A search engine. Useful for when you need to answer questions about current events, facts, or general knowledge. Input should be a search query."
)

wikipedia = WikipediaQueryRun(
    api_wrapper=WikipediaAPIWrapper()
)
print(f"{Colors.CYAN}✓ DuckDuckGo search tool ready (with rate limit handling){Colors.RESET}")
print(f"{Colors.CYAN}✓ Wikipedia tool ready{Colors.RESET}")

# Step 3: Create tools list
tools = [search, wikipedia]
print(f"\n{Colors.BLUE}[3/4] Agent has {len(tools)} tools available{Colors.RESET}")

# Step 4: Create agent with ReAct pattern
print(f"\n{Colors.BLUE}[4/4] Creating ReAct agent...{Colors.RESET}")
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,  # Shows the reasoning process!
    handle_parsing_errors=True,
    max_iterations=10  # Prevent infinite loops
)
print(f"{Colors.CYAN}✓ Agent ready with ReAct capabilities{Colors.RESET}")

print("\n" + "=" * 60)
print("Agent with Tools Ready!")
print("=" * 60)
print("\nTry asking:")
print("  - What are the latest developments in agentic AI?")
print("  - Who invented the transformer architecture?")
print("  - What is the population of Mumbai?")
print("\nType 'quit' to exit")
print("=" * 60 + "\n")

# Interactive loop
while True:
    user_input = input("You: ")

    if user_input.lower() in ['quit', 'exit', 'q']:
        print("\nGoodbye! 👋\n")
        break

    if not user_input.strip():
        continue

    print("\n" + "=" * 60)
    print(f"{Colors.MAGENTA}{Colors.BOLD}AGENT THOUGHT PROCESS (ReAct Pattern){Colors.RESET}")
    print("=" * 60)

    try:
        result = agent.run(user_input)
        print("\n" + "=" * 60)
        print(f"{Colors.MAGENTA}{Colors.BOLD}FINAL ANSWER{Colors.RESET}")
        print("=" * 60)
        print(f"\n{Colors.BLUE}{result}{Colors.RESET}\n")
    except Exception as e:
        print(f"\n{Colors.RED}❌ Error: {str(e)}{Colors.RESET}\n")

    print("-" * 60 + "\n")
