# Agentic AI Workshop Code
## Sessions 11 & 12 - Complete Workshop Materials

---

## 🔑 IMPORTANT CLARIFICATION

### What is Llama? What is Ollama?

**Llama 3.2** = Meta's open-source Large Language Model (the AI brain)
- Developed by Meta (Facebook)
- Available in 8B, 70B, 405B parameter sizes
- Free and open-source
- Excellent for agentic AI applications

**Ollama** = Tool/Server to run Llama locally (the infrastructure)
- Makes it easy to run LLMs on your computer
- Handles model loading, inference, and serving
- Works like a local ChatGPT server
- Free and open-source

**In our workshops, we use BOTH:**
- Llama 3.2 8B (the model) running through Ollama (the server)
- This gives us a powerful local AI without API costs!

---

## 📁 Workshop Structure

```
Session11_Workshop_Code/
├── 01_simple_agent.py              # Basic conversational agent
├── 02_agent_with_tools.py          # Agent with search & Wikipedia
├── 03_custom_calculator_tool.py    # Creating custom tools
├── 04_agent_with_memory.py         # Conversation memory
└── 05_complete_agent_final.py      # Full-featured agent (TEMPLATE)

Session12_Workshop_Code/
├── workshop1_admission_system.py   # Multi-agent admission system
└── workshop2_learning_path_system.py # Adaptive learning system
```

---

## 🚀 Installation & Setup

### ⚡ Quick Start (Automated Setup)

**For Mac/Linux users:**
```bash
# Run the automated setup script
cd 01_Setup_and_Installation
./setup.sh
```

This script will:
- ✅ Check Python installation
- ✅ Create virtual environment
- ✅ Install all Python packages
- ✅ Check for Ollama installation
- ✅ Verify Llama 3.2 model
- ✅ Test everything works

**To verify your setup anytime:**
```bash
python 01_Setup_and_Installation/verify_setup.py
```

---

### 📋 Manual Setup (If Automated Setup Fails)

### Step 1: Install Python Dependencies

```bash
# Create virtual environment (recommended)
python3 -m venv agentic_ai_env

# Activate it
# On Mac/Linux:
source agentic_ai_env/bin/activate
# On Windows:
agentic_ai_env\Scripts\activate

# Install from requirements.txt (recommended)
pip install -r 01_Setup_and_Installation/requirements.txt

# OR install packages individually:
pip install langchain==0.1.0
pip install langchain-community==0.0.13
pip install ollama==0.1.6
pip install python-dotenv==1.0.0
pip install duckduckgo-search==4.1.1
pip install wikipedia==1.4.0
```

### Step 2: Install Ollama

**Download Ollama:**
- Go to https://ollama.ai
- Download for your OS (Mac, Windows, Linux)
- Install (takes 2 minutes)

**Pull Llama 3.2 Model:**
```bash
# This downloads Meta's Llama 3.2 8B model (~4.7GB)
ollama pull llama3.2

# Verify installation
ollama list
# Should show: llama3.2
```

**Start Ollama Server:**
```bash
# Start the server (keep this running in a terminal)
ollama serve

# By default, it runs on http://localhost:11434
```

### Step 3: Test Installation

```bash
# Test Ollama with Llama 3.2
ollama run llama3.2 "Hello! What is agentic AI?"

# Test Python integration
python3 -c "from langchain_community.llms import Ollama; print('✓ Success!')"
```

If both work, you're ready! 🎉

---

## 📚 SESSION 11: Building Simple Agents

### Example 1: Simple Conversational Agent
**File:** `01_simple_agent.py`

**What it teaches:**
- Connecting to Llama 3.2 via Ollama
- Creating prompt templates
- Basic LLM interaction

**Run:**
```bash
cd Session11_Workshop_Code
python 01_simple_agent.py
```

**Try asking:**
- "What is agentic AI?"
- "Explain the ReAct pattern"
- "What are the benefits of open-source LLMs?"

---

### Example 2: Agent with Tools
**File:** `02_agent_with_tools.py`

**What it teaches:**
- Adding DuckDuckGo search capability
- Adding Wikipedia lookup
- ReAct pattern (Reasoning + Acting)
- Tool selection by Llama 3.2

**Run:**
```bash
python 02_agent_with_tools.py
```

**Try asking:**
- "What are the latest developments in agentic AI in 2025?"
- "Who invented the transformer architecture?"
- "What is the population of Mumbai?"

**Watch the agent:**
- Think about what it needs (Thought)
- Choose a tool (Action)
- Get results (Observation)
- Decide what to do next (Thought)
- Answer your question (Final Answer)

---

### Example 3: Custom Calculator Tool
**File:** `03_custom_calculator_tool.py`

**What it teaches:**
- Creating your own custom tools
- Tool descriptions for Llama 3.2
- Safe code execution
- How agents decide which tool to use

