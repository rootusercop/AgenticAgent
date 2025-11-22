"""
Session 12 - Workshop 2: INTERACTIVE Personalized Learning Path Generator
Multi-Agent System with Feedback Loops

Interactive Features:
1. Load student profiles from JSON files
2. Query learning paths and recommendations
3. Track progress interactively
4. Beautiful formatted output
5. Manual student profile entry

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
print(f"{Colors.MAGENTA}{Colors.BOLD}{' ' * 10}SESSION 12 - WORKSHOP 2 (INTERACTIVE){Colors.RESET}")
print(f"{Colors.MAGENTA}{Colors.BOLD}{' ' * 5}PERSONALIZED LEARNING PATH GENERATOR{Colors.RESET}")
print(f"{Colors.MAGENTA}{Colors.BOLD}{'=' * 70}{Colors.RESET}")
print(f"\n{Colors.CYAN}🎯 AI-Powered Adaptive Learning System{Colors.RESET}")
print(f"{Colors.BLUE}   Model: Meta's Llama 3.2 via Ollama{Colors.RESET}")
print(f"{Colors.MAGENTA}{Colors.BOLD}{'=' * 70}{Colors.RESET}\n")


class SkillsAssessmentAgent:
    """
    Agent 1: Assesses student's current skill level
    Tools: Code challenges, concept quizzes
    """

    def __init__(self, llm):
        print(f"{Colors.BLUE}  [Agent Skills Assessment] Initializing Skills Assessment Agent...{Colors.RESET}")
        self.llm = llm

        self.tools = [
            Tool(
                name="CodeChallenge",
                func=self.run_code_challenge,
                description="Run coding challenge. Input: difficulty (beginner/intermediate/advanced)"
            ),
            Tool(
                name="ConceptQuiz",
                func=self.run_concept_quiz,
                description="Run concept quiz. Input: topic name"
            )
        ]

        self.agent = initialize_agent(
            self.tools,
            llm,
            agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
            verbose=False
        )
        print(f"{Colors.CYAN}     ✓ Assessment Agent ready with 2 evaluation tools{Colors.RESET}")

    def run_code_challenge(self, difficulty: str) -> str:
        """Simulate running a code challenge"""
        challenges = {
            "beginner": {
                "problem": "Find largest number in a list",
                "score": 75,
                "time": "12 minutes",
                "feedback": "Good understanding of basics, familiar with list operations"
            },
            "intermediate": {
                "problem": "Implement binary search algorithm",
                "score": 65,
                "time": "22 minutes",
                "feedback": "Understands concept but needs practice with edge cases"
            },
            "advanced": {
                "problem": "Design a balanced binary search tree",
                "score": 45,
                "time": "35 minutes",
                "feedback": "Needs more experience with advanced data structures"
            }
        }

        challenge = challenges.get(difficulty, challenges["beginner"])
        return json.dumps({
            "problem": challenge["problem"],
            "score": challenge["score"],
            "time_taken": challenge["time"],
            "feedback": challenge["feedback"]
        })

    def run_concept_quiz(self, topic: str) -> str:
        """Simulate running a concept quiz"""
        return json.dumps({
            "topic": topic,
            "score": 80,
            "questions": 10,
            "correct": 8,
            "strengths": [f"Strong grasp of {topic} fundamentals"],
            "weaknesses": [f"Needs work on advanced {topic} applications"]
        })

    def assess(self, student_profile: dict) -> dict:
        """Comprehensive skill assessment"""
        print(f"{Colors.YELLOW}     → Running comprehensive assessment...{Colors.RESET}")

        # Use current_skills if provided, otherwise simulate
        if "current_skills" in student_profile:
            skills = student_profile["current_skills"]
            # Calculate overall level
            avg_score = sum(skills.values()) / len(skills)
            if avg_score <= 3:
                overall = "beginner"
            elif avg_score <= 6:
                overall = "intermediate"
            else:
                overall = "advanced"

            return {
                **skills,
                "overall_level": overall,
                "assessment_summary": f"Current skill level: {overall.title()}. Ready for structured learning path."
            }
        else:
            # Default assessment
            return {
                "python": 7,
                "algorithms": 6,
                "data_structures": 5,
                "machine_learning": 3,
                "deep_learning": 2,
                "mathematics": 6,
                "overall_level": "intermediate",
                "assessment_summary": "Strong programming foundation, ready for ML journey"
            }


class LearningPathPlanner:
    """
    Agent 2: Creates personalized learning paths
    Uses Llama 3.2 for intelligent planning
    """

    def __init__(self, llm):
        print(f"{Colors.BLUE}  [Agent Learning Path Planner] Initializing Learning Path Planner...{Colors.RESET}")
        self.llm = llm
        print(f"{Colors.CYAN}     ✓ Path Planner ready{Colors.RESET}")

    def create_path(self, skills_matrix: dict, goal: str, hours_per_week: int, overall_level: str = "intermediate") -> dict:
        """Create customized 6-month learning roadmap"""
        print(f"{Colors.YELLOW}     → Generating personalized learning path...{Colors.RESET}")

        # Generate path based on level and goal
        if "Machine Learning" in goal or "ML" in goal or "AI" in goal:
            return self._create_ml_path(skills_matrix, goal, hours_per_week, overall_level)
        elif "Software Developer" in goal or "Programming" in goal:
            return self._create_dev_path(skills_matrix, goal, hours_per_week, overall_level)
        elif "Data Scientist" in goal or "Data" in goal:
            return self._create_ds_path(skills_matrix, goal, hours_per_week, overall_level)
        else:
            return self._create_ml_path(skills_matrix, goal, hours_per_week, overall_level)

    def _create_ml_path(self, skills_matrix, goal, hours_per_week, level):
        """Create ML Engineer path"""
        return {
            "duration": "6 months",
            "total_hours": hours_per_week * 4 * 6,
            "hours_per_week": hours_per_week,
            "goal": goal,
            "difficulty_level": level,
            "months": [
                {
                    "month": 1,
                    "focus": "Advanced Python + Data Libraries",
                    "topics": [
                        "Object-oriented programming (classes, inheritance)",
                        "Decorators and generators",
                        "NumPy arrays and vectorization",
                        "Pandas DataFrames and data manipulation"
                    ],
                    "prerequisites": "Basic Python",
                    "hours": hours_per_week * 4,
                    "milestone": "Complete 3 data analysis projects using real datasets",
                    "skills_gained": ["OOP", "NumPy", "Pandas"]
                },
                {
                    "month": 2,
                    "focus": "Mathematics for Machine Learning",
                    "topics": [
                        "Linear Algebra (vectors, matrices, eigenvalues)",
                        "Calculus (derivatives, gradients, chain rule)",
                        "Probability and statistics",
                        "Mathematical notation in ML papers"
                    ],
                    "prerequisites": "High school math",
                    "hours": hours_per_week * 4,
                    "milestone": "Pass math fundamentals quiz with 80%+ score",
                    "skills_gained": ["Linear Algebra", "Calculus", "Statistics"]
                },
                {
                    "month": 3,
                    "focus": "Machine Learning Fundamentals",
                    "topics": [
                        "Supervised learning (regression, classification)",
                        "Unsupervised learning (clustering, dimensionality reduction)",
                        "Scikit-learn library and pipelines",
                        "Model evaluation and cross-validation"
                    ],
                    "prerequisites": "Python + Math foundations",
                    "hours": hours_per_week * 4,
                    "milestone": "Build 2 end-to-end ML projects from scratch",
                    "skills_gained": ["Scikit-learn", "ML algorithms", "Model evaluation"]
                },
                {
                    "month": 4,
                    "focus": "Deep Learning Basics",
                    "topics": [
                        "Neural networks fundamentals",
                        "Backpropagation and optimization",
                        "PyTorch or TensorFlow",
                        "CNNs for computer vision"
                    ],
                    "prerequisites": "ML fundamentals",
                    "hours": hours_per_week * 4,
                    "milestone": "Build image classifier with 90%+ accuracy",
                    "skills_gained": ["PyTorch", "Neural Networks", "CNNs"]
                },
                {
                    "month": 5,
                    "focus": "Advanced Deep Learning",
                    "topics": [
                        "RNNs and LSTMs for sequences",
                        "Transformers and attention mechanisms",
                        "Transfer learning and fine-tuning",
                        "GANs basics"
                    ],
                    "prerequisites": "DL basics",
                    "hours": hours_per_week * 4,
                    "milestone": "Fine-tune pre-trained model for custom task",
                    "skills_gained": ["RNNs", "Transformers", "Transfer Learning"]
                },
                {
                    "month": 6,
                    "focus": "MLOps and Production Deployment",
                    "topics": [
                        "Model deployment with Docker",
                        "FastAPI for ML APIs",
                        "Model monitoring and maintenance",
                        "Cloud platforms (AWS/GCP)"
                    ],
                    "prerequisites": "DL proficiency",
                    "hours": hours_per_week * 4,
                    "milestone": "Deploy full ML system to production with monitoring",
                    "skills_gained": ["Docker", "MLOps", "Production deployment"]
                }
            ],
            "final_goal": "Job-ready ML Engineer with portfolio of projects"
        }

    def _create_dev_path(self, skills_matrix, goal, hours_per_week, level):
        """Create Software Developer path"""
        return {
            "duration": "6 months",
            "total_hours": hours_per_week * 4 * 6,
            "hours_per_week": hours_per_week,
            "goal": goal,
            "difficulty_level": level,
            "months": [
                {
                    "month": 1,
                    "focus": "Programming Fundamentals & Best Practices",
                    "topics": [
                        "Clean code principles",
                        "Data structures (arrays, lists, trees, graphs)",
                        "Algorithm complexity analysis",
                        "Git version control mastery"
                    ],
                    "prerequisites": "Basic programming knowledge",
                    "hours": hours_per_week * 4,
                    "milestone": "Complete 20 coding challenges on LeetCode/HackerRank",
                    "skills_gained": ["Data Structures", "Algorithms", "Git"]
                },
                {
                    "month": 2,
                    "focus": "Web Development Foundations",
                    "topics": [
                        "HTML5, CSS3, and responsive design",
                        "JavaScript ES6+ fundamentals",
                        "DOM manipulation and events",
                        "REST API concepts"
                    ],
                    "prerequisites": "Programming fundamentals",
                    "hours": hours_per_week * 4,
                    "milestone": "Build 3 interactive web applications",
                    "skills_gained": ["HTML/CSS", "JavaScript", "APIs"]
                },
                {
                    "month": 3,
                    "focus": "Backend Development",
                    "topics": [
                        "Node.js or Python Flask/Django",
                        "Database design (SQL and NoSQL)",
                        "Authentication and authorization",
                        "Building RESTful APIs"
                    ],
                    "prerequisites": "Web foundations",
                    "hours": hours_per_week * 4,
                    "milestone": "Build full-stack CRUD application with database",
                    "skills_gained": ["Backend frameworks", "Databases", "API development"]
                },
                {
                    "month": 4,
                    "focus": "Modern Frontend Frameworks",
                    "topics": [
                        "React.js or Vue.js fundamentals",
                        "State management (Redux/Vuex)",
                        "Component-based architecture",
                        "Modern build tools (Webpack, Vite)"
                    ],
                    "prerequisites": "JavaScript proficiency",
                    "hours": hours_per_week * 4,
                    "milestone": "Build SPA (Single Page Application) with modern framework",
                    "skills_gained": ["React/Vue", "State management", "Modern tooling"]
                },
                {
                    "month": 5,
                    "focus": "DevOps & Testing",
                    "topics": [
                        "Unit testing and integration testing",
                        "CI/CD pipelines",
                        "Docker containers",
                        "Cloud deployment (AWS/GCP/Azure)"
                    ],
                    "prerequisites": "Full-stack development skills",
                    "hours": hours_per_week * 4,
                    "milestone": "Deploy application with automated testing and CI/CD",
                    "skills_gained": ["Testing", "Docker", "CI/CD", "Cloud"]
                },
                {
                    "month": 6,
                    "focus": "Portfolio & Interview Preparation",
                    "topics": [
                        "System design basics",
                        "Behavioral interview preparation",
                        "Portfolio website development",
                        "LeetCode medium/hard problems"
                    ],
                    "prerequisites": "All previous months",
                    "hours": hours_per_week * 4,
                    "milestone": "Complete portfolio with 5 projects, pass 10 mock interviews",
                    "skills_gained": ["System design", "Interview skills", "Portfolio"]
                }
            ],
            "final_goal": "Job-ready Junior Software Developer with strong portfolio"
        }

    def _create_ds_path(self, skills_matrix, goal, hours_per_week, level):
        """Create Data Scientist path"""
        return {
            "duration": "6 months",
            "total_hours": hours_per_week * 4 * 6,
            "hours_per_week": hours_per_week,
            "goal": goal,
            "difficulty_level": level,
            "months": [
                {
                    "month": 1,
                    "focus": "Python for Data Analysis",
                    "topics": [
                        "Python fundamentals and syntax",
                        "Pandas for data manipulation",
                        "Data cleaning and preprocessing",
                        "Jupyter notebooks workflow"
                    ],
                    "prerequisites": "Basic programming or analytical thinking",
                    "hours": hours_per_week * 4,
                    "milestone": "Complete 5 data cleaning and analysis projects",
                    "skills_gained": ["Python", "Pandas", "Data cleaning"]
                },
                {
                    "month": 2,
                    "focus": "Statistics & Probability",
                    "topics": [
                        "Descriptive and inferential statistics",
                        "Probability distributions",
                        "Hypothesis testing",
                        "Statistical significance"
                    ],
                    "prerequisites": "Basic mathematics",
                    "hours": hours_per_week * 4,
                    "milestone": "Complete statistical analysis on 3 real-world datasets",
                    "skills_gained": ["Statistics", "Hypothesis testing", "Data analysis"]
                },
                {
                    "month": 3,
                    "focus": "Data Visualization & Communication",
                    "topics": [
                        "Matplotlib and Seaborn",
                        "Plotly for interactive visualizations",
                        "Dashboard creation with Tableau/PowerBI",
                        "Data storytelling techniques"
                    ],
                    "prerequisites": "Python and statistics",
                    "hours": hours_per_week * 4,
                    "milestone": "Create 3 comprehensive data visualization dashboards",
                    "skills_gained": ["Data visualization", "Dashboards", "Storytelling"]
                },
                {
                    "month": 4,
                    "focus": "Machine Learning for Data Science",
                    "topics": [
                        "Regression and classification models",
                        "Feature engineering",
                        "Model selection and validation",
                        "Scikit-learn for ML"
                    ],
                    "prerequisites": "Statistics and Python",
                    "hours": hours_per_week * 4,
                    "milestone": "Build 3 predictive models with real business data",
                    "skills_gained": ["Machine learning", "Feature engineering", "Model validation"]
                },
                {
                    "month": 5,
                    "focus": "Advanced ML & Big Data",
                    "topics": [
                        "Ensemble methods (Random Forest, XGBoost)",
                        "Time series analysis",
                        "SQL for data extraction",
                        "Introduction to Spark for big data"
                    ],
                    "prerequisites": "ML fundamentals",
                    "hours": hours_per_week * 4,
                    "milestone": "Complete time series forecasting project with SQL integration",
                    "skills_gained": ["Advanced ML", "Time series", "SQL", "Big data"]
                },
                {
                    "month": 6,
                    "focus": "Portfolio & Business Skills",
                    "topics": [
                        "End-to-end data science project",
                        "Business metrics and KPIs",
                        "Communicating insights to stakeholders",
                        "GitHub portfolio development"
                    ],
                    "prerequisites": "All previous months",
                    "hours": hours_per_week * 4,
                    "milestone": "Complete capstone project with full analysis and presentation",
                    "skills_gained": ["Business acumen", "Communication", "Portfolio"]
                }
            ],
            "final_goal": "Job-ready Data Scientist with business-oriented portfolio"
        }


class ContentRecommender:
    """
    Agent 3: Recommends daily learning content
    Adapts to learning style
    """

    def __init__(self, llm):
        print(f"{Colors.BLUE}  [Agent Content Recommender] Initializing Content Recommender...{Colors.RESET}")
        self.llm = llm
        print(f"{Colors.CYAN}     ✓ Recommender ready{Colors.RESET}")

    def recommend_daily_content(self, current_month: dict, learning_style: str, day: int = 1) -> str:
        """Generate today's personalized study plan"""
        print(f"{Colors.YELLOW}     → Creating Day {day} study plan for {learning_style} learner...{Colors.RESET}")

        prompt = f"""Create today's study plan:

CURRENT FOCUS: {current_month["focus"]}
TOPICS: {current_month["topics"]}
LEARNING STYLE: {learning_style}

Recommend for today (2-hour session):
1. Video tutorial (30-40 min) - suggest specific title/channel
2. Reading material (20-30 min) - article or documentation
3. Hands-on practice (60-70 min) - specific exercise or mini-project

Adapt recommendations for {learning_style} learners.
Be specific and practical."""

        recommendations = self.llm.invoke(prompt)
        return recommendations


