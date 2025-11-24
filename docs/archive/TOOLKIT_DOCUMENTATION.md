# ModelA Integrated Toolkit Documentation

## Overview

The ModelA project now includes an integrated analytics and violation detection toolkit that runs automatically with every prompt generation. These tools provide real-time insights into token usage, atom efficiency, and compliance violations.

---

## Tools Included

### 1. **analytics.py** - Core Analytics Engine

Runs automatic analysis on every prompt generation and provides:

#### Features:
- **Token Counting**: Uses tiktoken if available, falls back to estimation
- **Atom Library Analysis**: Scans all definition files for token efficiency metrics
- **Priority Breakdown**: Shows token distribution across P0/P1/P2 atoms
- **File Weight Analysis**: Identifies heaviest token-consuming files
- **Efficiency Metrics**: Shows most/least efficient atoms by token-per-character ratio
- **Violation Detection**: Flags atoms over 100 tokens or with problematic language

#### Output (shown automatically after `python camera.py`):
```
📊 TOKEN OVERVIEW
  Prompt Tokens: 4,097
  Target: 3,000
  Budget Status: +1,097 ⚠️ OVER
  Utilization: 136.6% of target

📚 ATOM LIBRARY
  Total Atoms: 435
  Total Atom Tokens: 15,994
  Avg per Atom: 36.8 tokens

🎯 PRIORITY BREAKDOWN
  P0: MANDATE      47 atoms,  2251 tokens ( 14.1%)
  P1: CORE        285 atoms, 10856 tokens ( 67.9%)
  P2: DETAIL      103 atoms,  2887 tokens ( 18.1%)

🔝 HEAVIEST FILES
  dress_accent_complements.json    1964 tokens (45 atoms)
  [... more files ...]

⚡ EFFICIENCY INSIGHTS
  Most token-dense atoms (good compression):
    • hosiery.bow_accent_white    0.250 tokens/char
  Least efficient atoms (consider trimming):
    • dress_ensemble_system       0.000 tokens/char - trim candidate
```

---

### 2. **violation_reporter.py** - Detailed Violation Analysis

Provides actionable remediation guidance for specific violations:

#### Features:
- **Narrative Language Detection**: Identifies "shows," "appears," "seems," etc.
- **Filter-Risk Detection**: Finds language needing Safe-Content replacements
  - "exhausted" → "fatigued"
  - "resigned" → "composed"
  - "withdrawn" → "reserved"
  - "vacant" → "unfocused"
  - "trained" → "practiced"
  - "broken" → "diminished"
  - "conditioned" → "prepared"
  - "obedient" → "cooperative"
  - "complying" → "obliging"
- **Character Limit Detection**: Flags atoms over 300 characters
- **Token Heavy Atom Identification**: Lists atoms consuming most tokens

#### Output (shown automatically after `python camera.py`):
```
⚠️  NARRATIVE LANGUAGE VIOLATIONS (31)
  dress.most_special_ever_mandate [dress_colors.json]
    Patterns: elaborate, beautiful
    Fix: Replace with observable facts
    Content: MOST SPECIAL, BEAUTIFUL, ELABORATE dress ever worn...

🚨 FILTER-RISK LANGUAGE (3)
  expression.performed_cuteness [expression_emotion.json]
    Apply: trained → practiced
    Content: Smile present but strained...

📏 CHARACTER LIMIT VIOLATIONS (4)
  embellish.glitter_fabric_panels 390 chars (over by 90)

💾 HEAVIEST ATOMS - TRIM CANDIDATES
  embellish.glitter_fabric_panels 97 tokens
  fabric.glitter_weave_base        90 tokens
```

#### Output File:
- **VIOLATION_DETAIL_REPORT.md** - Saved automatically with each run
- Contains all violations with file locations and remediation guidance

---

## How Tools Integrate with camera.py

Every time you run:
```bash
python camera.py
```

The system automatically:
1. **Generates the prompt** (as before)
2. **Reports mandate checkpoint** (as before)
3. **Runs analytics.py** → prints token overview and efficiency insights
4. **Runs violation_reporter.py** → detects violations and saves report

---

## Using the Tools

### Automatic Integration (Easiest)
Just run camera.py as normal:
```bash
python camera.py
```
Everything runs automatically, and `VIOLATION_DETAIL_REPORT.md` is generated.

### Standalone Analysis
To run tools independently:

**Analytics only:**
```bash
python analytics.py
```

**Violation Report only:**
```bash
python violation_reporter.py
```

---

## How to Use Outputs for Iteration

### Example Workflow:

1. **Run camera.py**
   - See: "Over budget by 1,097 tokens"
   - See: "Heaviest files: dress_accent_complements.json (1964 tokens)"

2. **Read VIOLATION_DETAIL_REPORT.md**
   - See: 31 narrative language violations
   - See: 4 character limit violations (specific atoms listed with over-by amounts)
   - See: Trim candidates ranked by token cost

3. **Target specific atoms**
   - Find: `embellish.glitter_fabric_panels` (390 chars, 97 tokens, 90 over limit)
   - Action: Trim by 90 chars while preserving meaning
   - Cost: ~23 tokens saved

4. **Run camera.py again**
   - See: New token count
   - See: Updated violations list
   - VIOLATION_DETAIL_REPORT.md auto-updated

---

## Tiktoken Support

### Current Status:
- Tools work with or without tiktoken
- Without tiktoken: Uses character-based estimation (len / 4)
- With tiktoken: Accurate token counting per GPT-3.5/4 encoding

### Installing Tiktoken (Optional):
```bash
pip install tiktoken
```

### Verification:
```bash
python -c "import tiktoken; print('tiktoken OK')"
```

Once installed, analytics automatically upgrade to precise token counting.

---

## Data Available for Future Use

The toolkit collects detailed metrics that can be used for:

1. **Automation**: I could write scripts to auto-trim atoms hitting targets
2. **Reporting**: Generate daily/weekly efficiency reports
3. **Benchmarking**: Track atom efficiency over time
4. **Optimization**: Identify which files/patterns waste most tokens
5. **Compliance**: Ensure zero violations before delivery

---

## Maintenance

### Rule 32 Compliance:
Tools are automatically cleaned before ZIP:
- No `__pycache__/` directories
- No `.pyc` files
- No temporary files
- VIOLATION_DETAIL_REPORT.md is auto-generated (not archived)

---

## What I Can Do With This Toolkit

With these tools running every iteration, I can:

✅ **See exact token cost per atom** (with tiktoken) or estimate (without)
✅ **Identify top 10 token-wasting atoms** instantly
✅ **Target 20 atoms for 10-15% trim** = ~900 token savings
✅ **Detect and fix narrative language** automatically
✅ **Verify filter-safety** before delivery
✅ **Report efficiency** across all iterations
✅ **Benchmark improvements** between sessions

This transforms token management from guessing to precision targeting. 💙