**Run:**
```bash
python 03_custom_calculator_tool.py
```

**Try asking:**
- "What is 234 multiplied by 567?"
- "Calculate (1500 + 2500) divided by 100"
- "What's 15 percent of 2000?"

**Key learning:** The agent doesn't know math inherently - it uses the calculator tool!

---

### Example 4: Agent with Memory
**File:** `04_agent_with_memory.py`

**What it teaches:**
- Conversation memory
- Context retention
- Personalized responses

**Run:**
```bash
python 04_agent_with_memory.py
```

**Try this conversation:**
```
You: My name is Nikhil
Agent: Hello Nikhil! Nice to meet you.

You: I'm interested in machine learning
Agent: That's great! ML is fascinating...

You: What is my name?
Agent: Your name is Nikhil.

You: Can you recommend ML resources based on my interest?
Agent: Since you're interested in ML, here are some...
```

**Type 'memory' to see conversation history!**

---

### Example 5: Complete Agent (PRODUCTION TEMPLATE)
**File:** `05_complete_agent_final.py`

**What it teaches:**
- Everything combined!
- Production-ready architecture
- Error handling
- This is your starting template for real projects

**Features:**
- ✅ Llama 3.2 8B via Ollama
- ✅ Multiple tools (search, Wikipedia, calculator)
- ✅ Conversation memory
- ✅ Custom system prompt
- ✅ Error handling
- ✅ Interactive interface

**Run:**
```bash
python 05_complete_agent_final.py
```

**This is your template! Copy and modify for your projects.**

---

## 🏗️ SESSION 12: Multi-Agent Systems

### Workshop 1: College Admission Management System
**File:** `workshop1_admission_system.py`

**Architecture:** Sequential Pipeline

```
Student → Orchestrator → [Agent 1 | Agent 2 | Agent 3 | Agent 4] → Result
```

**Agents:**
1. **Query Handler** - Answers questions (FAQ, program info)
2. **Document Processor** - Extracts data from applications
3. **Eligibility Evaluator** - Determines admission decision
4. **Communication Manager** - Sends personalized emails

**Run:**
```bash
cd Session12_Workshop_Code
python workshop1_admission_system.py
```

**What you'll see:**
- Demo Scenario 1: Student asks about deadlines
- Demo Scenario 2: Complete application processing
  - Document extraction with Llama 3.2
  - Eligibility evaluation
  - Personalized email generation

**Real-world impact:**
- Processing time: 2-3 weeks → 2-3 days
- Staff workload: -80%
- Application completion: 70% → 95%
- Cost savings: $450,000/year for 5,000 applications

**Adapt this for:**
- HR recruitment
- Loan applications
- Grant proposals
- Customer onboarding

---

### Workshop 2: Personalized Learning Path Generator
**File:** `workshop2_learning_path_system.py`

**Architecture:** Sequential with Feedback Loops

```
Assessment → Planning → Content Recommendation → Progress Monitoring → Adaptation
                                                         ↓
                                                    [Feedback Loop]
```

**Agents:**
1. **Skills Assessment** - Tests current level
2. **Learning Path Planner** - Creates 6-month roadmap
3. **Content Recommender** - Daily study plans
4. **Progress Monitor** - Tracks and adapts

**Run:**
```bash
python workshop2_learning_path_system.py
```

**What you'll see:**
- Student profile input
- Skills assessment results
- Complete 6-month personalized learning path
- Daily content recommendations
- Progress tracking simulation

**Real-world impact:**
- Course completion: 40% → 75%
- Student satisfaction: 65% → 90%
- Personalization at scale
- Revenue per student: $200 → $500

**Adapt this for:**
- Corporate training
- Certification prep
- Academic tutoring
- Professional development

---

## 🎯 Key Concepts

### 1. ReAct Pattern (Reasoning + Acting)
How Llama 3.2 decides what to do:

```
1. Thought: "What do I need to know?"
2. Action: "Use Wikipedia tool"
3. Action Input: "transformer architecture"
4. Observation: [Wikipedia results]
5. Thought: "Do I have enough info? Yes!"
6. Final Answer: "The transformer architecture was..."
```

### 2. Tools
External capabilities for agents:
- Web search (DuckDuckGo)
- Knowledge lookup (Wikipedia)
- Calculations (Calculator)
- Custom tools (anything you build!)

### 3. Memory
Types:
- **ConversationBufferMemory** - Stores everything
- **ConversationSummaryMemory** - Summarizes old messages
- **Vector Memory** - For long-term storage

### 4. Multi-Agent Patterns

**Sequential Pipeline:**
```
A → B → C
```
Each agent processes, passes to next

**Parallel Execution:**
```
    → A →
Orch → B → Agg
    → C →
```
Agents work simultaneously

**Hierarchical:**
```
  Manager
   ↓
[W1, W2, W3]
```
Manager coordinates workers

---

## 🐛 Troubleshooting

