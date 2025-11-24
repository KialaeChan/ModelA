# CLOSE-UP TOKEN AUDIT REPORT
Date: 2025-11-23
Camera Distance: CLOSE (face-only framing)

## CURRENT STATUS
- **Actual Tokens**: 5,027
- **Target**: 3,000
- **Over Budget**: +2,027 tokens (67.6% over)
- **Required Reduction**: 40%

---

## SECTION BREAKDOWN (Close-Up Mode)

| Tokens | Section | % of Total | Priority |
|--------|---------|------------|----------|
| 1,186 | CHARACTER CORE (Makeup) | 27.5% | CRITICAL |
| 690 | SCENE ENVIRONMENT | 16.0% | HIGH |
| 495 | EXPRESSION EMOTION | 11.5% | MEDIUM |
| 448 | STYLE FOUNDATION | 10.4% | LOW (Rule 42) |
| 379 | ILLNESS STATE | 8.8% | MEDIUM |
| 273 | STYLE CHECKPOINT | 6.3% | LOW (Rule 42) |
| 231 | COUTURE DRESS | 5.4% | HIGH |
| 121 | STYLE FINAL | 2.8% | LOW (Rule 42) |
| 109 | CHARACTER AGE SAFETY | 2.5% | NONE (P0) |
| 95 | CHARACTER AGE SAFETY LATE | 2.2% | NONE (P0) |
| 77 | SCENE DISSONANCE | 1.8% | LOW |
| 69 | FRAMING ENFORCEMENT | 1.6% | LOW |
| 60 | POSE BODY | 1.4% | MEDIUM |
| 29 | HAIR STYLING | 0.7% | LOW |
| 22 | HAIR ACCESSORIES | 0.5% | LOW |
| 21 | ENSEMBLE VISION | 0.5% | NONE (P0) |

**TOTAL**: ~4,305 tokens (section content only, excludes preamble)

---

## TRIMMING STRATEGY (Target: 2,000+ token reduction)

### PHASE 1: High-Impact Cuts (Close-Up Specific)
**Rationale**: These sections describe elements barely/not visible in close-up framing

1. **SCENE ENVIRONMENT: 690 → 200 tokens (-490)**
   - Close-ups show minimal background
   - Keep: basic grey laboratory, lighting setup
   - Cut: detailed equipment descriptions, floor perspective, depth

2. **COUTURE DRESS: 231 → 100 tokens (-131)**
   - Only neckline edge visible in close-up
   - Keep: neckline construction, primary color visible at edge
   - Cut: skirt, petticoat, full dress construction, embellishments

3. **CHARACTER CORE (Makeup): 1,186 → 800 tokens (-386)**
   - Massive redundancy in glitter descriptions
   - Keep: foundation, eye makeup, lips, blush, key highlights
   - Cut: duplicate glitter atoms (currently 2-3 similar atoms load)
   - Consolidate: highlighter placement described multiple times

**Subtotal Savings: 1,007 tokens**

---

### PHASE 2: Medium-Impact Cuts (Consolidation)

4. **EXPRESSION EMOTION: 495 → 400 tokens (-95)**
   - Gaze atom loads in BOTH camera_gaze AND core_expression slots
   - Fix: Consolidate duplicate Pavlovian gaze language
   - Keep: smile mechanics, facial muscle details

5. **ILLNESS STATE: 379 → 300 tokens (-79)**
   - Repetitive language about bloodshot eyes, dark circles
   - Keep: severe insomnia, profound dissociation
   - Cut: Redundant repetition of same symptoms

**Subtotal Savings: 174 tokens**

---

### PHASE 3: Low-Impact Optimization (If Needed)

6. **STYLE FOUNDATION: 448 → 350 tokens (-98)**
   - Some repetition in edge definition language
   - Protected by Rule 42 but can optimize without losing aesthetic
   - Consolidate: multiple mentions of "bright white-blue light"

7. **STYLE CHECKPOINT: 273 → 200 tokens (-73)**
   - Trim verbose material descriptions
   - Keep: core rendering requirements

8. **Reduce P2 DETAIL max_atoms**: (-100 estimated)
   - Lower max_atoms in some P2 slots from 3 → 2

**Subtotal Savings: 271 tokens**

---

## TOTAL PROJECTED SAVINGS: 1,452 tokens
**Result**: 5,027 - 1,452 = **~3,575 tokens** (19% over target)

---

## PHASE 4: Final Calibration (If needed to reach 3,000)
Additional -575 tokens through:
- Further P2 max_atoms reduction
- Trim individual atom verbosity (10-15% across files)
- Consolidate similar style checkpoint language

---

## CRITICAL CONSTRAINTS (Rule 42)
**NEVER TRIM**:
- Style enforcement atoms (sacred per Rule 42)
- P0 MANDATE atoms
- Core aesthetic language ("manga painter rendering realistic anatomy")
- Specular highlight enforcement (just added for sharpness)
- Age safety checkpoints

---

## RECOMMENDED EXECUTION ORDER
1. ✅ Cut SCENE ENVIRONMENT for close-ups (biggest single win)
2. ✅ Cut COUTURE DRESS details for close-ups  
3. ✅ Consolidate duplicate MAKEUP atoms
4. ✅ Fix duplicate EXPRESSION gaze loading
5. ✅ Consolidate ILLNESS STATE repetition
6. ⚠️ ONLY IF NEEDED: Optimize style language carefully
7. ⚠️ ONLY IF NEEDED: Further P2 reduction

---

## NOTES
- Makeup section is 27.5% of entire prompt - largest single section
- Scene environment is 16% but barely visible in close-ups
- Two P0 atoms (gaze) loading duplicate content in different slots
- Style atoms protected by Rule 42 - last resort only
