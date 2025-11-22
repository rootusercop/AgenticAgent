"""
Session 11 - FINAL Complete Agent
Combining Everything: Tools + Memory + Custom System Prompt

What this demonstrates:
- Production-ready agent template
- Meta's Llama 3.2 with full capabilities
- Multiple tools, memory, error handling
- This is your starting template for real projects!
"""

# Suppress urllib3 NotOpenSSLWarning on macOS
import warnings
warnings.filterwarnings('ignore', message='.*OpenSSL.*')

from langchain.agents import initialize_agent, AgentType
from langchain.memory import ConversationBufferMemory
from langchain_community.llms import Ollama
from langchain_community.tools import DuckDuckGoSearchRun, WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.tools import Tool
import re
import time

# ANSI color codes for better visibility on white backgrounds
class Colors:
    BLUE = '\033[94m'      # Blue - for info
    CYAN = '\033[96m'      # Cyan - for success/checkmarks
    MAGENTA = '\033[95m'   # Magenta - for headers
    RED = '\033[91m'       # Red - for errors
    BOLD = '\033[1m'       # Bold text
    RESET = '\033[0m'      # Reset to default

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

def calculator(expression: str) -> str:
    """Custom calculator tool"""
    try:
        # Remove any surrounding quotes that the LLM might add
        expression = expression.strip().strip("'\"")

        if not re.match(r'^[0-9+\-*/().\s]+$', expression):
            return f"{Colors.RED}Error: Invalid expression{Colors.RESET}"
        result = eval(expression, {"__builtins__": {}}, {})
        return f"{Colors.CYAN}The result is: {result}{Colors.RESET}"
    except Exception as e:
        return f"{Colors.RED}Error: {str(e)}{Colors.RESET}"


print("=" * 70)
print(" " * 15 + "SESSION 11 - FINAL COMPLETE AGENT")
print("=" * 70)
print("\n🚀 This is your production-ready agent template!")
print("   Using: Meta's Llama 3.2 via Ollama")
print("   Features: Multiple tools + Memory + Custom prompt")
print("\n" + "-" * 70)

# Step 1: Initialize Llama 3.2
print(f"\n{Colors.BLUE}[1/6] Initializing Meta's Llama 3.2 via Ollama...{Colors.RESET}")
llm = Ollama(
    model="llama3.2",  # Meta's open-source model
    temperature=0.7
)
print(f"{Colors.CYAN}     ✓ Llama 3.2 8B model ready{Colors.RESET}")

# Step 2: Initialize memory
print(f"\n{Colors.BLUE}[2/6] Setting up conversation memory...{Colors.RESET}")
memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True
)
print(f"{Colors.CYAN}     ✓ Memory buffer initialized{Colors.RESET}")

# Step 3: Initialize all tools
print(f"\n{Colors.BLUE}[3/6] Configuring tools...{Colors.RESET}")
search_tool = Tool(
    name="duckduckgo_search",
    func=safe_duckduckgo_search,
    description="A search engine. Useful for when you need to answer questions about current events, facts, or general knowledge. Input should be a search query."
)
print(f"{Colors.CYAN}     ✓ DuckDuckGo search tool (with rate limit handling){Colors.RESET}")

wikipedia_tool = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())
print(f"{Colors.CYAN}     ✓ Wikipedia tool{Colors.RESET}")

calculator_tool = Tool(
    name="Calculator",
    func=calculator,
    description="For mathematical calculations. Input should be a valid mathematical expression WITHOUT quotes. Only use numbers and operators (+, -, *, /, parentheses, decimal points)."
)
print(f"{Colors.CYAN}     ✓ Calculator tool (custom){Colors.RESET}")

tools = [search_tool, wikipedia_tool, calculator_tool]
print(f"\n{Colors.BLUE}     Total tools available: {len(tools)}{Colors.RESET}")

# Step 4: Create custom system prompt
print(f"\n{Colors.BLUE}[4/6] Creating custom system prompt...{Colors.RESET}")
system_message = """You are an expert AI assistant for the AICTE ATAL Faculty Development Program on Agentic AI.

Your role and personality:
- Help faculty understand agentic AI concepts clearly
- Provide educational responses with practical examples
- Be encouraging, patient, and supportive
- You have memory of the entire conversation

CRITICAL: When to use tools vs. memory:
1. PERSONAL INFO (name, interests, preferences): Just acknowledge warmly. DO NOT use tools.
2. RECALL QUESTIONS about previous conversation: Answer from memory. DO NOT use tools.
3. MATH CALCULATIONS: Use Calculator tool
4. CURRENT EVENTS/NEWS: Use DuckDuckGo search
5. HISTORICAL FACTS/ENCYCLOPEDIA: Use Wikipedia
6. GENERAL KNOWLEDGE: Answer directly without tools

Examples:
- "My name is Sarah" → Just say: "Nice to meet you, Sarah!" (NO TOOLS)
- "What is my name?" → Answer: "Your name is Sarah" (USE MEMORY, NO TOOLS)
- "I like AI" → Just say: "That's great!" (NO TOOLS)
- "What is 25 * 67?" → Use Calculator
- "Latest AI news 2025?" → Use DuckDuckGo
- "Who invented the computer?" → Use Wikipedia

Always be helpful, accurate, and educational."""
print(f"{Colors.CYAN}     ✓ Custom system prompt configured{Colors.RESET}")

