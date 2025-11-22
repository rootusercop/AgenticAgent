"""
Session 12 - Workshop 1: College Admission Management System
Multi-Agent System Architecture

Components:
1. Query Handler Agent - Answers student questions
2. Document Processor Agent - Extracts data from applications
3. Eligibility Evaluator Agent - Determines admission eligibility
4. Communication Manager Agent - Sends notifications

Using: Meta's Llama 3.2 8B via Ollama
"""

# Suppress urllib3 NotOpenSSLWarning on macOS
import warnings
warnings.filterwarnings('ignore', message='.*OpenSSL.*')

from langchain.agents import initialize_agent, AgentType
from langchain_community.llms import Ollama
from langchain.tools import Tool
import json
from datetime import datetime

# ANSI color codes for better visibility on white backgrounds
class Colors:
    BLUE = '\033[94m'       # Blue - for info
    CYAN = '\033[96m'       # Cyan - for success/checkmarks
    MAGENTA = '\033[95m'    # Magenta - for headers
    GREEN = '\033[92m'      # Green - for positive outcomes
    YELLOW = '\033[93m'     # Yellow - for warnings/important
    RED = '\033[91m'        # Red - for errors
    BOLD = '\033[1m'        # Bold text
    UNDERLINE = '\033[4m'   # Underline
    RESET = '\033[0m'       # Reset to default

print(f"{Colors.MAGENTA}{Colors.BOLD}{'=' * 70}{Colors.RESET}")
print(f"{Colors.MAGENTA}{Colors.BOLD}{' ' * 10}SESSION 12 - WORKSHOP 1{Colors.RESET}")
print(f"{Colors.MAGENTA}{Colors.BOLD}{' ' * 5}COLLEGE ADMISSION MANAGEMENT SYSTEM{Colors.RESET}")
print(f"{Colors.MAGENTA}{Colors.BOLD}{'=' * 70}{Colors.RESET}")
print(f"\n{Colors.CYAN}🎓 Multi-Agent System for Automated Admissions{Colors.RESET}")
print(f"{Colors.BLUE}   Model: Meta's Llama 3.2 via Ollama{Colors.RESET}")
print(f"{Colors.MAGENTA}{Colors.BOLD}{'=' * 70}{Colors.RESET}\n")


class QueryHandlerAgent:
    """
    Agent 1: Handles student queries about admissions
    Tools: FAQ database, program information
    """

    def __init__(self, llm):
        print(f"{Colors.BLUE}  [Agent Query Handler] Initializing Query Handler...{Colors.RESET}")
        self.llm = llm

        # FAQ database (simulate - in production use vector DB)
        self.faq_db = {
            "deadline": "Application deadline is November 30th, 2025",
            "fee": "Application fee is $50 (waiver available)",
            "documents": "Required: Transcripts, ID, 2 recommendation letters, essay",
            "gpa": "Minimum GPA: 3.0 on 4.0 scale",
            "programs": "BS in CS, EE, ME available",
            "housing": "On-campus housing available, apply separately",
            "scholarships": "Merit scholarships up to $5,000/year available"
        }

        # Create tools for this agent
        self.tools = [
            Tool(
                name="FAQ_Search",
                func=self.search_faq,
                description="Search FAQ database. Input: keyword"
            ),
            Tool(
                name="Program_Info",
                func=self.get_program_info,
                description="Get program details. Input: 'CS', 'EE', or 'ME'"
            )
        ]

        # Initialize as LangChain agent
        self.agent = initialize_agent(
            self.tools,
            llm,
            agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
            verbose=False  # Set True to see reasoning
        )
        print(f"{Colors.CYAN}     ✓ Query Handler ready with 2 tools{Colors.RESET}")

    def search_faq(self, query: str) -> str:
        """Search FAQ database"""
        query = query.lower()
        for key, answer in self.faq_db.items():
            if key in query:
                return f"📋 {answer}"
        return "ℹ️ For this query, please contact admissions@university.edu"

    def get_program_info(self, program: str) -> str:
        """Get detailed program information"""
        programs = {
            "CS": {
                "name": "Computer Science",
                "duration": "4 years",
                "fee": "$10,000/year",
                "requirements": "Strong math, Physics/CS background",
                "career": "Software Engineer, Data Scientist, AI Researcher"
            },
            "EE": {
                "name": "Electrical Engineering",
                "duration": "4 years",
                "fee": "$10,000/year",
                "requirements": "Math, Physics background",
                "career": "Electronics Engineer, Power Systems Engineer"
            },
            "ME": {
                "name": "Mechanical Engineering",
                "duration": "4 years",
                "fee": "$9,500/year",
                "requirements": "Math, Physics background",
                "career": "Mechanical Designer, Robotics Engineer"
            }
        }
        info = programs.get(program.upper(), {})
        if info:
            return f"""
📚 {info['name']} Program
   Duration: {info['duration']}
   Fee: {info['fee']}
   Requirements: {info['requirements']}
   Career paths: {info['career']}
            """
        return "Program not found"

    def handle(self, query: str) -> str:
        """Handle a student query"""
        return self.agent.run(query)