class ProgressMonitor:
    """
    Agent 4: Monitors progress and adapts plan
    Provides feedback loop
    """

    def __init__(self, llm):
        print(f"{Colors.BLUE}  [Agent Progress Monitor] Initializing Progress Monitor...{Colors.RESET}")
        self.llm = llm
        self.student_progress = {}
        print(f"{Colors.CYAN}     ✓ Progress Monitor ready{Colors.RESET}")

    def track_completion(self, student_id: str, completed_item: dict):
        """Track completed learning items"""
        if student_id not in self.student_progress:
            self.student_progress[student_id] = []

        self.student_progress[student_id].append(completed_item)
        print(f"     ✅ Tracked: {completed_item['name']} (Score: {completed_item.get('score', 'N/A')})")

    def evaluate_progress(self, student_id: str, original_plan: dict, current_month: int) -> dict:
        """Evaluate if student is on track"""
        progress = self.student_progress.get(student_id, [])

        print(f"{Colors.YELLOW}     → Analyzing progress for Month {current_month}...{Colors.RESET}")

        prompt = f"""Evaluate student progress:

ORIGINAL PLAN (Month {current_month}):
Focus: {original_plan["months"][current_month-1]["focus"]}
Expected: {original_plan["months"][current_month-1]["topics"]}
Milestone: {original_plan["months"][current_month-1]["milestone"]}

COMPLETED SO FAR:
{json.dumps(progress, indent=2)}

Determine:
1. Status: ahead/on_track/behind/struggling
2. Should adjust plan: yes/no
3. Feedback message (encouraging)
4. Recommendations for next steps

Return as JSON."""

        evaluation = self.llm.invoke(prompt)
        return evaluation

    def adapt_plan(self, current_plan: dict, evaluation: str) -> dict:
        """Adapt plan based on progress"""
        if "behind" in evaluation.lower():
            print("     🔧 Adapting: Simplifying pace...")
        elif "ahead" in evaluation.lower():
            print("     🚀 Adapting: Adding advanced content...")

        return current_plan


