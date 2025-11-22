"""
Session 12 - Workshop 2: INTERACTIVE Personalized Learning Path Generator
Multi-Agent System with Feedback Loops

Interactive Features:
1. Skills Assessment Agent - Test your skills interactively
2. Learning Path Planner - Get personalized roadmap based on YOUR inputs
3. Content Recommender - Daily study plans tailored to you
4. Progress Monitor - Track and adapt YOUR progress

Using: Meta's Llama 3.2 8B via Ollama
"""

# Suppress urllib3 NotOpenSSLWarning on macOS
import warnings
warnings.filterwarnings('ignore', message='.*OpenSSL.*')

from langchain.agents import initialize_agent, AgentType
from langchain_community.llms import Ollama
from langchain.tools import Tool
import json

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

separator = "=" * 70
print(f"{Colors.MAGENTA}{Colors.BOLD}{separator}{Colors.RESET}")
print(" " * 10 + "SESSION 12 - WORKSHOP 2 (INTERACTIVE)")
print(" " * 5 + "PERSONALIZED LEARNING PATH GENERATOR")
print(f"{Colors.MAGENTA}{Colors.BOLD}{separator}{Colors.RESET}")
print("\n🎯 AI-Powered Adaptive Learning System")
print("   Model: Meta's Llama 3.2 via Ollama")
print("=" * 70 + "\n")


class SkillsAssessmentAgent:
    """
    Agent 1: Assesses student's current skill level
    Tools: Code challenges, concept quizzes
    """

    def __init__(self, llm):
        print(f"{Colors.BLUE}  [Agent Skills Assessment Agent] Initializing Skills Assessment Agent...{Colors.RESET}")
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

    def assess_interactively(self) -> dict:
        """Interactive skill assessment"""
        print(f"\n{Colors.YELLOW}{Colors.BOLD}📊 INTERACTIVE SKILLS ASSESSMENT{Colors.RESET}")
        print(f"{Colors.BLUE}{'=' * 70}{Colors.RESET}\n")

        print("Please rate your skills on a scale of 0-10 (0=beginner, 10=expert):\n")

        skills = {}
        skill_areas = [
            ("python", "Python Programming"),
            ("algorithms", "Algorithms & Problem Solving"),
            ("data_structures", "Data Structures"),
            ("machine_learning", "Machine Learning"),
            ("deep_learning", "Deep Learning"),
            ("mathematics", "Mathematics (Linear Algebra, Calculus, Stats)")
        ]

        for skill_key, skill_name in skill_areas:
            while True:
                try:
                    rating = input(f"  {skill_name}: ")
                    rating = int(rating)
                    if 0 <= rating <= 10:
                        skills[skill_key] = rating
                        break
                    else:
                        print(f"  {Colors.RED}Please enter a number between 0 and 10{Colors.RESET}")
                except ValueError:
                    print(f"  {Colors.RED}Please enter a valid number{Colors.RESET}")

        # Calculate overall level
        avg_score = sum(skills.values()) / len(skills)
        if avg_score < 3:
            overall_level = "beginner"
        elif avg_score < 7:
            overall_level = "intermediate"
        else:
            overall_level = "advanced"

        skills["overall_level"] = overall_level
        skills["assessment_summary"] = self._generate_summary(skills, overall_level)

        return skills

    def _generate_summary(self, skills: dict, level: str) -> str:
        """Generate assessment summary"""
        summaries = {
            "beginner": "You're at the beginning of your journey. Focus on building strong fundamentals!",
            "intermediate": "Strong foundation established. Ready to dive deeper into specialized areas!",
            "advanced": "Excellent technical skills. Ready for advanced projects and leadership!"
        }
        return summaries.get(level, "Assessment complete!")


