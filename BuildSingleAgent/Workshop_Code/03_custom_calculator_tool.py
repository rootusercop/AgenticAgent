"""
Session 11 - Workshop Example 3
Creating Custom Tools

What this demonstrates:
- How to create your own custom tools
- Tool descriptions for Llama 3.2 to understand
- Safe code execution
"""

# Suppress urllib3 NotOpenSSLWarning on macOS
import warnings
warnings.filterwarnings('ignore', message='.*OpenSSL.*')

from langchain.tools import Tool
from langchain.agents import initialize_agent, AgentType
from langchain_community.llms import Ollama
import re

# ANSI color codes for better visibility on white backgrounds
class Colors:
    BLUE = '\033[94m'      # Blue - for info
    CYAN = '\033[96m'      # Cyan - for success/checkmarks
    MAGENTA = '\033[95m'   # Magenta - for headers
    RED = '\033[91m'       # Red - for errors
    BOLD = '\033[1m'       # Bold text
    RESET = '\033[0m'      # Reset to default

def calculator(expression: str) -> str:
    """
    Safely evaluates mathematical expressions.
    This is a CUSTOM TOOL we're creating!
    """
    try:
        # Remove any surrounding quotes that the LLM might add
        expression = expression.strip().strip("'\"")

        # Security: Only allow numbers and basic operators
        if not re.match(r'^[0-9+\-*/().\s]+$', expression):
            return f"{Colors.RED}❌ Error: Invalid characters. Only use numbers and +, -, *, /, (), .{Colors.RESET}"

        # Safe evaluation (no access to dangerous functions)
        result = eval(expression, {"__builtins__": {}}, {})
        return f"{Colors.CYAN}✓ The result is: {result}{Colors.RESET}"

    except ZeroDivisionError:
        return f"{Colors.RED}❌ Error: Cannot divide by zero{Colors.RESET}"
    except Exception as e:
        return f"{Colors.RED}❌ Error: {str(e)}{Colors.RESET}"


print("=" * 60)
print("SESSION 11 - EXAMPLE 3: Custom Calculator Tool")
print("=" * 60)
print("\nCreating a custom tool for Llama 3.2 to use")
print("-" * 60)

# Step 1: Initialize Llama 3.2
print(f"\n{Colors.BLUE}[1/3] Initializing Llama 3.2...{Colors.RESET}")
llm = Ollama(
    model="llama3.2",
    temperature=0  # Use 0 for math - we want deterministic results
)
print(f"{Colors.CYAN}✓ Llama 3.2 ready{Colors.RESET}")

# Step 2: Create custom tool
print(f"\n{Colors.BLUE}[2/3] Creating custom calculator tool...{Colors.RESET}")
calc_tool = Tool(
    name="Calculator",
    func=calculator,
    description="""Useful for mathematical calculations.
    Input should be a valid mathematical expression WITHOUT quotes like:
    - 2 + 2
    - (15 * 67) + 890
    - 100 / 25
    - 2000 * 0.15
    Only use numbers and operators (+, -, *, /, parentheses, decimal points).
    Do NOT include words, quotes, or any other characters - only the mathematical expression."""
)
print(f"{Colors.CYAN}✓ Calculator tool created{Colors.RESET}")
print(f"{Colors.BLUE}   Tool name: {calc_tool.name}{Colors.RESET}")
print(f"{Colors.BLUE}   Tool function: {calc_tool.func.__name__}{Colors.RESET}")

# Step 3: Create agent with custom tool
print(f"\n{Colors.BLUE}[3/3] Creating agent with calculator...{Colors.RESET}")

# Add system message to help the agent understand when to give final answer
system_message = """You are a helpful assistant with access to a Calculator tool.

When answering questions:
1. If it's a math problem, use the Calculator tool ONCE
2. After getting the result from the Calculator, immediately provide your Final Answer
3. Do NOT call the Calculator multiple times for the same calculation

Example:
Question: What is 234 multiplied by 567?
Thought: I need to calculate 234 * 567
Action: Calculator
Action Input: 234 * 567
Observation: The result is: 132678
Thought: I have the answer
Final Answer: 132678"""

agent = initialize_agent(
    tools=[calc_tool],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
    handle_parsing_errors=True,
    max_iterations=5,  # Reduced to stop loops faster
    early_stopping_method="generate",  # Generate final answer if stuck
    agent_kwargs={"prefix": system_message}
)
print(f"{Colors.CYAN}✓ Agent ready{Colors.RESET}")

print("\n" + "=" * 60)
print("Testing Custom Calculator Tool")
print("=" * 60)

# Test queries
test_queries = [
    "What is 234 multiplied by 567?",
    "Calculate (1500 + 2500) divided by 100",
    "What's 15 percent of 2000? (Calculate as 2000 * 0.15)"
]

for i, query in enumerate(test_queries, 1):
    print(f"\n{'=' * 60}")
    print(f"{Colors.MAGENTA}{Colors.BOLD}TEST {i}/3: {query}{Colors.RESET}")
    print("=" * 60)

    try:
        result = agent.run(query)
        print(f"\n{Colors.CYAN}✓ Final Answer: {result}{Colors.RESET}\n")
    except Exception as e:
        print(f"\n{Colors.RED}❌ Error: {str(e)}{Colors.RESET}\n")

    input("Press Enter to continue...")

print("\n" + "=" * 60)
print("Now try your own calculations! Type 'quit' to exit")
print("=" * 60 + "\n")

# Interactive mode
while True:
    user_input = input("You: ")

    if user_input.lower() in ['quit', 'exit', 'q']:
        print("\nGoodbye! 👋\n")
        break

    if not user_input.strip():
        continue

    try:
        result = agent.run(user_input)
        print(f"\n{Colors.CYAN}✓ Answer: {result}{Colors.RESET}\n")
    except Exception as e:
        print(f"\n{Colors.RED}❌ Error: {str(e)}{Colors.RESET}\n")
