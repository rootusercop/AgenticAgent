# Agentic AI: From Building Blocks to Multi-Agent Systems

A hands-on learning repository for understanding and building Agentic AI systems from the ground up. This repository takes you on a journey from creating simple autonomous agents to designing complex multi-agent architectures that can solve real-world problems.

## 🤖 What is Agentic AI?

**Agentic AI** refers to artificial intelligence systems that can act autonomously to achieve goals, rather than simply responding to prompts. Unlike traditional AI that waits for instructions, agentic AI systems can:

- **Perceive** their environment and understand context
- **Plan** sequences of actions to achieve objectives
- **Act** by using tools and making decisions
- **Learn** from feedback and adapt their behavior
- **Remember** past interactions and build on previous knowledge

Think of it as the difference between a calculator (responds to inputs) and a personal assistant (takes initiative, remembers your preferences, and proactively helps you achieve your goals).

## 📖 What This Repository Contains

This repository is organized into two progressive learning modules:

### 🧱 Part 1: Building Blocks of Autonomous Agents

**Learn the fundamentals of creating a single intelligent agent that can think, act, and remember.**

An autonomous agent is built from three core components:

#### 1. **The Brain (Language Model + Reasoning)**
The agent uses a Large Language Model (LLM) as its cognitive core. This gives it the ability to:
- Understand natural language queries
- Reason about problems
- Decide what actions to take
- Generate human-like responses

#### 2. **The Toolbox (External Capabilities)**
Agents become powerful when they can interact with the world through tools:
- **Search Tools:** Access information from the web (e.g., DuckDuckGo, Wikipedia)
- **APIs:** Call external services (weather, databases, calculators)
- **File Systems:** Read and write files
- **Custom Functions:** Any Python function can become an agent tool

*Example:* An agent with a calculator tool can perform math. An agent with a search tool can find current information beyond its training data.

#### 3. **The Memory (Context & State)**
Memory allows agents to be contextually aware:
- **Short-term Memory:** Remember the current conversation
- **Long-term Memory:** Store and retrieve information across sessions
- **Working Memory:** Keep track of intermediate steps in complex tasks

*Example:* An agent with memory can remember your name, your previous questions, and continue conversations naturally.

**What You'll Build:**
- A basic agent that answers questions using an LLM
- An agent that can search the web and Wikipedia
- An agent with conversational memory
- A complete agent combining all three capabilities

**Location:** `BuildSingleAgent/` directory

---

### 🤝 Part 2: Agent-to-Agent Communication & Multi-Agent Systems

**Learn how multiple specialized agents work together to solve complex problems that a single agent cannot handle alone.**

Real-world problems often require multiple types of expertise. Just as a hospital has specialists (cardiologists, radiologists, surgeons), complex AI systems benefit from having specialized agents that coordinate with each other.

#### Why Multiple Agents?

**Single Agent Limitations:**
- Cannot be expert in everything
- Becomes overwhelmed with complex, multi-step problems
- Difficult to maintain and update
- Cannot parallelize work

**Multi-Agent Benefits:**
- **Specialization:** Each agent focuses on what it does best
- **Scalability:** Add new capabilities by adding new agents
- **Maintainability:** Update one agent without affecting others
- **Robustness:** If one agent fails, others can continue
- **Parallelization:** Multiple agents can work simultaneously

#### Agent Communication Patterns

**1. Hierarchical (Coordinator-Worker)**
```
Coordinator Agent (Routes requests)
    ├── Specialist Agent A (Handles queries)
    ├── Specialist Agent B (Performs evaluations)
    └── Specialist Agent C (Makes recommendations)
```
*Use case:* Customer service system with routing to different departments

**2. Sequential Pipeline**
```
Agent A → Agent B → Agent C → Final Result
```
*Use case:* Document processing (extraction → analysis → summarization)

**3. Collaborative (Peer-to-Peer)**
```
Agent A ↔ Agent B ↔ Agent C
```
*Use case:* Brainstorming or consensus-building tasks

#### How Agents Communicate

Agents exchange information through:

- **Shared Memory:** A common workspace where agents read/write data
- **Message Passing:** Direct communication between agents
- **State Machines:** Agents trigger other agents based on state changes
- **Event Systems:** Agents subscribe to and publish events

**What You'll Build:**

