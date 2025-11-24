# Aesthetic Target - ModelA

**This document is the ground truth for ModelA's intended visual style. All style atoms and test results should align with this target.**

Last Updated: Nov 22, 2025 (CORRECTED - Phase 2)

---

## PRIMARY AESTHETIC INTENT

**Style:** Realistic clean digital rendering with vibrant saturated colors standing out against institutional grey. Sharp overhead institutional lighting creating dimensional form through strong shadows. Cute AMAB in elaborate couture creating visual dissonance through contrast.
**Reference Artists:** Clean digital rendering (artgerm/wlop realistic style), institutional lighting effect
**Core Narrative:** Beautiful, perfectly presented person in utilitarian beautification space, but internally disconnected and unfocused
**Genre/Category:** Realistic rendering with visual/emotional dissonance (striking ↔ absent)
**NOT:** Glowing/ethereal/magical, soft flattering light, desaturated/muted, grim/resigned tone (despite harsh space)

---

## VISUAL QUALITIES REQUIRED

### Linework
- ❌ NO visible linework (clean blended edges)
- ❌ NO cartoon simplification
- ✅ Clean precise edges through realistic rendering
- ✅ Professional digital technique

### Shading & Form
- ✅ Realistic dimensional form through accurate lighting
- ✅ **Sharp defined shadows from overhead institutional light**
- ✅ Strong value separation (light areas bright, shadow areas deep)
- ✅ Overhead angle casting shadows on face/body
- ✅ Material properties affect how light interacts (fabric sheen, skin texture)

### Color & Atmosphere
- ✅ **Vibrant, saturated, luminous color palette on dress**
- ✅ Cool institutional grey walls/floor (contrast background)
- ✅ Dress stands out visually against grey environment
- ✅ *Apparent* glow from dissonance/contrast, not magical luminescence
- ✅ Clean, technical, observational rendering style
- ✅ Utilitarian-yet-luxurious space aesthetic

### Character Appearance
- ✅ Cute AMAB, young-looking adult (20-24, mature despite appearance)
- ✅ Perfect styling evident (elaborate dress, heavy makeup, precise hair)
- ✅ **Unfocused gaze and internal disconnection despite external perfection**
- ✅ Eyes not engaged, looking past/through
- ✅ Body complies but consciousness absent
- ✅ Visible exhaustion in expression despite careful preparation

### Environment & Contrast
- ✅ Institutional grey setting (utilitarian yet technically luxurious)
- ✅ Overhead institutional LED lighting (harsh, defining, realistic)
- ✅ Elaborate precious dress stands out against clinical setting
- ✅ Cool institutional color temperature
- ✅ Dissonance: beautiful presentation in non-celebratory space

### Technical Execution
- [x] Realistic clean digital rendering (not illustration, not painterly)
- [x] Professional quality execution
- [x] Clear sharp image (not soft-focus)
- [x] Dimensional form defined through overhead lighting and shadows
- [x] Material properties accurate (fabric, skin, hair behavior)

---

## VISUAL QUALITIES TO AVOID

### ❌ Absolutely Avoid
- Soft flattering studio lighting (should be harsh overhead institutional)
- Glowing/ethereal/magical appearance (should be realistic material reflection)
- Engaged/present expression (should be unfocused/disconnected)
- Desaturated muted colors (dress should pop with vibrant saturation)
- Soft shadow transitions (should be sharp defined shadows from overhead)
- Resigned/grim emotional tone (should be disconnected/absent - different mood)
- Photorealistic texture to excess (should feel clean and technical)

### ⚠️ Watch For (Common Generator Defaults)
- Drifting toward soft flattering light instead of harsh institutional
- Making character appear engaged/happy despite prompt
- Colors desaturating instead of remaining vibrant
- Shadows becoming soft gradients instead of sharp definition
- Overall aesthetic becoming too dark/grim (should be striking/beautiful but vacant)
- Adding emotion to expression (should be blank/unfocused)
- Making space too comfortable/welcoming instead of utilitarian

---

## WHAT SHOULD BE VISIBLE IN GENERATED IMAGE

**When you generate a test image, look for:**

1. **Linework:**
   - Is there NO visible linework? (smooth blending throughout)
   - Are edges defined by shading alone, not lines?
   - Does it look professional and polished (not sketchy)?

2. **Color & Light:**
   - Is the palette desaturated/muted (not bright)?
   - Does it feel cool and institutional (not warm)?
   - Is skin tone sallow/drained (not glowing)?
   - Is lighting flat and uninspiring (not dramatic)?