class DocumentProcessorAgent:
    """
    Agent 2: Processes and extracts information from documents
    Uses Llama 3.2 for intelligent extraction
    """

    def __init__(self, llm):
        print(f"{Colors.BLUE}  [Agent Document Processor] Initializing Document Processor...{Colors.RESET}")
        self.llm = llm
        print(f"{Colors.CYAN}     ✓ Document Processor ready{Colors.RESET}")

    def extract(self, documents: dict) -> dict:
        """Extract structured information from documents"""
        extracted = {}

        for doc_type, doc_content in documents.items():
            print(f"{Colors.YELLOW}     → Processing {doc_type}...{Colors.RESET}")

            if doc_type == "transcript":
                prompt = f"""Extract this information from the transcript:
- GPA (numeric value)
- Subjects studied (list)
- Graduation year

Transcript:
{doc_content}

Return ONLY valid JSON: {{"gpa": X.X, "subjects": [...], "graduation_year": YYYY}}"""

                result = self.llm.invoke(prompt)
                extracted["transcript"] = result

            elif doc_type == "recommendation":
                prompt = f"""Summarize this recommendation in 3 bullet points:

{doc_content}

Format as:
- Point 1
- Point 2
- Point 3"""

                result = self.llm.invoke(prompt)
                extracted["recommendation"] = result

            elif doc_type == "essay":
                prompt = f"""Analyze this essay and return JSON:

Essay:
{doc_content}

Return: {{"main_themes": ["theme1", "theme2"], "writing_quality": X, "authenticity": X}}
Scores are 1-10."""

                result = self.llm.invoke(prompt)
                extracted["essay"] = result

        return extracted


class EligibilityEvaluatorAgent:
    """
    Agent 3: Evaluates student eligibility based on criteria
    Uses Llama 3.2 for intelligent evaluation
    """

    def __init__(self, llm):
        print(f"{Colors.BLUE}  [Agent Eligibility Evaluator] Initializing Eligibility Evaluator...{Colors.RESET}")
        self.llm = llm
        self.criteria = {
            "min_gpa": 3.0,
            "required_subjects": ["Math", "Physics"],
            "min_essay_score": 6
        }
        print(f"     ✓ Evaluator ready with criteria: GPA≥{self.criteria['min_gpa']}")

    def evaluate(self, extracted_data: dict) -> str:
        """Evaluate eligibility and return decision"""
        print(f"{Colors.YELLOW}     → Calculating eligibility score...{Colors.RESET}")

        prompt = f"""Evaluate student eligibility:

CRITERIA:
{json.dumps(self.criteria, indent=2)}

STUDENT DATA:
{json.dumps(extracted_data, indent=2)}

Determine:
1. Eligible? (true/false)
2. Score (0-100)
3. Strengths (list 2-3)
4. Weaknesses (if any)
5. Reasoning (2 sentences)

Return valid JSON with keys: eligible, score, strengths, weaknesses, reasoning"""

        result = self.llm.invoke(prompt)
        return result