**Workshop 1 - University Admission System:**
A multi-agent system with specialized roles:
- **Coordinator Agent:** Routes student queries to the right specialist
- **FAQ Agent:** Answers common questions about programs, deadlines, fees
- **Evaluator Agent:** Assesses student applications against criteria
- **Recommender Agent:** Suggests best-fit programs based on student profile

**Workshop 2 - Personalized Learning Path Generator:**
A collaborative agent system that creates custom curricula:
- **Profiler Agent:** Analyzes student background and goals
- **Skill Assessor Agent:** Evaluates current knowledge levels
- **Path Designer Agent:** Creates step-by-step learning roadmaps
- **Resource Curator Agent:** Recommends courses, books, and projects

**Location:** `BuildMultiAgent/` directory

---

## 🗂️ Repository Structure

```
AgenticAgent/
│
├── 01_Setup_and_Installation/          # Get your environment ready
│   ├── README.md                       # Quick setup guide
│   ├── setup.sh / setup.bat            # Automated installation scripts
│   └── requirements.txt                # Python dependencies
│
├── BuildSingleAgent/                   # Part 1: Single Agent Fundamentals
│   ├── Session_11_Complete_Presentation.html
│   └── Workshop_Code/
│       ├── 01_simple_agent.py          # Your first agent
│       ├── 02_agent_with_tools.py      # Adding web search capability
│       ├── 03_agent_with_memory.py     # Adding conversation memory
│       └── 04_complete_agent.py        # Full-featured agent
│
└── BuildMultiAgent/                    # Part 2: Multi-Agent Systems
    ├── Session_12_Complete_Presentation.html
    └── Workshop_Code/
        ├── workshop1_admission_system.py       # Multi-agent admission system
        ├── workshop1_interactive.py            # Interactive version
        ├── workshop2_learning_path_system.py   # Multi-agent learning paths
        ├── workshop2_interactive.py            # Interactive version
        └── *.md                                # Supporting documentation
```

## 🚀 Getting Started

### Prerequisites

- **Python 3.8+** (programming language)
- **8GB RAM minimum** (16GB recommended for smooth performance)
- **10GB free disk space** (for model and dependencies)
- **Basic Python knowledge** (helpful but not required)

### Installation (5 minutes)

1. **Clone or download this repository**

2. **Run the automated setup:**

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

   This installs:
   - Python virtual environment (isolated workspace)
   - LangChain (agent framework)
   - Ollama (runs AI models locally on your machine)
   - Llama 3.2 model (~4.7GB download)

3. **Verify everything works:**
   ```bash
   python verify_setup.py
   ```

📖 **Detailed installation guide:** [01_Setup_and_Installation/README.md](01_Setup_and_Installation/README.md)

## 🎯 Learning Path

### Recommended: Start with Building Blocks

```
Step 1: Setup (30 minutes)
   ↓
Step 2: Build Single Agents (90 minutes)
   → Run 01_simple_agent.py
   → Run 02_agent_with_tools.py
   → Run 03_agent_with_memory.py
   → Run 04_complete_agent.py
   ↓
Step 3: Build Multi-Agent Systems (90 minutes)
   → Run workshop1_interactive.py (Admission System)
   → Run workshop2_interactive.py (Learning Paths)
```

### Quick Demo: See Multi-Agent Systems in Action

Want to see the end result first? Try the interactive demos:

```bash
cd BuildMultiAgent/Workshop_Code
python workshop1_interactive.py  # Chat with an admission system
python workshop2_interactive.py  # Get a personalized learning path
```

## 🛠️ Technology Stack

