# Workshop 1 - File Loading Guide

## 🎯 Quick Start (RECOMMENDED)

The **easiest way** to run Workshop 1 is to use the sample data files:

```bash
python workshop1_interactive_with_files.py
```

Then type: **`file`**

---

## 📁 What Files Are Provided

### Sample Data Folder Structure:
```
sample_data/
├── strong_candidate_transcript.txt           (GPA 3.9, excellent)
├── strong_candidate_recommendation.txt       (Top 1% recommendation)
├── strong_candidate_essay.txt                (Strong, passionate)
├── borderline_candidate_transcript.txt       (GPA 3.1, meets minimum)
├── borderline_candidate_recommendation.txt   (Good, shows potential)
├── borderline_candidate_essay.txt            (Adequate)
└── sample_applications.json                  (Both in JSON format)
```

---

## 🚀 How to Use

### **Option 1: Use Sample Files (Fastest)**

1. Run: `python workshop1_interactive_with_files.py`
2. Type: `file`
3. Choose option **1** (strong candidate) or **2** (borderline candidate)
4. Watch the 4 agents process the application automatically!

**Result:** Complete processing in ~30 seconds with realistic data

---

### **Option 2: Use JSON File**

1. Run: `python workshop1_interactive_with_files.py`
2. Type: `file`
3. Choose option **3** (Load from JSON)
4. Enter: `sample_data/sample_applications.json`
5. Select which application to process

**JSON Format:**
```json
{
  "strong_candidate": {
    "email": "sarah.johnson@email.com",
    "documents": {
      "transcript": "Full transcript text...",
      "recommendation": "Full recommendation text...",
      "essay": "Full essay text..."
    }
  }
}
```

---

### **Option 3: Use Your Own Text Files**

**Create 3 text files:**

**1. transcript.txt** - Example:
```
Student: John Doe
GPA: 3.5 / 4.0
Subjects: Mathematics (A), Physics (B+), Computer Science (A), Chemistry (B)
Graduation: June 2025
```

**2. recommendation.txt** - Example:
```
To the Admissions Committee,

I have taught John in Computer Science for two years.

John demonstrates:
- Strong programming skills
- Good work ethic
- Team collaboration

I recommend John for your program.

Sincerely,
Prof. Jane Smith
```

**3. essay.txt** - Example:
```
My Interest in Computer Science

I became interested in CS when I took my first programming class...
[Your essay content here]
```

**Then run:**
1. `python workshop1_interactive_with_files.py`
2. Type: `file`
3. Choose option **4** (your own files)
4. Enter file paths when prompted

---

## 📋 What Data to Put in Files

### **Transcript File Must Include:**
- Student name
- GPA (out of 4.0)
- Subjects with grades
- Graduation date

**The agent extracts:** GPA (number), subjects (list), graduation year

---

### **Recommendation Letter Should Include:**
- Relationship to student
- Student strengths (2-3 points)
- Recommendation statement
- Recommender name and title

**The agent creates:** 3-bullet point summary

---

### **Essay Should Include:**
- Personal story/motivation
- Relevant experiences
- Why this program
- Future goals

**The agent analyzes:** Main themes, writing quality (1-10), authenticity (1-10)

---

## ✅ Testing the System

### **Test 1: Strong Candidate (Should be ACCEPTED)**
```
You: file
Choose: 1

Expected: High eligibility score, acceptance email
```

### **Test 2: Borderline Candidate (May be WAITLISTED)**
```
You: file
Choose: 2

Expected: Medium score, conditional acceptance or suggestions
```

### **Test 3: Compare Both**
Run both samples to see different outcomes!

---

## 🎓 For Workshop Presentations

### **Demo Flow:**

**1. Show sample files first (2 mins)**
```bash
cat sample_data/strong_candidate_transcript.txt
```
Let participants see what real data looks like

**2. Run with strong candidate (3 mins)**
```
python workshop1_interactive_with_files.py
> file
> 1
```
Show full 4-agent pipeline processing

**3. Explain what happened (3 mins)**
- Agent 1: Query Handler (didn't use in this flow)
- Agent 2: Document Processor (extracted structured data)
- Agent 3: Eligibility Evaluator (calculated score)
- Agent 4: Communication Manager (generated personalized email)

**4. Run borderline candidate (2 mins)**
```
> file
> 2
```
Show different outcome with different data

**5. Q&A and customization (5 mins)**
- Participants can edit sample files
- Re-run to see different results
- Show how to create their own files

**Total: ~15 minutes for complete demo**

---

## 📊 File Format Requirements

### **Text Files (.txt)**
- ✅ Plain text, any format
- ✅ Agent uses LLM to extract information
- ✅ Flexible - doesn't require specific structure
- ✅ Works with copy-pasted content

### **JSON Files (.json)**
- ✅ Must be valid JSON format
- ✅ Must have "email" and "documents" keys
- ✅ Documents must have "transcript", "recommendation", "essay"
- ✅ Can include multiple applications in one file

---

## 🔧 Troubleshooting

### **Error: File not found**
- Check file path is correct
- Use relative path from script location: `sample_data/filename.txt`
- Or use absolute path: `/full/path/to/file.txt`

### **Error: Invalid JSON**
- Validate JSON at jsonlint.com
- Check all quotes are escaped properly
- Check all commas and brackets match

### **Agent produces weird results**
- Check input data is clear and readable
- Llama 3.2 works best with well-formatted text
- Add more detail if data is too sparse

---

## 💡 Tips

**For Workshops:**
- ✅ Use sample files (option 1 or 2) for demos
- ✅ Let participants edit samples and re-run
- ✅ Show JSON format for programmatic access

**For Real Use:**
- ✅ Create template files participants can fill in
- ✅ Use JSON for batch processing multiple applications
- ✅ Text files are easier for non-technical users

**For Testing:**
- ✅ Create variations: high GPA, low essay quality, etc.
- ✅ Test edge cases: minimum GPA, missing subjects
- ✅ Compare results across different profiles

---

## 🎯 Summary

**Three ways to input data:**
1. **Sample files** - Instant demo ⚡
2. **Your text files** - Easy to create 📝
3. **JSON files** - Programmatic/batch 🔧

**All work with the same agent pipeline:**
Document Processing → Eligibility Evaluation → Communication

**No special parsing needed - LLM handles everything!**

---

## 📞 What to Tell Workshop Participants

> **"This system can process applications in 3 ways:**
>
> **1. SAMPLE DATA (Fastest):**
> - Type `file` and choose option 1 or 2
> - See instant results with realistic data
> - Perfect for understanding the flow
>
> **2. YOUR FILES (Flexible):**
> - Create 3 simple text files
> - No special format needed
> - LLM extracts information automatically
>
> **3. JSON FORMAT (Advanced):**
> - Structured data in one file
> - Good for batch processing
> - Programmatic access
>
> **The agents process:**
> - Transcripts → Extract GPA, subjects, graduation
> - Recommendations → Summarize in 3 points
> - Essays → Analyze themes and quality
>
> **Try it now:** `python workshop1_interactive_with_files.py` then type `file`"

---

## ✅ Files Ready to Use

All sample files are tested and work correctly:
- ✓ Strong candidate (high acceptance probability)
- ✓ Borderline candidate (conditional acceptance)
- ✓ JSON format (both candidates)
- ✓ Easy to modify and re-run

**Start with:** `python workshop1_interactive_with_files.py` → type `file` → choose `1`
