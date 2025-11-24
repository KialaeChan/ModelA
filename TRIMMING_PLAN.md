# CLOSE-UP TOKEN TRIMMING PLAN
**Status**: 5,027 tokens → Target: 3,000 tokens
**Required Cut**: 2,027 tokens (40% reduction)

---

## IMMEDIATE ACTIONS (High Confidence Cuts)

### 1. SCENE ENVIRONMENT (-490 tokens) ✓ SAFE TO CUT
**Current**: 690 tokens describing laboratory equipment, floor details, spatial depth
**Issue**: Close-ups show MINIMAL background - just grey blur behind face
**Action**: 
- Keep: "Cold sterile facility with grey space. Laboratory grey walls visible at depth"
- Keep: Lighting setup (critical for speculars)
- Cut: Equipment details, floor perspective, room depth descriptions
**New Target**: 200 tokens

### 2. COUTURE DRESS (-131 tokens) ✓ SAFE TO CUT
**Current**: 231 tokens describing full dress construction
**Issue**: Close-ups only show NECKLINE EDGE - no bodice, skirt, petticoat visible
**Action**:
- Keep: Neckline style, visible color at edge
- Cut: Skirt construction, petticoat system, embellishments, full dress details
**New Target**: 100 tokens

### 3. CHARACTER CORE MAKEUP (-386 tokens) ⚠️ REQUIRES CARE
**Current**: 1,186 tokens - LARGEST section (27.5% of prompt!)
**Issue**: Multiple glitter atoms describe same particles differently, highlighter placement repeated
**Action**:
- Consolidate: 2-3 glitter atoms into 1 comprehensive description
- Remove: Duplicate highlighter placement descriptions
- Keep: Foundation, eye makeup, lips, blush core
**New Target**: 800 tokens

---

## SUBTOTAL PHASE 1: -1,007 tokens
**Result after Phase 1**: 4,020 tokens (still 34% over)

---

## SECONDARY ACTIONS (Consolidation)

### 4. EXPRESSION EMOTION (-95 tokens) ✓ BUG FIX
**Current**: 495 tokens
**Issue**: Pavlovian gaze atom loads in BOTH camera_gaze slot AND core_expression slot
**Action**: Fix slot schema so gaze only loads once
**New Target**: 400 tokens

### 5. ILLNESS STATE (-79 tokens) ✓ SAFE TO CONSOLIDATE
**Current**: 379 tokens
**Issue**: "Bloodshot eyes," "dark circles showing through" repeated multiple times
**Action**: Consolidate into single comprehensive illness description
**New Target**: 300 tokens

---

## SUBTOTAL PHASE 2: -174 tokens
**Result after Phase 2**: 3,846 tokens (28% over)

---

## FINAL CALIBRATION (If approved)

### 6. P2 DETAIL Reduction (-100 tokens estimated)
**Action**: Reduce max_atoms in some P2 slots from 3 → 2
- Pose timing
- Hair styling details
- Minor embellishments

### 7. Individual Atom Trimming (-300 tokens)
**Action**: Trim 10-15% verbosity from:
- Makeup application atoms (remove filler words)
- Expression atoms (consolidate similar language)
- Scene lighting atoms (remove repetition)

---

## PROJECTED FINAL: 3,446 tokens (15% over target)
**Acceptable?** Close to 3,000 with quality preserved

---

## PROTECTED ELEMENTS (Rule 42 - UNTOUCHABLE)
- ❌ Style enforcement atoms (artstyle is sacred)
- ❌ P0 MANDATE atoms
- ❌ "Manga painter rendering realistic anatomy" language
- ❌ Specular highlight enforcement (just added for sharpness fix)
- ❌ Age safety checkpoints

---

## EXECUTION ORDER
1. Cut scene environment for close-ups
2. Cut dress details for close-ups
3. Consolidate makeup glitter atoms
4. Fix duplicate gaze loading
5. Consolidate illness repetition
6. **CHECKPOINT** - measure tokens
7. If still over: Reduce P2 max_atoms
8. If still over: Trim individual atom verbosity

---

## APPROVAL NEEDED
**Proceed with Phases 1 & 2?** (Projected: 3,846 tokens)
- Phase 1: Scene/Dress cuts (safe for close-ups)
- Phase 2: Consolidation (bug fixes + redundancy removal)

**Target 3,000 exactly?** Will require Phase 3 (additional trimming)