- **Language Model:** Llama 3.2 (Meta's open-source AI, 8 billion parameters)
- **Runtime:** Ollama (runs models locally, no cloud needed)
- **Framework:** LangChain (Python library for building agents)
- **Tools:** DuckDuckGo Search, Wikipedia API
- **Language:** Python 3.8+

**Why these technologies?**
- **Free & Open Source:** No API costs, no vendor lock-in
- **Privacy:** Everything runs on your machine
- **Learning-Friendly:** Well-documented with active communities

## 💡 Key Concepts You'll Learn

### Single Agent Concepts
- **Prompt Engineering:** How to give effective instructions to LLMs
- **Tool Integration:** Connecting agents to external capabilities
- **Memory Systems:** Short-term vs long-term memory patterns
- **Agent Loops:** Perception → Planning → Action → Feedback

### Multi-Agent Concepts
- **Agent Specialization:** Designing focused, single-purpose agents
- **Communication Protocols:** How agents pass information
- **Coordination Patterns:** Hierarchical, sequential, collaborative
- **State Management:** Tracking complex workflows across agents
- **Error Handling:** Graceful degradation when agents fail

## 📚 Additional Resources

- **Setup Guide:** [01_Setup_and_Installation/README.md](01_Setup_and_Installation/README.md)
- **Quick Start Guide:** [BuildMultiAgent/Workshop_Code/QUICK_START.md](BuildMultiAgent/Workshop_Code/QUICK_START.md)
- **Interactive Workshops:** [BuildMultiAgent/Workshop_Code/INTERACTIVE_WORKSHOPS_README.md](BuildMultiAgent/Workshop_Code/INTERACTIVE_WORKSHOPS_README.md)
- **Testing Guide:** [BuildMultiAgent/Workshop_Code/TESTING_SUMMARY.md](BuildMultiAgent/Workshop_Code/TESTING_SUMMARY.md)

## 🔧 Troubleshooting

### "Connection refused" or "Can't connect to Ollama"
```bash
# Start the Ollama server (keep it running in a terminal)
ollama serve
```

### "Model 'llama3.2' not found"
```bash
# Download the AI model (one-time, ~4.7GB)
ollama pull llama3.2
```

### "Module not found" errors
```bash
# Activate your virtual environment first
source agentic_ai_env/bin/activate  # Mac/Linux
agentic_ai_env\Scripts\activate     # Windows

# Then reinstall dependencies
pip install -r requirements.txt
```

📖 **Full troubleshooting guide:** [01_Setup_and_Installation/README.md](01_Setup_and_Installation/README.md)

## 📊 What You'll Build

### By the End of Part 1 (Single Agent):
- ✅ An agent that answers questions using AI
- ✅ An agent that searches the web for current information
- ✅ An agent that remembers conversation context
- ✅ Understanding of agent components (LLM, tools, memory)

### By the End of Part 2 (Multi-Agent):
- ✅ A university admission system with 4 specialized agents
- ✅ A learning path generator with agent collaboration
- ✅ Understanding of agent communication patterns
- ✅ Ability to design multi-agent architectures for new problems

## 🎓 Who Is This For?

- **Students:** Learn cutting-edge AI development skills
- **Educators:** Teaching materials for AI/ML courses
- **Developers:** Practical introduction to agentic AI
- **Researchers:** Foundation for exploring agent-based systems
- **Hobbyists:** Build cool AI projects at home

**No prior AI experience required!** If you know basic Python, you can follow along.

## 🚀 Beyond This Repository

After completing these workshops, you'll be ready to:

1. **Build custom agents** for your specific use cases
2. **Design multi-agent systems** for complex workflows
3. **Integrate agents** into existing applications
4. **Explore advanced topics** like:
   - Retrieval-Augmented Generation (RAG)
   - Agent fine-tuning
   - Production deployment
   - Agent monitoring and observability

## 🤝 Contributing & Feedback

This repository was created as part of the **AICTE ATAL Faculty Development Program on Agentic AI**.

- **Presenter:** Mr. Nikhil Katre, Staff Software Engineer, Walmart Global Tech
- **Date:** November 22, 2025
- **Sessions:** 11 & 12 (Day 6)

Feel free to:
- Experiment with the code
- Adapt it for your use cases
- Share your implementations
- Provide feedback for improvements

## 📝 License

This workshop material is provided for educational purposes as part of the AICTE ATAL Faculty Development Program.

## 🙏 Acknowledgments

- **AICTE ATAL** - For organizing the Faculty Development Program
- **Meta AI** - For the Llama 3.2 open-source model
- **LangChain** - For the excellent agent framework
- **Ollama** - For making local LLM deployment accessible

---

## 🎉 Ready to Start?

1. **Install the tools:** `cd 01_Setup_and_Installation && ./setup.sh`
2. **Verify setup:** `python verify_setup.py`
3. **Build your first agent:** `cd ../BuildSingleAgent/Workshop_Code && python 01_simple_agent.py`

**Welcome to the world of Agentic AI!** 🚀

---

*Questions? Issues? Check the troubleshooting guides in each directory's documentation.*