class LearningPathPlanner:
    """
    Agent 2: Creates personalized learning paths
    Uses Llama 3.2 for intelligent planning
    """

    def __init__(self, llm):
        print(f"{Colors.BLUE}  [Agent Learning Path Planner] Initializing Learning Path Planner...{Colors.RESET}")
        self.llm = llm
        print(f"{Colors.CYAN}     ✓ Path Planner ready{Colors.RESET}")

    def create_path(self, skills_matrix: dict, goal: str, hours_per_week: int) -> dict:
        """Create customized 6-month learning roadmap"""
        print(f"{Colors.YELLOW}     → Generating personalized learning path...{Colors.RESET}")

        # Generate structured path based on goal and skills
        return self._generate_structured_path(skills_matrix, goal, hours_per_week)

    def _generate_structured_path(self, skills: dict, goal: str, hours_per_week: int) -> dict:
        """Generate structured learning path based on skills and goal"""

        # Determine starting point based on current skills
        avg_ml_skill = (skills.get("machine_learning", 0) + skills.get("deep_learning", 0)) / 2

        if "machine learning" in goal.lower() or "ml" in goal.lower():
            if avg_ml_skill < 3:
                months = self._get_ml_beginner_path(hours_per_week)
            elif avg_ml_skill < 6:
                months = self._get_ml_intermediate_path(hours_per_week)
            else:
                months = self._get_ml_advanced_path(hours_per_week)
        else:
            months = self._get_general_dev_path(hours_per_week)

        return {
            "duration": "6 months",
            "total_hours": hours_per_week * 4 * 6,
            "hours_per_week": hours_per_week,
            "goal": goal,
            "months": months,
            "final_goal": f"Achieve proficiency in {goal}"
        }

    def _get_ml_beginner_path(self, hours_per_week):
        return [
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
        ]

    def _get_ml_intermediate_path(self, hours_per_week):
        return [
            {
                "month": 1,
                "focus": "Advanced Machine Learning",
                "topics": ["Ensemble methods", "Feature engineering", "Model optimization", "Advanced scikit-learn"],
                "prerequisites": "ML basics",
                "hours": hours_per_week * 4,
                "milestone": "Win Kaggle competition or achieve top 10%",
                "skills_gained": ["Advanced ML", "Feature Engineering"]
            },
            {
                "month": 2,
                "focus": "Deep Learning Architectures",
                "topics": ["CNNs", "RNNs", "Transformers", "Attention mechanisms"],
                "prerequisites": "Neural network basics",
                "hours": hours_per_week * 4,
                "milestone": "Implement 3 architectures from scratch",
                "skills_gained": ["Deep Learning", "PyTorch"]
            },
            {
                "month": 3,
                "focus": "Natural Language Processing",
                "topics": ["BERT", "GPT", "Text generation", "Fine-tuning LLMs"],
                "prerequisites": "DL architectures",
                "hours": hours_per_week * 4,
                "milestone": "Build custom NLP application",
                "skills_gained": ["NLP", "Transformers", "LLMs"]
            },
            {
                "month": 4,
                "focus": "Computer Vision Advanced",
                "topics": ["Object detection", "Segmentation", "GANs", "Diffusion models"],
                "prerequisites": "CNNs",
                "hours": hours_per_week * 4,
                "milestone": "Create image generation model",
                "skills_gained": ["Computer Vision", "GANs"]
            },
            {
                "month": 5,
                "focus": "MLOps & Production",
                "topics": ["Model serving", "A/B testing", "Monitoring", "CI/CD for ML"],
                "prerequisites": "Model building",
                "hours": hours_per_week * 4,
                "milestone": "Deploy production ML pipeline",
                "skills_gained": ["MLOps", "DevOps"]
            },
            {
                "month": 6,
                "focus": "Specialization & Portfolio",
                "topics": ["Choose specialization", "Build portfolio", "Contribute to open source", "Interview prep"],
                "prerequisites": "All previous",
                "hours": hours_per_week * 4,
                "milestone": "Complete portfolio with 3 impressive projects",
                "skills_gained": ["Portfolio", "Specialization"]
            }
        ]

    def _get_ml_advanced_path(self, hours_per_week):
        return [
            {
                "month": 1,
                "focus": "Research & Latest Papers",
                "topics": ["Reading research papers", "State-of-the-art models", "Reproducing papers"],
                "prerequisites": "Strong ML/DL foundation",
                "hours": hours_per_week * 4,
                "milestone": "Reproduce 2 recent papers",
                "skills_gained": ["Research", "Paper Implementation"]
            },
            {
                "month": 2,
                "focus": "Specialized Domain Deep Dive",
                "topics": ["Choose: NLP/CV/RL", "Advanced techniques", "Custom architectures"],
                "prerequisites": "Research skills",
                "hours": hours_per_week * 4,
                "milestone": "Novel architecture implementation",
                "skills_gained": ["Specialization", "Innovation"]
            },
            {
                "month": 3,
                "focus": "Large Scale ML Systems",
                "topics": ["Distributed training", "Model optimization", "Serving at scale"],
                "prerequisites": "ML systems knowledge",
                "hours": hours_per_week * 4,
                "milestone": "Build scalable ML system",
                "skills_gained": ["Distributed ML", "Optimization"]
            },
            {
                "month": 4,
                "focus": "AI Safety & Ethics",
                "topics": ["Bias in AI", "Fairness", "Interpretability", "Responsible AI"],
                "prerequisites": "Production experience",
                "hours": hours_per_week * 4,
                "milestone": "Implement fairness framework",
                "skills_gained": ["AI Ethics", "Interpretability"]
            },
            {
                "month": 5,
                "focus": "Contribution & Leadership",
                "topics": ["Open source contribution", "Technical writing", "Mentoring"],
                "prerequisites": "Strong expertise",
                "hours": hours_per_week * 4,
                "milestone": "Major open source contribution",
                "skills_gained": ["Leadership", "Communication"]
            },
            {
                "month": 6,
                "focus": "Career Advancement",
                "topics": ["Building personal brand", "Speaking at conferences", "Advanced interviews"],
                "prerequisites": "Proven track record",
                "hours": hours_per_week * 4,
                "milestone": "Land senior ML role or research position",
                "skills_gained": ["Career", "Networking"]
            }
        ]

    def _get_general_dev_path(self, hours_per_week):
        return [
            {
                "month": 1,
                "focus": "Advanced Programming Fundamentals",
                "topics": ["Design patterns", "Clean code", "Testing", "Git workflows"],
                "prerequisites": "Basic programming",
                "hours": hours_per_week * 4,
                "milestone": "Build well-architected application",
                "skills_gained": ["Design Patterns", "Testing"]
            },
            {
                "month": 2,
                "focus": "Backend Development",
                "topics": ["APIs", "Databases", "Authentication", "Caching"],
                "prerequisites": "Programming fundamentals",
                "hours": hours_per_week * 4,
                "milestone": "Build full-featured API",
                "skills_gained": ["Backend", "APIs"]
            },
            {
                "month": 3,
                "focus": "Frontend Development",
                "topics": ["React/Vue", "State management", "UI/UX", "Responsive design"],
                "prerequisites": "HTML/CSS/JS basics",
                "hours": hours_per_week * 4,
                "milestone": "Build interactive web application",
                "skills_gained": ["Frontend", "React"]
            },
            {
                "month": 4,
                "focus": "DevOps & Cloud",
                "topics": ["Docker", "Kubernetes", "CI/CD", "AWS/GCP"],
                "prerequisites": "Application development",
                "hours": hours_per_week * 4,
                "milestone": "Deploy application to cloud",
                "skills_gained": ["DevOps", "Cloud"]
            },
            {
                "month": 5,
                "focus": "System Design",
                "topics": ["Scalability", "Load balancing", "Microservices", "Caching strategies"],
                "prerequisites": "Backend + DevOps",
                "hours": hours_per_week * 4,
                "milestone": "Design scalable system architecture",
                "skills_gained": ["System Design", "Architecture"]
            },
            {
                "month": 6,
                "focus": "Specialization & Portfolio",
                "topics": ["Choose focus area", "Build projects", "Interview preparation"],
                "prerequisites": "Full stack knowledge",
                "hours": hours_per_week * 4,
                "milestone": "Complete portfolio and land job",
                "skills_gained": ["Specialization", "Portfolio"]
            }
        ]


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


