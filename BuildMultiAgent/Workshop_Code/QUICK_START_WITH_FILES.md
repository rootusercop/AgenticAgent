# Quick Start - Workshop 1 with File Loading

## 🚀 Fastest Way to Run

```bash
python workshop1_interactive_with_files.py
```

Type: **`file`** → Choose: **`1`**

Done! Watch the 4 agents process a complete application in ~30 seconds.

---

## 📁 What You Get

### **3 Ways to Load Data:**

1. **Sample Files (RECOMMENDED)**
   - Strong candidate (high GPA, excellent recs)
   - Borderline candidate (meets minimums)
   - Instant processing, realistic results

2. **JSON File**
   - `sample_data/sample_applications.json`
   - Both candidates in structured format
   - Easy to edit and extend

3. **Your Own Files**
   - Create 3 text files: transcript.txt, recommendation.txt, essay.txt
   - No special format needed
   - LLM extracts information automatically

---

## 📂 Sample Files Provided

```
sample_data/
├── strong_candidate_transcript.txt
├── strong_candidate_recommendation.txt  
├── strong_candidate_essay.txt
├── borderline_candidate_transcript.txt
├── borderline_candidate_recommendation.txt
├── borderline_candidate_essay.txt
└── sample_applications.json
```

**All tested and working!**

---

## 💡 Quick Commands

| Command | What It Does |
|---------|--------------|
| `file` | Load from files (RECOMMENDED) |
| `info` | Show available FAQ topics |
| `apply` | Type application manually |
| Ask question | Query agent directly |
| `quit` | Exit |

---

## 🎯 For Workshop Demo

**Step 1:** Run the script
```bash
python workshop1_interactive_with_files.py
```

**Step 2:** Type `file` and choose `1` (strong candidate)

**Step 3:** Watch agents process:
- 📄 Document Processor extracts data
- 📊 Eligibility Evaluator calculates score  
- 📧 Communication Manager generates email

**Step 4:** Type `file` and choose `2` (borderline candidate)

**Step 5:** Compare the two outcomes!

**Total time:** ~5 minutes for complete demo

---

## 📝 Create Your Own Files

### Example: transcript.txt
```
Student: Your Name
GPA: 3.5 / 4.0
Subjects: Math (A), Physics (B), CS (A)
Graduation: June 2025
```

### Example: recommendation.txt
```
To Admissions,

I taught this student for 2 years.

They demonstrate:
- Strong technical skills
- Good work ethic
- Leadership potential

I recommend them.

Prof. Name
```

### Example: essay.txt
```
Why I Want to Study CS

[Your essay content here]
```

---

## ✅ What Works

- ✓ Plain text files (.txt)
- ✓ JSON files (.json)
- ✓ Any format - LLM extracts data
- ✓ No strict structure required
- ✓ Works with copy-pasted content

---

## 🎓 Tell Participants

> **"Three ways to use this system:**
>
> **DEMO MODE:**
> Type `file` → Choose 1 or 2 → Instant results
>
> **YOUR FILES:**
> Create 3 simple text files → Load them → Get personalized results
>
> **MANUAL:**
> Type `apply` → Enter data directly
>
> **Try the demo first:** Takes 30 seconds, shows all 4 agents working!"

---

## 📖 More Details

See **FILE_LOADING_GUIDE.md** for:
- Complete file format specifications
- Troubleshooting tips
- Advanced JSON usage
- What data to include

---

## 🎉 Ready!

**Start now:** `python workshop1_interactive_with_files.py`

Type `file` and choose `1` to see it work immediately!