def format_learning_path_output(result: dict, student_name: str):
    """Format the learning path results beautifully"""
    print(f"\n{Colors.MAGENTA}{Colors.BOLD}{'=' * 70}{Colors.RESET}")
    print(f"{Colors.MAGENTA}{Colors.BOLD}{' ' * 15}📊 LEARNING PATH RESULTS{Colors.RESET}")
    print(f"{Colors.MAGENTA}{Colors.BOLD}{' ' * 20}FOR {student_name.upper()}{Colors.RESET}")
    print(f"{Colors.MAGENTA}{Colors.BOLD}{'=' * 70}{Colors.RESET}\n")

    # Skills Assessment
    if "skills_assessment" in result:
        print(f"{Colors.BLUE}{Colors.BOLD}📊 SKILLS ASSESSMENT{Colors.RESET}")
        print(f"{Colors.BLUE}{'-' * 70}{Colors.RESET}\n")

        skills = result["skills_assessment"]

        for skill, level in skills.items():
            if isinstance(level, (int, float)) and 0 <= level <= 10:
                bar = "█" * int(level) + "░" * (10 - int(level))
                skill_name = skill.replace('_', ' ').title()

                # Color code based on level
                if level >= 7:
                    bar_color = Colors.GREEN
                elif level >= 4:
                    bar_color = Colors.YELLOW
                else:
                    bar_color = Colors.RED

                print(f"  {skill_name:.<30} {bar_color}[{bar}]{Colors.RESET} {level}/10")
            elif skill == "overall_level":
                level_display = str(level).upper()
                if "beginner" in str(level).lower():
                    color = Colors.YELLOW
                elif "intermediate" in str(level).lower():
                    color = Colors.CYAN
                else:
                    color = Colors.GREEN
                print(f"\n  {Colors.BOLD}Overall Level:{Colors.RESET} {color}{level_display}{Colors.RESET}")
            elif skill == "assessment_summary":
                print(f"  {Colors.CYAN}Summary:{Colors.RESET} {level}")

        print()

    # Learning Path
    if "learning_path" in result:
        path = result["learning_path"]

        print(f"\n{Colors.BLUE}{Colors.BOLD}🗺️  6-MONTH LEARNING PATH{Colors.RESET}")
        print(f"{Colors.BLUE}{'-' * 70}{Colors.RESET}")
        print(f"\n  {Colors.CYAN}Goal:{Colors.RESET} {path['goal']}")
        print(f"  {Colors.CYAN}Duration:{Colors.RESET} {path['duration']}")
        print(f"  {Colors.CYAN}Total Hours:{Colors.RESET} {path['total_hours']} hours ({path['hours_per_week']} hours/week)")
        print(f"  {Colors.CYAN}Difficulty:{Colors.RESET} {path.get('difficulty_level', 'N/A').title()}\n")

        for month in path["months"]:
            print(f"  {Colors.GREEN}{Colors.BOLD}📅 MONTH {month['month']}: {month['focus']}{Colors.RESET}")
            print(f"     {Colors.YELLOW}Topics:{Colors.RESET}")
            for topic in month['topics']:
                print(f"       • {topic}")
            print(f"     {Colors.YELLOW}Prerequisites:{Colors.RESET} {month['prerequisites']}")
            print(f"     {Colors.YELLOW}Time Investment:{Colors.RESET} {month['hours']} hours")
            print(f"     {Colors.GREEN}🎯 Milestone:{Colors.RESET} {month['milestone']}")
            print(f"     {Colors.CYAN}Skills Gained:{Colors.RESET} {', '.join(month['skills_gained'])}")
            print()

        print(f"  {Colors.MAGENTA}{Colors.BOLD}🏆 FINAL GOAL: {path['final_goal']}{Colors.RESET}\n")

    # First Week Content
    if "first_week_content" in result:
        print(f"{Colors.BLUE}{Colors.BOLD}📚 WEEK 1 STUDY PLAN{Colors.RESET}")
        print(f"{Colors.BLUE}{'-' * 70}{Colors.RESET}")
        content = result["first_week_content"]
        for line in content.split('\n'):
            if line.strip():
                print(f"  {line}")
        print()

    print(f"{Colors.MAGENTA}{Colors.BOLD}{'=' * 70}{Colors.RESET}\n")