### Problem: "Connection refused" or "Can't connect to Ollama"
**Solution:**
```bash
# Make sure Ollama is running
ollama serve

# Check if it's listening
curl http://localhost:11434/api/version
```

### Problem: "Model 'llama3.2' not found"
**Solution:**
```bash
# Pull the model
ollama pull llama3.2

# Verify
ollama list
```

### Problem: Agent not using tools
**Solution:**
- Check tool descriptions - they should be clear
- Set `verbose=True` to see agent's reasoning
- Use `temperature=0` for more deterministic behavior

### Problem: "Out of memory" or slow responses
**Solution:**
- Llama 3.2 8B needs ~8GB RAM
- Close other applications
- Use a smaller model: `ollama pull llama3.2:1b`

### Problem: Import errors
**Solution:**
```bash
# Reinstall packages
pip install --upgrade langchain langchain-community ollama
```

---

## 💡 Tips for Your Own Projects

### 1. Start with the Template
Use `05_complete_agent_final.py` as your starting point

### 2. Custom Tools
Pattern:
```python
def your_custom_function(input: str) -> str:
    # Your logic here
    return result

tool = Tool(
    name="YourTool",
    func=your_custom_function,
    description="Clear description of WHEN to use this tool"
)
```

### 3. System Prompts Matter
```python
system_message = """You are [role].

Your personality:
- [trait 1]
- [trait 2]

Guidelines:
- [rule 1]
- [rule 2]
"""
```

### 4. Error Handling
Always use:
```python
try:
    result = agent.run(query)
except Exception as e:
    print(f"Error: {e}")
    # Fallback logic
```

### 5. Testing
Test each component separately:
```python
# Test tool independently
result = tool.run("test input")

# Test LLM
response = llm.invoke("test prompt")

# Then test full agent
```

---

## 📊 Performance Tips

### Speed Optimization
1. **Use smaller models for simple tasks**
   ```bash
   ollama pull llama3.2:1b  # 1B parameter model (faster)
   ```

2. **Cache common queries**
   ```python
   import functools

   @functools.lru_cache(maxsize=100)
   def cached_agent_call(query):
       return agent.run(query)
   ```

3. **Reduce verbosity in production**
   ```python
   agent = initialize_agent(..., verbose=False)
   ```

### Cost Savings
Llama 3.2 8B via Ollama:
- **Cost:** $0 per query (after setup)
- **Setup:** $0-2,000 (depending on hardware)
- **vs GPT-4:** $0.03 per query = $108,000/year for 50K queries

---

## 🎓 Learning Path

### Beginner
1. Run all Session 11 examples in order
2. Modify prompts and see how responses change
3. Create one custom tool

### Intermediate
4. Run Session 12 workshops
5. Understand multi-agent architecture
6. Build a simple multi-agent system for your domain

### Advanced
7. Deploy to production with Docker
8. Add monitoring and logging
9. Implement advanced memory (vector stores)
10. Create a full application

---

## 📚 Additional Resources

### Documentation
- **Ollama:** https://ollama.ai/library
- **Llama Models:** https://ai.meta.com/llama/
- **LangChain:** https://python.langchain.com/docs/

### Papers
- ReAct: Reasoning and Acting (https://arxiv.org/abs/2210.03629)
- Llama 3 Model Card (https://github.com/meta-llama/llama3)

### Communities
- Ollama Discord
- r/LocalLLaMA
- LangChain Discord

---

## ❓ FAQ

**Q: Can I use other models besides Llama 3.2?**
A: Yes! Try: `ollama pull mistral`, `ollama pull phi3`, etc.
Then change: `Ollama(model="mistral")`

**Q: Can I use cloud APIs (GPT-4, Claude) instead?**
A: Yes! Just swap:
```python
from langchain_openai import ChatOpenAI
llm = ChatOpenAI(model="gpt-4")
```

**Q: How do I deploy this to production?**
A: See Session 12 slides for Docker/Kubernetes deployment

**Q: Can agents write and execute code?**
A: Yes! Create a code execution tool (with safety measures)

**Q: What about security?**
A: Always validate inputs, use sandboxing for code execution, don't expose sensitive data in prompts

---

## 🎉 Congratulations!

You now have:
- ✅ Complete working code for all examples
- ✅ Understanding of single and multi-agent systems
- ✅ Production-ready templates
- ✅ Knowledge of Meta's Llama 3.2 via Ollama

**Next steps:**
1. Build something for your specific domain
2. Share what you create
3. Keep learning and experimenting

**Questions?** Review the code comments and try the examples hands-on!

---

## 📞 Support

If you encounter issues:
1. Check the Troubleshooting section
2. Make sure Ollama is running
3. Verify Llama 3.2 model is downloaded
4. Check Python package versions

**Remember:** Llama 3.2 (Meta's model) runs through Ollama (the server)!

---

Happy Building! 🚀
