"""
Session 12 - Workshop 1: INTERACTIVE College Admission Management System
Multi-Agent System Architecture

Interactive Features:
1. Query Handler Agent - Answer your admission questions
2. Document Processor Agent - Submit and process applications
3. Eligibility Evaluator Agent - Get instant eligibility feedback
4. Communication Manager Agent - Receive personalized notifications

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
print(f"{Colors.MAGENTA}{Colors.BOLD}{' ' * 10}SESSION 12 - WORKSHOP 1 (INTERACTIVE){Colors.RESET}")
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

    def show_available_info(self):
        """Display available information"""
        print(f"\n{Colors.CYAN}{Colors.BOLD}📚 AVAILABLE INFORMATION{Colors.RESET}")
        print(f"{Colors.BLUE}{'=' * 70}{Colors.RESET}")
        print("\n📋 FAQ Topics:")
        for key in self.faq_db.keys():
            print(f"   • {key.title()}")
        print("\n🎓 Available Programs:")
        print("   • Computer Science (CS)")
        print("   • Electrical Engineering (EE)")
        print("   • Mechanical Engineering (ME)")
        print(f"\n{Colors.BLUE}{'=' * 70}{Colors.RESET}\n")


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
        print(f"{Colors.CYAN}     ✓ Evaluator ready with criteria: GPA≥{self.criteria['min_gpa']}{Colors.RESET}")

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


def load_application_from_files(email, transcript_file, rec_file, essay_file):
    """Load application from separate text files"""
    try:
        with open(transcript_file, 'r') as f:
            transcript = f.read()
        with open(rec_file, 'r') as f:
            recommendation = f.read()
        with open(essay_file, 'r') as f:
            essay = f.read()

        return {
            "email": email,
            "documents": {
                "transcript": transcript,
                "recommendation": recommendation,
                "essay": essay
            }
        }
    except FileNotFoundError as e:
        print(f"{Colors.RED}❌ Error: File not found - {e.filename}{Colors.RESET}")
        return None
    except Exception as e:
        print(f"{Colors.RED}❌ Error loading files: {str(e)}{Colors.RESET}")
        return None


def load_application_from_json(json_file):
    """Load application from JSON file"""
    try:
        with open(json_file, 'r') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        print(f"{Colors.RED}❌ Error: File not found - {json_file}{Colors.RESET}")
        return None
    except json.JSONDecodeError as e:
        print(f"{Colors.RED}❌ Error: Invalid JSON format - {str(e)}{Colors.RESET}")
        return None
    except Exception as e:
        print(f"{Colors.RED}❌ Error loading JSON: {str(e)}{Colors.RESET}")
        return None


def get_multiline_input(prompt_msg):
    """Get multi-line input from user"""
    print(prompt_msg)
    print("(Type your content and press Ctrl+D (Unix/Mac) or Ctrl+Z (Windows) when done)")
    lines = []
    try:
        while True:
            line = input()
            lines.append(line)
    except EOFError:
        pass
    return "\n".join(lines)


def main():
    """Interactive demo of the admission system"""

    # Initialize the multi-agent system
    system = AdmissionOrchestrator()

    print(f"\n{Colors.MAGENTA}{Colors.BOLD}{'=' * 70}{Colors.RESET}")
    print(f"{Colors.MAGENTA}{Colors.BOLD}{' ' * 20}INTERACTIVE MODE{Colors.RESET}")
    print(f"{Colors.MAGENTA}{Colors.BOLD}{'=' * 70}{Colors.RESET}")

    print("""
🎯 WHAT YOU CAN DO:

1️⃣  ASK QUESTIONS
   - Ask about admission deadlines, fees, programs, requirements
   - Example: "What is the application deadline?"
   - Example: "Tell me about the CS program"

2️⃣  SUBMIT APPLICATION (3 ways)
   - Load from sample files (quick demo)
   - Load from your own files
   - Type manually

3️⃣  VIEW AVAILABLE INFO
   - See all FAQ topics and programs

Commands:
   'info'  - Show available information
   'file'  - Load application from files (RECOMMENDED)
   'apply' - Type application manually
   'quit'  - Exit the system