class LearningPathSystem:
    """
    Complete Learning Path Generator
    Orchestrates all agents with feedback loops
    """

    def __init__(self):
        print(f"\n{Colors.CYAN}{Colors.BOLD}🔧 Initializing Learning Path System...{Colors.RESET}")
        print(f"{Colors.BLUE}{'-' * 70}{Colors.RESET}")

        # Initialize Llama 3.2 (shared)
        print("\n[Core] Connecting to Meta's Llama 3.2 via Ollama...")
        llm = Ollama(model="llama3.2", temperature=0.7)
        print("  ✓ Llama 3.2 8B connected")

        print("\n[Sub-Agents] Initializing specialized agents...")
        self.skills_agent = SkillsAssessmentAgent(llm)
        self.planner = LearningPathPlanner(llm)
        self.recommender = ContentRecommender(llm)
        self.monitor = ProgressMonitor(llm)

        print("\n" + "=" * 70)
        print(" " * 15 + "✅ SYSTEM FULLY OPERATIONAL")
        print("=" * 70 + "\n")

    def onboard_student(self, student_profile: dict) -> dict:
        """Complete student onboarding workflow"""
        print("\n" + "🎓" * 35)
        print(f" " * 15 + f"ONBOARDING: {student_profile['name']}")
        print("🎓" * 35 + "\n")

        # STEP 1: Skills Assessment
        print("[STEP 1/3] 📊 SKILLS ASSESSMENT")
        print(f"{Colors.BLUE}{'-' * 70}{Colors.RESET}")
        skills_matrix = self.skills_agent.assess(student_profile)
        print("  ✅ Skills assessed")
        print(f"     Overall level: {skills_matrix['overall_level'].upper()}")
        print(f"     Summary: {skills_matrix['assessment_summary']}\n")

        # STEP 2: Create Learning Path
        print("[STEP 2/3] 🗺️  LEARNING PATH CREATION")
        print(f"{Colors.BLUE}{'-' * 70}{Colors.RESET}")
        learning_path = self.planner.create_path(
            skills_matrix,
            goal=student_profile["goal"],
            hours_per_week=student_profile["hours_per_week"],
            overall_level=skills_matrix["overall_level"]
        )
        print("  ✅ 6-month personalized roadmap created")
        print(f"     Total hours: {learning_path['total_hours']}")
        print(f"     Goal: {learning_path['goal']}\n")

        # STEP 3: Generate First Week Content
        print("[STEP 3/3] 📚 CONTENT RECOMMENDATIONS")
        print(f"{Colors.BLUE}{'-' * 70}{Colors.RESET}")
        week1_content = self.recommender.recommend_daily_content(
            learning_path["months"][0],
            student_profile.get("learning_style", "hands-on"),
            day=1
        )
        print("  ✅ First week study plan ready\n")

        print("🎓" * 35)
        print(" " * 12 + "✅ ONBOARDING COMPLETE")
        print("🎓" * 35 + "\n")

        return {
            "skills_assessment": skills_matrix,
            "learning_path": learning_path,
            "first_week_content": week1_content
        }


