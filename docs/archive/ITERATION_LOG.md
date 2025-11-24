# ModelA - Iteration Log

Ongoing documentation of generation attempts, failures, and solutions discovered.

---

## Generation 1 - Lighting & Harshness Overhaul (Nov 21, 2025)

**Issue Identified:** 
- Lighting was too soft and flattering despite "harsh institutional" language
- Environment (walls, floor) appeared warm beige instead of cold grey
- Dress blended harmoniously with environment instead of clashing jarringly
- Visual dissonance (central concept) was not apparent

**Root Cause Analysis:**
- Lighting language was present but weak ("cool neutral" 5000-6000K was still pleasant)
- Style atoms emphasized "soft diffused" and "polished" surfaces
- Image generator defaults toward flattering soft lighting regardless of prompt language
- Scene description lacked institutional coldness
- No dedicated dissonance atom file—tension scattered across character/scene atoms

**Solutions Implemented:**

1. **scene_lighting.json rewrite:**
   - Changed color temperature from 5000-6000K (cool-neutral) to 7000-8000K (harsh fluorescent)
   - Added "harsh overhead" language replacing "soft diffused"
   - Described "sharp shadows beneath features" instead of "gentle shadows"
   - Changed walls to "stone-grey, NOT warm beige"
   - Added new `dissonance.dress_vs_environment` atom explicitly stating clash

2. **style_enforcement.json overhaul:**
   - Renamed atoms to "painted_surface_stark" with "harsh contrasts"
   - Changed fabric rendering to "glossy sheen and shine" catching harsh light
   - Updated lighting model to "harsh institutional with strong shadows"
   - Removed "soft ambient occlusion" language
   - Emphasized "stark shadows" not "gentle"

3. **character_core.json enhancement:**
   - Added new atom `character.adult_face_geometry` with explicit "NOT childlike"
   - Strengthened `character.age_explicit` to "Legally adult, completely mature adult"
   - All age atoms set to P0 MANDATE priority

4. **camera.py preamble:**
   - Added "LEGALLY ADULT, COMPLETELY MATURE" with repeated negations
   - "Adult face with mature bone structure. Looks distinctly adult."
   - Final line now emphasizes "institutional harsh lighting" and "Clinical institutional aesthetic"

**Expected Outcome:**
- Next generation should show harsh cold fluorescent lighting
- Dress should appear shiny/glossy catching harsh light against grey walls
- Visual dissonance between precious dress and clinical space should be apparent
- Age should be more clearly adult

**Next Check:**
- Verify if 7000-8000K fluorescent is still too subtle
- May need to remove "cool-neutral" language entirely, replace with "fluorescent white" or "hospital harsh blue-white"
- Consider if glossy language is strong enough for image generator

---

## Enhancements Added to Mandate (Nov 21, 2025)

**New Files Created:**

1. **character_age_safety.json** - Dedicated age safety atoms:
   - `character.age_safety_explicit_adult` - "Legally adult, completely mature"
   - `character.adult_face_maturity` - "Mature skull structure, NOT childlike"
   - `character.adult_proportions_body` - "Long slender limbs, adult development"
   - `character.adult_eye_proportion` - "Eyes small relative to head, adult anime style"

2. **scene_dissonance.json** - Central tension atoms:
   - `dissonance.dress_shine_vs_grey` - Glossy dress clashes with grey institutional
   - `dissonance.precious_vs_clinical` - Most special dress in utilitarian setting
   - `dissonance.beauty_vs_breakdown` - Perfect appearance hides exhaustion
   - `dissonance.celebration_vs_extraction` - Celebration dress in medical facility
   - `dissonance.compliance_vs_collapse` - Trained compliance failing mid-pose

**Schema Updates:**

1. **CHARACTER_AGE_SAFETY (early)** - Layer 1.5 after STYLE_FOUNDATION
   - Slot: `character.age_safety_early` - 2 atoms from character_age_safety.json
   - P0 MANDATE - ensures adult interpretation early

2. **SCENE_DISSONANCE** - Layer 10.5 before final style
   - Slot: `dissonance.core` - 2-3 atoms from scene_dissonance.json
   - P1 CORE - saturates prompt with central paradox

3. **CHARACTER_AGE_SAFETY (late)** - Layer 11.5 before STYLE_FINAL
   - Slot: `character.age_safety_late` - 2 atoms from character_age_safety.json
   - P0 MANDATE - final reinforcement lock

**Console Output Enhancement:**

Added MANDATE CHECKPOINT REPORT to camera.py that displays:
- Age Safety (Early): X atoms selected with names
- Age Safety (Late): X atoms selected with names
- Dissonance: X atoms selected with names
- Style Foundation: X atoms selected with names
- Pass/Fail assessment: Green checkmark if all critical atoms present

Allows verification of mandate adherence BEFORE image generation.

---

## Known Issues to Monitor

**Lighting Model Resistance:**
- Image generators may default to soft flattering light regardless of "harsh" language
- Solution: May need to use more extreme language ("brutal," "clinical," "unflattering," "unforgiving")
- Alternative: Try removing "soft," "gentle," "polished" entirely from style atoms

**Age Safety Vulnerability:**
- Anime aesthetic naturally biases toward youthful appearance
- Solution: Dedicating early and late checkpoint slots helps, but may need even stronger language
- Alternative: Consider adding "adult aged 20-24, NOT under 18" to preamble multiple times

**Dissonance Subtlety:**
- Image generator may not pick up on paradox between elements
- Solution: Explicit dissonance atoms help
- Alternative: Make dress MORE special (increase embellishment language?) or environment MORE cold (make walls darker?)

---

## Success Metrics (Phase 3)

Testing next generation image should show:

1. **Lighting:**
   - [ ] Harsh overhead fluorescent light visible
   - [ ] Strong defined shadows under eyes, cheekbones
   - [ ] Cold blue-white light tone, NOT golden
   - [ ] Unflattering harsh lighting

2. **Environment:**
   - [ ] Walls distinctly grey, NOT beige
   - [ ] Institutional cold feel
   - [ ] Visible facility equipment in background

3. **Dress:**
   - [ ] Shiny glossy finish catching harsh light
   - [ ] Warm pink clashes with cold grey walls
   - [ ] Appears wrong/out of place in clinical setting

4. **Character:**
   - [ ] Distinctly adult features
   - [ ] Exhaustion visible despite makeup
   - [ ] Paradox between perfect dress and broken appearance

5. **Overall:**
   - [ ] Visual dissonance immediately apparent
   - [ ] "This is wrong" feeling
   - [ ] Horror tone vs. beauty tone contrast working

---

## Future Iteration Planning

**If lighting still too soft:**
- Remove "soft painted surfaces" from style, replace with "rendered surfaces"
- Try "brutally lit," "unforgiving light," "harsh clinical lighting" instead of "harsh institutional"
- Consider making preamble mention "harsh lighting" explicitly

**If age still ambiguous:**
- Add to preamble: "ADULT. Not child. Not teen. Not minor. Mature adult."
- Consider rephrasing character atoms to use "mature" vs "young"
- May need to remove anime styling that triggers cute/young perception

**If dissonance still weak:**
- Increase embellishment language (make dress MORE precious)
- Increase exhaustion language (make character MORE broken)
- Make environment MORE institutional/cold
- Add explicit contradiction statements

---

## Archive

*Previous generations and full logs available on request.*