class LearningPathSystem:
    """
    Complete Learning Path Generator
    Orchestrates all agents with feedback loops
    """

    def __init__(self):
        print(f"\n{Colors.CYAN}{Colors.BOLD}🔧 Initializing Learning Path System...{Colors.RESET}")
        dash_line = "-" * 70
        print(f"{Colors.BLUE}{dash_line}{Colors.RESET}")

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
        dash_line = "-" * 70
        print(f"{Colors.BLUE}{dash_line}{Colors.RESET}")
        skills_matrix = self.skills_agent.assess_interactively()
        print("  ✅ Skills assessed")
        print(f"     Overall level: {skills_matrix['overall_level'].upper()}")
        print(f"     Summary: {skills_matrix['assessment_summary']}\n")

        # STEP 2: Create Learning Path
        print("[STEP 2/3] 🗺️  LEARNING PATH CREATION")
        dash_line = "-" * 70
        print(f"{Colors.BLUE}{dash_line}{Colors.RESET}")
        learning_path = self.planner.create_path(
            skills_matrix,
            goal=student_profile["goal"],
            hours_per_week=student_profile["hours_per_week"]
        )
        print("  ✅ 6-month personalized roadmap created")
        print(f"     Total hours: {learning_path['total_hours']}")
        print(f"     Goal: {learning_path['goal']}\n")

        # STEP 3: Generate First Week Content
        print("[STEP 3/3] 📚 CONTENT RECOMMENDATIONS")
        dash_line = "-" * 70
        print(f"{Colors.BLUE}{dash_line}{Colors.RESET}")
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