# Step 5: Create the complete agent
print(f"\n{Colors.BLUE}[5/6] Assembling the complete agent...{Colors.RESET}")
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
    memory=memory,
    verbose=True,  # Shows reasoning process
    agent_kwargs={"system_message": system_message},
    max_iterations=5,  # Prevent infinite loops
    early_stopping_method="generate",
    handle_parsing_errors=True
)
print(f"{Colors.CYAN}     ✓ Agent fully assembled and ready!{Colors.RESET}")

# Step 6: Ready!
print(f"\n{Colors.BLUE}[6/6] Final checks...{Colors.RESET}")
print(f"{Colors.CYAN}     ✓ All systems operational{Colors.RESET}")

print("\n" + "=" * 70)
print(" " * 20 + "🎉 AGENT IS READY! 🎉")
print("=" * 70)

print("""
WHAT YOU CAN ASK:

📚 Knowledge Questions:
   - "What is agentic AI?"
   - "Explain the ReAct pattern"

🔍 Current Information (uses DuckDuckGo):
   - "What are the latest AI developments in 2025?"
   - "Current trends in large language models"

📖 Encyclopedia Queries (uses Wikipedia):
   - "Who invented the transformer architecture?"
   - "What is the history of artificial intelligence?"

🔢 Calculations (uses Calculator):
   - "What is 1,234 multiplied by 567?"
   - "Calculate 15% of 50,000"

💬 Conversational Memory:
   - Tell me your name and I'll remember it
   - Ask me to recall what we discussed earlier

SPECIAL COMMANDS:
   - 'memory' → View conversation history
   - 'quit'   → Exit

Try me out! Ask anything!
""")
print("=" * 70 + "\n")

# Interactive loop
conversation_count = 0

while True:
    try:
        user_input = input("You: ")

        if user_input.lower() in ['quit', 'exit', 'q']:
            print("\n" + "=" * 70)
            print(" " * 25 + "SESSION ENDED")
            print("=" * 70)
            print("\n📊 Session Statistics:")
            print(f"   - Total turns: {conversation_count}")
            print(f"   - Tools available: {len(tools)}")
            print(f"   - Model used: Llama 3.2 8B (Meta)")
            print("\n💾 Conversation saved in memory")
            print("\nThank you for using the Complete Agent! 👋\n")
            break

        if user_input.lower() == 'memory':
            print("\n" + "=" * 70)
            print(f"{Colors.MAGENTA}{Colors.BOLD}" + " " * 20 + f"CONVERSATION HISTORY{Colors.RESET}")
            print("=" * 70)
            if memory.buffer:
                print(f"{Colors.BLUE}{memory.buffer}{Colors.RESET}")
            else:
                print(f"{Colors.BLUE}No conversation yet{Colors.RESET}")
            print("=" * 70 + "\n")
            continue

        if not user_input.strip():
            continue

        conversation_count += 1

        print("\n" + "=" * 70)
        print(f"{Colors.MAGENTA}{Colors.BOLD} Turn {conversation_count} - Agent Processing...{Colors.RESET}")
        print("=" * 70)

        response = agent.run(user_input)

        print("\n" + "=" * 70)
        print(f"{Colors.MAGENTA}{Colors.BOLD} FINAL RESPONSE{Colors.RESET}")
        print("=" * 70)
        print(f"\n{Colors.BLUE}{response}{Colors.RESET}\n")
        print("-" * 70 + "\n")

    except KeyboardInterrupt:
        print("\n\nExiting on user interrupt...")
        break
    except Exception as e:
        print(f"\n{Colors.RED}❌ Error occurred: {str(e)}{Colors.RESET}")
        print("Please try again.\n")


print("\n" + "=" * 70)
print(" " * 15 + "💡 KEY TAKEAWAYS FROM SESSION 11 💡")
print("=" * 70)
print("""
You've learned how to build:
✓ Simple conversational agents with Llama 3.2
✓ Agents with external tools (search, Wikipedia)
✓ Custom tools for specific tasks
✓ Agents with conversation memory
✓ Complete production-ready agent systems

This agent architecture can be adapted for:
- Student Q&A systems
- Research assistants
- Customer support bots
- Educational tutors
- Code review agents
- And much more!

Next in Session 12: Multi-agent systems for complex workflows!
""")
print("=" * 70 + "\n")