def load_student_profile(file_path: str) -> dict:
    """Load student profile from JSON file"""
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        print(f"{Colors.RED}❌ Error: File not found - {file_path}{Colors.RESET}")
        return None
    except json.JSONDecodeError as e:
        print(f"{Colors.RED}❌ Error: Invalid JSON format - {str(e)}{Colors.RESET}")
        return None
    except Exception as e:
        print(f"{Colors.RED}❌ Error loading profile: {str(e)}{Colors.RESET}")
        return None


def get_manual_profile() -> dict:
    """Get student profile through manual input"""
    print(f"\n{Colors.YELLOW}{'=' * 70}{Colors.RESET}")
    print(" " * 20 + "📝 MANUAL PROFILE ENTRY")
    print(f"{Colors.YELLOW}{'=' * 70}{Colors.RESET}\n")

    name = input("Student name: ").strip()
    email = input("Email address: ").strip()
    background = input("Background (experience/education): ").strip()
    current_role = input("Current role: ").strip()
    goal = input("Learning goal: ").strip()

    while True:
        try:
            hours = int(input("Hours available per week: ").strip())
            break
        except ValueError:
            print(f"{Colors.RED}Please enter a valid number{Colors.RESET}")

    print("\nLearning style options: visual, hands-on, reading, mixed")
    learning_style = input("Preferred learning style: ").strip() or "hands-on"

    return {
        "name": name,
        "email": email,
        "background": background,
        "current_role": current_role,
        "goal": goal,
        "hours_per_week": hours,
        "learning_style": learning_style,
        "deadline": "6 months"
    }