def main():
    """Interactive demo of the learning path system"""

    # Initialize system
    system = LearningPathSystem()

    print(f"\n{Colors.MAGENTA}{Colors.BOLD}{'=' * 70}{Colors.RESET}")
    print(f"{Colors.MAGENTA}{Colors.BOLD}{' ' * 20}INTERACTIVE MODE{Colors.RESET}")
    print(f"{Colors.MAGENTA}{Colors.BOLD}{'=' * 70}{Colors.RESET}")

    print("""
🎯 CREATE YOUR PERSONALIZED LEARNING PATH

This system will:
1. Assess your current skills interactively
2. Create a personalized 6-month learning roadmap
3. Generate customized daily study plans
4. Track your progress and adapt the plan

Let's get started!
""")

    print(f"{Colors.MAGENTA}{Colors.BOLD}{'=' * 70}{Colors.RESET}\n")

    # Gather student information
    print(f"{Colors.YELLOW}📝 STUDENT INFORMATION{Colors.RESET}")
    print(f"{Colors.BLUE}{'=' * 70}{Colors.RESET}\n")

    name = input("Your name: ").strip()
    background = input("Your background (e.g., '2 years Python, built web apps'): ").strip()
    current_role = input("Current role/status (e.g., 'Software Developer', 'Student'): ").strip()
    goal = input("Your goal (e.g., 'Become Machine Learning Engineer'): ").strip()

    while True:
        try:
            hours_per_week = int(input("Hours you can dedicate per week: ").strip())
            if hours_per_week > 0:
                break
            else:
                print(f"{Colors.RED}Please enter a positive number{Colors.RESET}")
        except ValueError:
            print(f"{Colors.RED}Please enter a valid number{Colors.RESET}")

    print("\nLearning styles: visual, hands-on, reading, mixed")
    learning_style = input("Your preferred learning style: ").strip() or "hands-on"

    student_profile = {
        "name": name,
        "background": background,
        "current_role": current_role,
        "goal": goal,
        "hours_per_week": hours_per_week,
        "learning_style": learning_style
    }

    print(f"\n{Colors.GREEN}✅ Profile created! Starting onboarding...{Colors.RESET}\n")

    # Onboard student
    result = system.onboard_student(student_profile)

    # Display results
    print("\n" + "📊" * 35)
    print(" " * 20 + "YOUR LEARNING PATH")
    print("📊" * 35)

    # Skills Assessment
    print("\n📊 YOUR SKILLS ASSESSMENT")
    dash_line = "-" * 70
    print(f"{Colors.BLUE}{dash_line}{Colors.RESET}")
    for skill, level in result["skills_assessment"].items():
        if isinstance(level, (int, float)):
            bar = "█" * level + "░" * (10 - level)
            print(f"  {skill.replace('_', ' ').title():.<30} [{bar}] {level}/10")
        else:
            print(f"  {skill.replace('_', ' ').title()}: {level}")

    # Learning Path
    print("\n\n🗺️  YOUR 6-MONTH LEARNING PATH")
    dash_line = "-" * 70
    print(f"{Colors.BLUE}{dash_line}{Colors.RESET}")
    for month in result["learning_path"]["months"]:
        print(f"\n  📅 MONTH {month['month']}: {month['focus']}")
        print(f"     Topics:")
        for topic in month['topics']:
            print(f"       • {topic}")
        print(f"     Hours: {month['hours']}")
        print(f"     🎯 Milestone: {month['milestone']}")

    # This Week's Content
    print("\n\n📚 YOUR FIRST WEEK'S STUDY PLAN")
    dash_line = "-" * 70
    print(f"{Colors.BLUE}{dash_line}{Colors.RESET}")
    print(result["first_week_content"])

    print(f"\n\n{Colors.MAGENTA}{Colors.BOLD}{'=' * 70}{Colors.RESET}")
    print(" " * 15 + "🎉 YOUR PATH IS READY!")
    print(f"{Colors.MAGENTA}{Colors.BOLD}{'=' * 70}{Colors.RESET}")
    print(f"""
{Colors.GREEN}✅ You now have:{Colors.RESET}
   - Personalized skills assessment
   - 6-month customized learning roadmap
   - Week 1 study plan tailored to your learning style
   - Total commitment: {result["learning_path"]["total_hours"]} hours over 6 months

{Colors.YELLOW}💡 Next Steps:{Colors.RESET}
   1. Save this learning path
   2. Follow Month 1 curriculum
   3. Track your progress
   4. Adjust as you learn and grow

{Colors.CYAN}🚀 You're ready to start your learning journey!{Colors.RESET}
""")
    print("=" * 70 + "\n")


if __name__ == "__main__":
    main()
