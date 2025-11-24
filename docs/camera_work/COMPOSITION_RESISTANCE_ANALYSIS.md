# Composition Framing Issues - DALL-E Resistance Analysis
**Date:** December 1, 2025
**Problem:** DALL-E ignores "bad" framing instructions

---

## ISSUE #1: OFF-CENTER PLACEMENT (Not Working)

**What we ask for:**
- Preamble: "Subject EXTREMELY FAR to left or right edge. Occupies LEFT 40% or RIGHT 40% only. MASSIVE EMPTY VOID opposite (60% empty)."
- Compositional flaw atom: "Subject positioned arbitrarily. Zero composition skill. Off-center placement."

**What DALL-E gives us:**
- Centered composition
- Subject nicely balanced in frame
- Professional-looking placement

**Why DALL-E resists:**
- Trained on "good" photos with rule-of-thirds
- Extreme off-center (40%/60%) reads as "mistake" to correct
- DALL-E's safety: prevent "broken" compositions

---

## ISSUE #2: CAMERA DISTANCE (Not Working)

**What we ask for:**
- "3 feet distance. Chest up - neckline through face."
- "Bottom of frame cuts at waist level. Legs NOT visible."

**What DALL-E gives us:**
- 6-7 feet full-body shot
- Entire dress visible
- Professional portrait distance

**Why DALL-E resists:**
- Close crops feel "claustrophobic"
- Full-body shots show "the whole outfit"
- Fashion/dress photography bias

---

## DALL-E RESISTANCE PATTERNS

### Strong Biases (Hard to Fight):
1. **Centered composition** - Rule of thirds, balanced framing
2. **Full-body for fashion** - Show the whole outfit
3. **Professional headroom** - Correct spacing above head
4. **Clean backgrounds** - No awkward intersections
5. **Level horizons** - Straight floor lines

### Weak Biases (Easier to Fight):
1. Lighting quality (harsh vs soft)
2. Color saturation
3. Expression/emotion
4. Material rendering
5. Detail level

---

## CURRENT LANGUAGE PROBLEMS

### TOO SUBTLE:
❌ "Off-center placement" - DALL-E ignores
❌ "3 feet distance" - DALL-E ignores
❌ "Careless framing" - DALL-E corrects
❌ "Hasty amateur recording" - DALL-E makes it professional anyway

### MIGHT WORK:
✅ "CLOSE-UP PORTRAIT" - composition type keyword
✅ "Bottom of frame cuts at waist" - specific crop instruction
✅ "NOT full body shot" - negative blocking
✅ "LEFT 40% ONLY, RIGHT 60% EMPTY VOID" - extreme specific numbers

---

## ESCALATION STRATEGIES

### LEVEL 1: Aggressive Language (Testing Now)
- Repeat instructions 3-4 times
- Use specific measurements
- Add negative blocking
- Explicit crop lines

**Example (close-up):**
"CLOSE-UP PORTRAIT. 3 feet camera distance. TIGHT FRAMING: Bottom of frame cuts at waist level. Legs NOT visible, feet NOT in frame, skirt hem NOT visible. Subject fills 85-90% of frame height. NOT full body shot. NOT distant framing. Waist-up cropping only."

### LEVEL 2: Preamble Placement
- Move distance to very start of prompt
- Before style/character/anything
- Force DALL-E to prioritize it

**Example:**
"CLOSE-UP PORTRAIT FRAMING. Camera 3 feet from subject. Frame cuts at waist - legs not visible. [rest of prompt]"

### LEVEL 3: Negative Emphasis
- Focus on what NOT to show
- "NO full body", "NO feet visible", "NO floor in frame"

### LEVEL 4: Compromise
- Accept DALL-E won't do extreme off-center
- Focus on distance control only
- Pick battles we can win

---

## COMPOSITION ATOMS - EFFECTIVENESS RATING

**Likely Ignored by DALL-E (Low Impact):**
- composition.hasty_centering - "awkwardly off-center"
- composition.awkward_cropping - "excessive empty space"
- composition.subject_drastically_off_center - "arbitrarily positioned"

**Might Work (Medium Impact):**
- composition.tilted_horizon - "3-7deg tilt" (specific angle)
- composition.subject_partially_cropped - "arm cut off by frame edge"
- composition.poor_headroom - "excessive empty space above head"

**Probably Works (High Impact):**
- composition.snapshot_mentality - "single quick exposure"
- composition.lazy_standing_position - "shot from wherever"
- These don't fight visual layout, just describe quality

---

## TESTING MATRIX

| Instruction Type | Current Language | DALL-E Compliance | Fix Needed |
|-----------------|------------------|-------------------|------------|
| Close distance (3-5ft) | "3 feet distance" | ❌ FAILS | ✅ Test aggressive |
| Medium distance (5-7ft) | "5-6 feet distance" | ❓ UNKNOWN | Test needed |
| Full-body distance (6-8ft) | "6-8 feet distance" | ✅ PROBABLY WORKS | Low priority |
| Off-center 40%/60% | "LEFT 40% only" | ❌ FAILS | May be impossible |
| Tilted horizon | "3-7deg tilt" | ❓ UNKNOWN | Test needed |
| Awkward cropping | "arm cut off" | ❓ UNKNOWN | Test needed |

---

## RECOMMENDATIONS

### PRIORITY 1: Distance Control
**Focus:** Make close/medium cameras work consistently
**Method:** Aggressive crop language with negative blocking
**Test:** chest_up_close with new language (pending)

### PRIORITY 2: Partial Cropping
**Focus:** "Arm cut off by frame edge" type cropping
**Method:** Specific body part exclusions
**Test:** After distance tests complete

### PRIORITY 3: Accept Off-Center Limitations
**Reality:** DALL-E may never do 40%/60% extreme off-center
**Options:** 
- Compromise with 30%/70% (less extreme)
- Focus on other amateur markers (tilt, cropping)
- Accept this limitation

---

## NEXT EXPERIMENTS

1. **Test aggressive close-up language** (in progress)
2. **If success:** Apply to all close cameras
3. **If failure:** Try preamble placement
4. **Test medium distance** with same pattern
5. **Test tilted horizon** - does "3-7deg" work?
6. **Test arm cropping** - does specific body part work?

---

## QUESTIONS FOR EMILY

1. Is 40%/60% off-center **critical** or can we compromise?
2. Is distance control more important than off-center?
3. Should we test tilted horizon next?
4. How many test iterations can we do?

---