def main():
    """Interactive demo of the learning path system"""

    # Initialize the system
    system = LearningPathSystem()

    print(f"\n{Colors.MAGENTA}{Colors.BOLD}{'=' * 70}{Colors.RESET}")
    print(f"{Colors.MAGENTA}{Colors.BOLD}{' ' * 20}INTERACTIVE MODE{Colors.RESET}")
    print(f"{Colors.MAGENTA}{Colors.BOLD}{'=' * 70}{Colors.RESET}")

    print("""
🎯 WHAT YOU CAN DO:

1️⃣  LOAD STUDENT PROFILE FROM FILES
   - Choose from sample profiles (beginner, intermediate, advanced)
   - Load your own JSON profile
   - See personalized learning paths instantly

2️⃣  MANUAL PROFILE ENTRY
   - Enter student information directly
   - Get customized recommendations

3️⃣  VIEW LEARNING PATH
   - See 6-month roadmap
   - Month-by-month breakdown
   - Weekly study plans

Commands:
   'load'   - Load profile from file (RECOMMENDED)
   'manual' - Enter profile manually
   'quit'   - Exit the system
""")

    print(f"{Colors.MAGENTA}{Colors.BOLD}{'=' * 70}{Colors.RESET}\n")

    while True:
        try:
            user_input = input(f"{Colors.CYAN}You: {Colors.RESET}").strip().lower()

            if user_input in ['quit', 'exit', 'q']:
                print(f"\n{Colors.MAGENTA}{Colors.BOLD}{'=' * 70}{Colors.RESET}")
                print(" " * 25 + "SESSION ENDED")
                print(f"{Colors.MAGENTA}{Colors.BOLD}{'=' * 70}{Colors.RESET}")
                print("\n🎓 Thank you for using the Learning Path Generator!")
                print("   Continue your learning journey!\n")
                break

            elif user_input == 'load':
                print(f"\n{Colors.YELLOW}{'=' * 70}{Colors.RESET}")
                print(" " * 20 + "📁 LOAD STUDENT PROFILE")
                print(f"{Colors.YELLOW}{'=' * 70}{Colors.RESET}\n")

                print("Choose an option:")
                print("  1. Beginner - Recent graduate seeking first job")
                print("  2. Intermediate - Developer transitioning to ML")
                print("  3. Advanced - Senior engineer moving to AI research")
                print("  4. Career Changer - Business analyst to Data Scientist")
                print("  5. Load from custom JSON file")
                print("  6. Cancel")

                choice = input("\nYour choice (1-6): ").strip()

                profile = None

                if choice == '1':
                    print(f"\n{Colors.CYAN}Loading beginner profile...{Colors.RESET}")
                    profile = load_student_profile("workshop2_sample_data/beginner_student.json")
                elif choice == '2':
                    print(f"\n{Colors.CYAN}Loading intermediate profile...{Colors.RESET}")
                    profile = load_student_profile("workshop2_sample_data/intermediate_student.json")
                elif choice == '3':
                    print(f"\n{Colors.CYAN}Loading advanced profile...{Colors.RESET}")
                    profile = load_student_profile("workshop2_sample_data/advanced_student.json")
                elif choice == '4':
                    print(f"\n{Colors.CYAN}Loading career changer profile...{Colors.RESET}")
                    profile = load_student_profile("workshop2_sample_data/career_changer.json")
                elif choice == '5':
                    file_path = input("\nEnter JSON file path: ").strip()
                    if not file_path:
                        print(f"{Colors.RED}No file path provided{Colors.RESET}")
                        continue
                    print(f"\n{Colors.CYAN}Loading from {file_path}...{Colors.RESET}")
                    profile = load_student_profile(file_path)
                elif choice == '6':
                    print(f"{Colors.YELLOW}Cancelled{Colors.RESET}")
                    continue
                else:
                    print(f"{Colors.RED}Invalid choice{Colors.RESET}")
                    continue

                if profile:
                    print(f"\n{Colors.GREEN}✅ Profile loaded successfully!{Colors.RESET}")
                    print(f"   Name: {profile['name']}")
                    print(f"   Goal: {profile['goal']}")
                    print(f"   Processing...\n")

                    # Onboard student
                    result = system.onboard_student(profile)

                    # Format and display results
                    format_learning_path_output(result, profile['name'])
                else:
                    print(f"\n{Colors.RED}Failed to load profile{Colors.RESET}")

            elif user_input == 'manual':
                profile = get_manual_profile()

                print(f"\n{Colors.GREEN}✅ Profile created! Processing...{Colors.RESET}\n")

                # Onboard student
                result = system.onboard_student(profile)

                # Format and display results
                format_learning_path_output(result, profile['name'])

            elif not user_input:
                continue

            else:
                print(f"{Colors.YELLOW}Unknown command. Try 'load', 'manual', or 'quit'{Colors.RESET}")

        except KeyboardInterrupt:
            print("\n\nExiting on user interrupt...")
            break
        except Exception as e:
            print(f"\n{Colors.RED}❌ Error occurred: {str(e)}{Colors.RESET}")
            print("Please try again.\n")


if __name__ == "__main__":
    main()