class CommunicationManagerAgent:
    """
    Agent 4: Manages all communication with students
    Generates personalized emails using Llama 3.2
    """

    def __init__(self, llm):
        print(f"{Colors.BLUE}  [Agent Communication Manager] Initializing Communication Manager...{Colors.RESET}")
        self.llm = llm
        print(f"{Colors.CYAN}     ✓ Communication Manager ready{Colors.RESET}")

    def notify(self, email: str, eligibility_result: str) -> dict:
        """Generate and send notification email"""
        print(f"{Colors.YELLOW}     → Preparing notification for {email}...{Colors.RESET}")

        prompt = f"""Write a professional admission email:

DECISION:
{eligibility_result}

Requirements:
- Professional but warm tone
- Clear decision statement
- If accepted: Congratulate + next steps
- If not: Encourage + suggest alternatives
- Include: admissions@university.edu for questions

Write the complete email:"""

        email_content = self.llm.invoke(prompt)

        # In production: send via SMTP/SendGrid
        separator = "=" * 60
        print(f"{Colors.CYAN}{Colors.BOLD}\n     {separator}{Colors.RESET}")
        print(f"     📧 EMAIL TO: {email}")
        print(f"{Colors.CYAN}{Colors.BOLD}     {separator}{Colors.RESET}")
        print(f"{email_content}")
        print("     " + "=" * 60 + "\n")

        return {
            "sent": True,
            "to": email,
            "timestamp": datetime.now().isoformat(),
            "content": email_content
        }


class AdmissionOrchestrator:
    """
    Main Orchestrator: Coordinates all agents
    Implements sequential pipeline pattern
    """

    def __init__(self):
        print(f"\n{Colors.CYAN}{Colors.BOLD}🔧 Initializing Admission Management System...{Colors.RESET}")
        dash_line = "-" * 70
        print(f"{Colors.BLUE}{dash_line}{Colors.RESET}")

        # Initialize Llama 3.2 (shared across all agents)
        print("\n[Core] Connecting to Meta's Llama 3.2 via Ollama...")
        self.llm = Ollama(model="llama3.2", temperature=0.7)
        print("  ✓ Llama 3.2 8B connected")

        print("\n[Sub-Agents] Initializing specialized agents...")
        self.query_handler = QueryHandlerAgent(self.llm)
        self.doc_processor = DocumentProcessorAgent(self.llm)
        self.eligibility_evaluator = EligibilityEvaluatorAgent(self.llm)
        self.comm_manager = CommunicationManagerAgent(self.llm)

        self.state = {}  # Shared state across agents

        print("\n" + "=" * 70)
        print(" " * 15 + "✅ SYSTEM FULLY OPERATIONAL")
        print("=" * 70 + "\n")

    def route_request(self, request_type: str, data):
        """Route request to appropriate agent"""
        if request_type == "query":
            return self.query_handler.handle(data)
        elif request_type == "application":
            return self.process_application(data)
        else:
            return {"error": "Unknown request type"}

    def process_application(self, application_data: dict) -> dict:
        """
        Process application through sequential pipeline:
        Document Processing → Eligibility Evaluation → Communication
        """
        print("\n" + "🔄" * 35)
        print(" " * 15 + "APPLICATION PROCESSING PIPELINE")
        print("🔄" * 35 + "\n")

        # STEP 1: Process Documents
        print("[STEP 1/3] 📄 DOCUMENT PROCESSING")
        dash_line = "-" * 70
        print(f"{Colors.BLUE}{dash_line}{Colors.RESET}")
        extracted_data = self.doc_processor.extract(
            application_data["documents"]
        )
        self.state["extracted_data"] = extracted_data
        print("  ✅ Documents processed successfully\n")

        # STEP 2: Evaluate Eligibility
        print("[STEP 2/3] 📊 ELIGIBILITY EVALUATION")
        dash_line = "-" * 70
        print(f"{Colors.BLUE}{dash_line}{Colors.RESET}")
        eligibility = self.eligibility_evaluator.evaluate(extracted_data)
        self.state["eligibility"] = eligibility
        print("  ✅ Eligibility determined\n")

        # STEP 3: Send Communication
        print("[STEP 3/3] 📧 COMMUNICATION")
        dash_line = "-" * 70
        print(f"{Colors.BLUE}{dash_line}{Colors.RESET}")
        notification = self.comm_manager.notify(
            application_data["email"],
            eligibility
        )

        print("🔄" * 35)
        print(" " * 10 + "✅ APPLICATION PROCESSING COMPLETE")
        print("🔄" * 35 + "\n")

        return {
            "status": "processed",
            "extracted_data": extracted_data,
            "eligibility": eligibility,
            "notification_sent": True
        }


