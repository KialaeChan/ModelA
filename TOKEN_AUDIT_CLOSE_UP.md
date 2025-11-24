# TOKEN AUDIT - CLOSE-UP PROMPTS (2025-11-24)

## CURRENT STATUS

**5-Run Average:** 4,393 tokens
**Target:** 3,000 tokens  
**Over budget:** +1,393 tokens (46.4% over)

**Individual runs:**
- Run 1: 4,587 tokens
- Run 2: 4,352 tokens
- Run 3: 4,244 tokens
- Run 4: 4,464 tokens
- Run 5: 4,317 tokens

**Range:** 343 tokens variation (4,244 to 4,587)

---

## TOP 15 HEAVIEST ATOMS (CLOSE-UP LOADS)

| Atom | Tokens | File | Status |
|------|--------|------|--------|
| camera.angle_offcenter_amateur_closeup | 196 | camera_angles_close.json | Over 300 chars |
| expression.gaze_struggling_to_track | 186 | expression_emotion.json | Over 300 chars, narrative |
| illness.dissociation_profound | 175 | illness_manifestations.json | Over 300 chars |
| illness.chronic_insomnia_severe | 167 | illness_manifestations.json | Over 300 chars |
| hair.primary.butterfly_crystal_swarm | 151 | hair_accessories.json | Over 300 chars |
| hair.primary.dimensional_rose_cluster | 144 | hair_accessories.json | Over 300 chars |
| hair.primary.theatrical_bow_palace | 143 | hair_accessories.json | Over 300 chars, narrative |
| hair.primary.cascading_ribbon_sculpture | 142 | hair_accessories.json | Over 300 chars |
| hair.primary.floral_crown_architecture | 138 | hair_accessories.json | Over 300 chars |
| style.sparkle_mandate | 136 | style_enforcement.json | Over 300 chars, P0 protected |
| hair.primary.crystal_cascade_statement | 135 | hair_accessories.json | Over 300 chars |
| hair.primary.pearl_circlet_princess_excess | 130 | hair_accessories.json | Over 300 chars, narrative |
| hair.primary.gingham_bow_cascade_sculpture | 126 | hair_accessories.json | Over 300 chars |
| hair.primary.lace_crown_vintage_excess | 125 | hair_accessories.json | Over 300 chars |
| expression.say_cheese_delirious | 114 | expression_emotion.json | Over 300 chars |

**Top 15 total:** ~2,208 tokens (50% of prompt)

---

## HEAVIEST FILES (TOTAL LIBRARY)

| File | Tokens | Atoms | Avg/Atom |
|------|--------|-------|----------|
| couture_construction.json | 3,018 | 57 | 52.9 |
| shiny_embellishments.json | 2,415 | 50 | 48.3 |
| makeup_application.json | 2,132 | 44 | 48.5 |
| hair_accessories.json | 1,990 | 35 | 56.9 |
| expression_emotion.json | 1,440 | 35 | 41.1 |

---

## TRIM OPPORTUNITIES & ESTIMATED SAVINGS

### HIGH IMPACT (200-400 token savings)

**1. Hair Primary Embellishments (9 atoms)**
- Current: All 500-600 chars, 125-151 tokens each
- Issue: Excessive detail for close-ups, narrative language
- Action: Trim to 300 chars max, remove narrative
- Estimated savings: ~300 tokens

**2. Camera & Expression Atoms (3 atoms)**
- camera.angle_offcenter_amateur_closeup: 196 tokens
- expression.gaze_struggling_to_track: 186 tokens  
- expression.say_cheese_delirious: 114 tokens
- Issue: Verbose descriptions, narrative language
- Action: Condense to observable facts only
- Estimated savings: ~200 tokens

### MEDIUM IMPACT (100-200 token savings)

**3. Illness Manifestations (2 atoms)**
- illness.dissociation_profound: 175 tokens
- illness.chronic_insomnia_severe: 167 tokens
- Issue: Over 300 chars, repetitive descriptions
- Action: Consolidate overlapping content
- Estimated savings: ~100 tokens

**4. Neckline Construction (10+ atoms)**
- 10 necklines at 301-339 chars (76-84 tokens each)
- Issue: Barely over 300 char limit
- Action: Trim 30-40 chars from each
- Estimated savings: ~80 tokens

### LOW IMPACT (50-100 token savings)

**5. Style.sparkle_mandate**
- Current: 136 tokens
- Issue: Rule 42 - PROTECTED, but verbose
- Action: Keep message, trim redundancy
- Estimated savings: ~30 tokens (careful)

**6. Bodice Close-up Variants**
- 5 bodice atoms at 75-80 tokens each
- Action: Consolidate or trim descriptions
- Estimated savings: ~50 tokens

---

## PROJECTED TOKEN TARGETS

| Strategy | Target | Savings Needed | Actions |
|----------|--------|----------------|---------|
| **Aggressive** | 3,000 | -1,393 | All HIGH + MEDIUM + LOW |
| **Moderate** | 3,500 | -893 | All HIGH + MEDIUM |
| **Light** | 3,800 | -593 | HIGH impact only |

---

## VIOLATIONS SUMMARY

- **Character limit:** 36 atoms over 300 chars
- **Narrative language:** 8 atoms
- **Filter-risk:** 3 atoms

**Priority:** Fix violations while trimming for dual benefit.

---

## RECOMMENDATIONS

1. **Start with Hair Primaries:** Biggest single-file impact (9 atoms, ~300 token savings)
2. **Fix Camera/Expression:** Remove narrative, trim to facts (~200 tokens)
3. **Consolidate Illness:** Merge overlapping symptoms (~100 tokens)
4. **Trim Necklines:** Just need 30-40 chars off each (~80 tokens)

**Total potential savings:** ~680 tokens  
**Projected result:** ~3,713 tokens (23.8% over, acceptable range)