3. **Character:**
   - Does face read as adult (defined features)?
   - Is expression resigned/unfocused (not engaged)?
   - Is exhaustion visible (dark circles, heavy lids)?
   - Are eyes looking away or down (not at camera with spark)?

4. **Overall Feeling:**
   - "This looks like professional smooth rendering but emotionally drained"
   - "The colors feel institutional and cold"
   - "The character looks resigned and withdrawn, not hopeful"
   - "The light is flat and uninspiring, not dramatic or harsh"
   - "This feels grim and uncomfortable, not beautiful"

---

## PREVIOUS FAILURES (WHAT NOT TO DO)

### Heavy Bold Linework Iteration (REJECTED - User Feedback)
- **Problem:** Generated with bold linework but user said "still not grim enough"
- **Language:** "Heavy bold linework," "aggressive line weight," "expressive line weight"
- **Why it failed:** Graphic presence was opposite of "grim" - made it look energetic/aggressive
- **Lesson:** Grimness comes from emotional tone (resignation, desaturation), not graphic style

### Pure Animation Iteration (REJECTED)
- **Problem:** Generated full anime style, lost professional rendering quality
- **Why it failed:** Pure animation language abandons dimensional quality
- **Lesson:** Use "smooth blended" not "animated"

### Photorealistic CG Iteration (REJECTED)
- **Problem:** Generated photorealistic 3D, triggered uncanny valley
- **Language:** "High-end CG rendering," "3D dimensional form"
- **Why it failed:** "CG" triggers photorealism default
- **Lesson:** Must use "illustrated" or "illustration" language

---

## WHAT WORKS (PROVEN IN TESTS)

## WHAT WORKS (PROVEN IN TESTS)

### Smooth Blended + Institutional Desaturation ✅ (NEW)
- **Language:** "Smooth blended," "institutional color grading," "desaturated," "resigned quality"
- **Result:** TBD - awaiting test image (3655 tokens)
- **Basis:** User provided 3 reference images showing this exact aesthetic
- **Status:** CURRENT TARGET

### Inoue-Level Professional Rendering ⭐ (VERIFIED)
- **Language:** "Professional Inoue-level," "smooth transitions," "no linework emphasis"
- **Result:** Generators respond well to specific artist references
- **Status:** KEY TECHNIQUE REFERENCE

### Institutional Lighting & Color Grading ⭐ (VERIFIED)
- **Language:** "Institutional light color grading," "cool greenish," "flat desaturated," "draining warmth"
- **Result:** Creates resigned, grim emotional tone through technical qualities
- **Status:** CORE EMOTIONAL LANGUAGE

### Resigned/Emotionally Flat Language ⭐ (NEW)
- **Language:** "Resigned," "cold emotional quality," "emotionally flat," "withdrawn," "unfocused gaze"
- **Result:** Shifts mood from photorealism or animation toward specific emotional state
- **Status:** CRITICAL FOR GRIMNESS

---

## DECISION FRAMEWORK FOR NEXT ITERATION

**If test image shows:**

1. **Linework visible** → Remove "smooth blended," increase "no linework emphasis"
2. **Colors too warm/saturated** → Strengthen "cool greenish," "desaturated," "muted"
3. **Lighting too harsh or dramatic** → Change "institutional flat" language, reduce any "shadow" emphasis
4. **Character looks happy/engaged** → Add "resigned," "unfocused," "withdrawn," "emotionally flat"
5. **Overall feels wrong** → Check if aesthetic drifted from AESTHETIC_TARGET.md
6. **Everything working** → Lock this direction, proceed to token optimization

---

## TESTING PROTOCOL

**Every time you change style atoms:**

1. Run `python camera.py` and check prompt language
2. Generate ONE test image in same session
3. Document in STYLE_TEST_LOG.md:
   - What changed
   - What you expected
   - What actually happened
   - What to try next
4. Update this document if direction needs adjustment

**Never iterate multiple times without testing image generation.**

---

## Current Status

**Phase:** Aesthetic direction refinement complete, awaiting test image

**Last Change:** Nov 21, 2025 - Complete shift to smooth blended institutional desaturation (3655 tokens)

**Aesthetic:** Smooth professional rendering (Inoue-level) with institutional color grading, desaturated palette, resigned/cold emotional tone

**Assessment:** Atoms rewritten based on 3 user reference images. Language now targets:
- Smooth blending (NO linework)
- Institutional flat lighting (cool greenish, desaturated)
- Resigned emotional tone (emotionally flat, withdrawn, cold)
- Professional Inoue rendering technique

**Next Step:** Generate test image to verify aesthetic direction. If successful, lock this direction and optimize tokens.