def main():
    """Demo the admission system"""

    # Initialize the multi-agent system
    system = AdmissionOrchestrator()

    print("\n" + "📋" * 35)
    print(" " * 20 + "DEMO SCENARIOS")
    print("📋" * 35 + "\n")

    # SCENARIO 1: Student Query
    print("\n" + "=" * 70)
    print("SCENARIO 1: Student Query")
    separator = "=" * 70
    print(f"{Colors.MAGENTA}{Colors.BOLD}{separator}{Colors.RESET}")
    query = "What is the application deadline and what documents do I need?"
    print(f"\n💬 Student asks: {query}\n")
    print("🤖 Query Handler Agent processing...\n")

    response = system.route_request("query", query)
    print(f"\n📝 Response:\n{response}\n")

    input("\n⏸️  Press Enter to continue to Scenario 2...\n")

    # SCENARIO 2: Application Submission
    print("\n" + "=" * 70)
    print("SCENARIO 2: Complete Application Processing")
    separator = "=" * 70
    print(f"{Colors.MAGENTA}{Colors.BOLD}{separator}{Colors.RESET}")

    application = {
        "email": "priya.sharma@email.com",
        "documents": {
            "transcript": """
Student: Priya Sharma
GPA: 3.7 / 4.0
Subjects: Mathematics (A), Physics (A), Computer Science (A-), Chemistry (B+)
Graduation: June 2025
            """,
            "recommendation": """
To the Admissions Committee,

I have known Priya for three years as her Computer Science teacher.
She is an exceptional student with:
- Strong analytical and problem-solving skills
- Leadership in coding club and hackathons
- Consistent top 5% class ranking
- Genuine passion for technology and innovation

I highly recommend her for your Computer Science program.

Sincerely,
Prof. Raj Mehta
            """,
            "essay": """
My Journey into Computer Science

Ever since I built my first website at age 14, I knew I wanted to pursue computer science.
The ability to create solutions that impact millions of people fascinates me.
During high school, I led our school's coding club and organized hackathons.
I'm particularly interested in artificial intelligence and its potential to solve real-world problems.
Your university's research in agentic AI aligns perfectly with my goals.
I'm excited to contribute to this field and learn from the best.
            """
        }
    }

    print("\n📨 Student submits application:")
    print(f"   Email: {application['email']}")
    print(f"   Documents: {len(application['documents'])} files")
    print("\n🚀 Starting multi-agent processing...\n")

    result = system.process_application(application)

    print("\n" + "=" * 70)
    print(" " * 20 + "📊 FINAL RESULTS")
    separator = "=" * 70
    print(f"{Colors.MAGENTA}{Colors.BOLD}{separator}{Colors.RESET}")
    print(json.dumps(result, indent=2, default=str))

    print("\n" + "=" * 70)
    print(" " * 15 + "🎉 WORKSHOP 1 COMPLETE!")
    separator = "=" * 70
    print(f"{Colors.MAGENTA}{Colors.BOLD}{separator}{Colors.RESET}")
    print("""
✅ You've built a multi-agent system that:
   - Answers student queries (Agent 1)
   - Processes documents automatically (Agent 2)
   - Evaluates eligibility intelligently (Agent 3)
   - Sends personalized communications (Agent 4)

💡 This pattern can be adapted for:
   - HR recruitment systems
   - Loan application processing
   - Grant proposal evaluation
   - Customer onboarding
   - And much more!

🔧 Architecture: Sequential Pipeline
   Document Processing → Evaluation → Communication

🤖 Powered by: Meta's Llama 3.2 8B via Ollama
""")
    print("=" * 70 + "\n")


if __name__ == "__main__":
    main()