""")

    print(f"{Colors.MAGENTA}{Colors.BOLD}{'=' * 70}{Colors.RESET}\n")

    while True:
        try:
            user_input = input(f"{Colors.CYAN}You: {Colors.RESET}").strip()

            if user_input.lower() in ['quit', 'exit', 'q']:
                print(f"\n{Colors.MAGENTA}{Colors.BOLD}{'=' * 70}{Colors.RESET}")
                print(" " * 25 + "SESSION ENDED")
                print(f"{Colors.MAGENTA}{Colors.BOLD}{'=' * 70}{Colors.RESET}")
                print("\n🎓 Thank you for using the Admission Management System!")
                print("   For questions, contact: admissions@university.edu\n")
                break

            elif user_input.lower() == 'info':
                system.query_handler.show_available_info()
                continue

            elif user_input.lower() == 'file':
                print(f"\n{Colors.YELLOW}{'=' * 70}{Colors.RESET}")
                print(" " * 20 + "📁 LOAD FROM FILES")
                print(f"{Colors.YELLOW}{'=' * 70}{Colors.RESET}\n")

                print("Choose an option:")
                print("  1. Strong candidate (sample - high GPA, great recs)")
                print("  2. Borderline candidate (sample - meets minimum requirements)")
                print("  3. Load from JSON file")
                print("  4. Load from your own text files")
                print("  5. Cancel")

                choice = input("\nYour choice (1-5): ").strip()

                application = None

                if choice == '1':
                    print(f"\n{Colors.CYAN}Loading strong candidate sample...{Colors.RESET}")
                    application = load_application_from_files(
                        "sarah.johnson@email.com",
                        "sample_data/strong_candidate_transcript.txt",
                        "sample_data/strong_candidate_recommendation.txt",
                        "sample_data/strong_candidate_essay.txt"
                    )

                elif choice == '2':
                    print(f"\n{Colors.CYAN}Loading borderline candidate sample...{Colors.RESET}")
                    application = load_application_from_files(
                        "alex.rivera@email.com",
                        "sample_data/borderline_candidate_transcript.txt",
                        "sample_data/borderline_candidate_recommendation.txt",
                        "sample_data/borderline_candidate_essay.txt"
                    )

                elif choice == '3':
                    json_path = input("\nEnter JSON file path (e.g., sample_data/sample_applications.json): ").strip()
                    print(f"\n{Colors.CYAN}Loading from JSON...{Colors.RESET}")
                    data = load_application_from_json(json_path)
                    if data:
                        # Check if it's a collection or single application
                        if "email" in data:
                            application = data
                        else:
                            # It's a collection, ask which one
                            print("\nAvailable applications in file:")
                            for idx, key in enumerate(data.keys(), 1):
                                print(f"  {idx}. {key}")
                            app_choice = input("\nSelect application number: ").strip()
                            try:
                                app_key = list(data.keys())[int(app_choice) - 1]
                                application = data[app_key]
                            except (ValueError, IndexError):
                                print(f"{Colors.RED}Invalid selection{Colors.RESET}")

                elif choice == '4':
                    email = input("\nStudent email: ").strip()
                    transcript_file = input("Transcript file path: ").strip()
                    rec_file = input("Recommendation file path: ").strip()
                    essay_file = input("Essay file path: ").strip()
                    print(f"\n{Colors.CYAN}Loading from your files...{Colors.RESET}")
                    application = load_application_from_files(email, transcript_file, rec_file, essay_file)

                elif choice == '5':
                    print(f"{Colors.YELLOW}Cancelled{Colors.RESET}")
                    continue

                else:
                    print(f"{Colors.RED}Invalid choice{Colors.RESET}")
                    continue

                if application:
                    print(f"\n{Colors.GREEN}✅ Application loaded successfully!{Colors.RESET}")
                    print(f"   Email: {application['email']}")
                    print(f"   Processing...{Colors.RESET}\n")

                    # Process application
                    result = system.process_application(application)

                    print(f"\n{Colors.MAGENTA}{Colors.BOLD}{'=' * 70}{Colors.RESET}")
                    print(" " * 20 + "📊 FINAL RESULTS")
                    print(f"{Colors.MAGENTA}{Colors.BOLD}{'=' * 70}{Colors.RESET}")
                    print(json.dumps(result, indent=2, default=str))
                    print()
                else:
                    print(f"\n{Colors.RED}Failed to load application{Colors.RESET}")

                continue

            elif user_input.lower() == 'apply':
                print(f"\n{Colors.YELLOW}{'=' * 70}{Colors.RESET}")
                print(" " * 20 + "📝 APPLICATION SUBMISSION")
                print(f"{Colors.YELLOW}{'=' * 70}{Colors.RESET}\n")

                # Collect application data
                email = input("Your email address: ").strip()

                print("\n📄 TRANSCRIPT")
                print("Enter your transcript information (Name, GPA, Subjects, Graduation):")
                transcript = get_multiline_input("")

                print("\n📝 RECOMMENDATION LETTER")
                recommendation = get_multiline_input("Enter your recommendation letter:")

                print("\n✍️  ESSAY")
                essay = get_multiline_input("Enter your essay:")

                # Create application
                application = {
                    "email": email,
                    "documents": {
                        "transcript": transcript,
                        "recommendation": recommendation,
                        "essay": essay
                    }
                }

                print(f"\n{Colors.GREEN}✅ Application received! Processing...{Colors.RESET}\n")

                # Process application
                result = system.process_application(application)

                print(f"\n{Colors.MAGENTA}{Colors.BOLD}{'=' * 70}{Colors.RESET}")
                print(" " * 20 + "📊 FINAL RESULTS")
                print(f"{Colors.MAGENTA}{Colors.BOLD}{'=' * 70}{Colors.RESET}")
                print(json.dumps(result, indent=2, default=str))
                print()

            elif not user_input:
                continue

            else:
                # Handle as a query
                print(f"\n{Colors.YELLOW}🤖 Query Handler Agent processing...{Colors.RESET}\n")
                response = system.route_request("query", user_input)
                print(f"\n{Colors.BLUE}📝 Response:{Colors.RESET}")
                print(f"{response}\n")
                print(f"{Colors.BLUE}{'-' * 70}{Colors.RESET}\n")

        except KeyboardInterrupt:
            print("\n\nExiting on user interrupt...")
            break
        except Exception as e:
            print(f"\n{Colors.RED}❌ Error occurred: {str(e)}{Colors.RESET}")
            print("Please try again.\n")


if __name__ == "__main__":
    main()
