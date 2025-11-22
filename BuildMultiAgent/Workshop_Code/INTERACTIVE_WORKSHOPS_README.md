# Interactive Workshop Files - Usage Guide

## Overview

These are **interactive versions** of both Session 12 workshops that take **USER INPUT** instead of running through static scenarios. Much more engaging for workshop participants!

---

## 📁 Files

- **`workshop1_interactive.py`** - Interactive College Admission Management System
- **`workshop2_interactive.py`** - Interactive Personalized Learning Path Generator  
- **`workshop1_admission_system.py`** - Original static version
- **`workshop2_learning_path_system.py`** - Original static version

---

## 🎓 Workshop 1: Interactive Admission Management System

### What's Different?

**Original `workshop1_admission_system.py`:**
- Hardcoded query and application for "Priya Sharma"
- Just watches the pipeline run

**NEW `workshop1_interactive.py`:**
- **Ask YOUR questions** about admissions
- **Submit YOUR application**
- **Interactive menu** system

### 📊 Static Data (In-Memory)

**FAQ Database:**
- deadline: November 30th, 2025
- fee: $50 (waiver available)  
- documents: Transcripts, ID, 2 rec letters, essay
- gpa: Minimum 3.0
- programs: CS, EE, ME
- housing: Available
- scholarships: Up to $5,000/year

**Programs:**
- CS: $10K/year, 4 years, careers: SWE, Data Scientist, AI Researcher
- EE: $10K/year, 4 years, careers: Electronics Engineer
- ME: $9.5K/year, 4 years, careers: Mechanical Designer, Robotics Engineer

**Eligibility Criteria:**
- Min GPA: 3.0
- Required subjects: Math, Physics
- Min essay score: 6/10

### 🚀 How to Run

```bash
python workshop1_interactive.py
```

### Commands:
- Type any question: "What is the deadline?"
- Type `info`: See all available data
- Type `apply`: Submit application
- Type `quit`: Exit

---

## 📚 Workshop 2: Interactive Learning Path Generator

### What's Different?

**Original `workshop2_learning_path_system.py`:**
- Hardcoded profile for "Priya Sharma"
- Predefined skill levels

**NEW `workshop2_interactive.py`:**
- **Enter YOUR profile** and goals
- **Rate YOUR skills** (0-10)
- **Get YOUR path** customized to you

### 📊 Static Data (In-Memory)

**Skill Areas (6):**
- Python Programming
- Algorithms & Problem Solving
- Data Structures  
- Machine Learning
- Deep Learning
- Mathematics

**Learning Paths (4 templates):**
1. ML Beginner (ML skills < 3)
2. ML Intermediate (ML skills 3-6)
3. ML Advanced (ML skills > 6)
4. General Dev (non-ML goals)

**Learning Styles:**
- visual, hands-on, reading, mixed

### 🚀 How to Run

```bash
python workshop2_interactive.py
```

### Process:
1. Enter your profile info
2. Rate your 6 skills (0-10)
3. Get personalized 6-month roadmap
4. Receive first week study plan

---

## 💡 Key Improvements

| Feature | Original | Interactive |
|---------|----------|-------------|
| Input | Hardcoded | YOUR data |
| Output | Fixed | Personalized |
| Experience | Watch | Participate |
| Scenarios | One | Multiple |

---

## 🎯 Quick Test Examples

### Workshop 1:
```
You: info
You: What is the CS program fee?
You: quit
```

### Workshop 2:
```
Name: Test User
Goal: Learn Machine Learning
Hours/week: 10
Skills: 7,6,6,3,2,5
```

---

## ✅ Files Ready

- ✓ Syntax validated
- ✓ Colors optimized
- ✓ Warnings suppressed
- ✓ Multi-line input support
- ✓ Error handling

See **QUICK_START.md** for fast testing guide!
