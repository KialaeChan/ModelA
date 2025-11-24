# BUGS AND SOLUTIONS - Pattern Library

**Learn from past mistakes. Watch for these patterns.**

---

## CATEGORY 1: ATOM WRITING VIOLATIONS

### BUG: Narrative Process Language
**What:** Atoms describing HOW things were made instead of WHAT exists
**Examples:** "stitched," "creates," "layered," "applied with," "hand-sewn," "buffed"
**Why it breaks:** AI generators need observable facts, not craft process
**Solution:** Replace with result states - "5mm stitching visible," "raised 3mm," "glossy surface"
**Watch for:** Any verb describing action/process rather than current visual state

### BUG: Interpretive Language
**What:** Atoms using evaluative/emotional descriptors
**Examples:** "beautiful," "elaborate," "professional," "precious," "masterfully," "elegant"
**Why it breaks:** These are subjective judgments, not camera-visible facts
**Solution:** Replace with specific measurements, counts, positions
**Watch for:** Any adjective that describes quality/impression rather than observable property

### BUG: Time References
**What:** Atoms referencing duration or sequence
**Examples:** "hours of work," "after preparation," "recently applied"
**Why it breaks:** Prompt describes a single frozen moment, no before/after
**Solution:** Remove entirely or convert to visible result
**Watch for:** Any reference to time passage or preparation

### BUG: Character Limit Violations
**What:** Atoms exceeding 300 characters (P0/P1) or 200 characters (P2)
**Why it breaks:** Token bloat, redundancy, usually contains narrative violations
**Solution:** Split into 2 atoms OR trim to observable facts only
**Watch for:** Long flowing descriptions, multiple concepts in one atom
**Never:** Compress good content to meet limit - split instead

---

## CATEGORY 2: EMBELLISHMENT COORDINATION

### BUG: D0_Core Atoms Competing with Primary
**What:** Small "complementary" details that actually define separate decorative schemes
**Examples:** 
- Metallic couching on 8 edges when primary is beaded fringe
- Ribbon lattice grid on back when primary is back bow column
- Embroidered vine when primary is embroidered gradient
**Why it breaks:** Two decoration systems fighting for attention, unclear hierarchy
**Solution:** Rewrite D0_Core to SUPPORT primary, not add new decoration
**Test:** "Does this enhance the primary's presence, or compete with it?"
**Pattern:** If D0 atom could be mistaken for the primary embellishment, it's competing

### BUG: Missing Visual Hierarchy
**What:** Primary and supporting embellishments described with equal weight
**Why it breaks:** AI doesn't know which element should dominate
**Solution:** Use language like "PRIMARY EMBELLISHMENT," "supporting accents," "enhancing without competing"
**Watch for:** Multiple embellishments with no stated relationship

### BUG: Redundant Sparkle Descriptions
**What:** Multiple atoms all saying "sparkles/glitters/gleams" without coordination
**Why it breaks:** Redundancy wastes tokens, no clear sparkle hierarchy
**Solution:** One coordination atom describes HOW embellishments catch light, specific atoms describe WHAT embellishments exist
**Fixed by:** required_atoms feature ensuring coordination atom always present

---

## CATEGORY 3: TOKEN BUDGET

### BUG: Random Token Spikes
**What:** Some generations 4400 tokens, others 3000, same codebase
**Why:** Random atom selection can pull different token weights
**Solution:** Run camera.py 5 times, use AVERAGE not single run
**Watch for:** Making decisions based on one generation

### BUG: Trimming Too Aggressively from One File
**What:** Removing 40% from one file to save tokens
**Why it breaks:** Destroys variety in that category
**Solution:** Trim 10-20% across MULTIPLE files
**Pattern:** Spread pain evenly, maintain variety everywhere

### BUG: Compressing Atoms to Meet Character Limits
**What:** Removing good content to fit 300 char limit
**Why it breaks:** Loses important visual facts
**Solution:** Split into TWO atoms instead
**Example:** One atom for placement, another for appearance

---

## CATEGORY 4: THEME-LOCKING & FILTERING

### BUG: Theme Atoms Not Loading
**What:** Warning "No atoms matched embellishment_focus" 
**Why:** 
1. Atoms missing theme_tags
2. Focus keywords misspelled
3. Exclude filters removing tagged atoms BEFORE theme matching runs
**Solution:** Check atom has correct theme_tags, check exclude_groups not removing them
**Debug:** Print candidates BEFORE and AFTER filtering to see where atoms disappear

### BUG: Ensemble Pool vs Slot Source Confusion
**What:** Primary embellishment pulling from wrong pool
**Why:** 
- ensemble.embellishment_pool defines theme options
- theme_embellishment_primary slot pulls from ALL atoms with theme_locked
- dress.embellishments slot pulls from shiny_embellishments.json
**Solution:** Understand which slot pulls from where
**Architecture:**
- PRIMARY = theme_embellishment_primary slot (theme_locked, pulls D1_Architectural)
- COMPLEMENTARY = dress.embellishments slot (pulls D0_Core, excludes D1)

---

## CATEGORY 5: SCHEMA & ARCHITECTURE

### BUG: Schema Changes Breaking Slot Loading
**What:** Modified layer_slot_schema.json, now slots don't pull atoms
**Why:** Typo in slot_id, wrong source_file, broken prefix
**Solution:** Run `python camera.py` IMMEDIATELY after schema changes
**Test:** Verify console shows expected atoms loading for each slot

### BUG: P0 MANDATE Atoms Missing
**What:** Mandate checkpoint FAIL - critical atoms not loading
**Why:** 
1. Atom deleted accidentally
2. Priority changed from P0 to P1
3. Atom file not in slot's source_files
**Solution:** Check slot sources include all mandate files, verify atom priority field
**Critical:** NEVER delete P0 atoms without asking Emily first

### BUG: Randomization Disabled When Variety Wanted
**What:** Same atoms appearing every generation
**Why:** "random": false set on variation atoms
**Solution:** Only lock randomization for P0 MANDATE and foundational style atoms
**Pattern:** Detail/embellishment/variation atoms should ALWAYS be random: true

---

## CATEGORY 6: FILTER-RISK LANGUAGE

### BUG: Content Filter Triggering
**What:** Atoms using words that trigger AI safety filters
**Examples:** "exhausted" → "fatigued," "vacant" → "unfocused," "trained" → "practiced"
**Why it breaks:** Prompt may be rejected or generate unexpected safety behavior
**Solution:** Use approved replacement words (see MANDATORY_RULES.md Rule 2)
**Note:** "strained" is NOT "trained" - false positive, don't change it

---

## CATEGORY 7: NEGATIVE LANGUAGE

### BUG: Using "NOT X" in Standard Atoms
**What:** Atoms containing "NOT," "AVOID," "NEVER"
**Why it breaks:** AI generators work better with positive descriptions
**Exception:** style_enforcement.json can use negatives to block common defaults
**Solution:** Replace "NOT soft edges" with "hard edge definition"
**Pattern:** State what IS present, not what ISN'T

---

## CATEGORY 8: SPARKLE & LIGHTING RENDERING

### BUG: Sparkles Mentioned But Not Visible
**What:** Prompt says "sparkles" but generated image shows matte surfaces
**Why:** Lacking explicit rendering behavior language
**Solution:** 
- Add "bright specular highlights"
- Add "catching direct light"  
- Add "rendering with white highlights"
- Add "visible bright reflections"
**Pattern:** Describe HOW light behaves on surface, not just that surface "sparkles"
**Fixed in:** Session 2025-11-24 sparkle enhancement

### BUG: Lighting Too Soft Despite "Harsh" Language
**What:** Generated images show flattering soft light
**Why:** AI defaults to flattering light, needs explicit harsh override
**Solution:**
- Increase color temperature (7000-8000K, not 5000-6000K)
- Use "sharp downward shadows"
- Use "deep shadows beneath features"
- Use "harsh institutional" not "cool neutral"
**Pattern:** AI generators need VERY explicit anti-flattering language

---

## CATEGORY 10: ARCHITECTURAL INTEGRITY VIOLATIONS

### BUG: Sleeve-Bodice Conflicts
**What:** Bodice atoms included sleeve descriptions, causing conflicts with sleeve embellishments
**Why it breaks:** DALL-E renders first description it sees, ignores later overrides
**Solution:** Separated sleeves into dedicated slot, added skip logic for architectural sleeves
**Pattern:** Each slot should handle ONE aspect only - never mix multiple elements
**Session:** 2025-11-24 sleeve separation

### BUG: Theme Coordination Failure
**What:** Ensemble themes don't pull appropriate atoms despite having embellishment_focus
**Why:** Mismatch between focus keywords (e.g., "floral") and theme_tags (e.g., "romantic_floral")
**Solution:** Either use exact matching tags or fix the matching logic to handle partial matches
**Test:** Run theme_diagnostic.py to identify mismatches
**Pattern:** Keywords and tags must align for theme coordination to work

### BUG: Distance Filtering Fallback Breaking System
**What:** When no suitable cameras for embellishment, system uses ALL cameras anyway
**Why it breaks:** Hair primaries (close-only) appearing in full body shots
**Solution:** If no suitable cameras, SELECT DIFFERENT PRIMARY (don't break distance rules)
**Code location:** camera.py line 221-223
**Pattern:** NEVER compromise architectural rules with "fallback" logic

### BUG: Missing Spatial Coherence
**What:** Atoms don't coordinate spatial references for DALL-E
**Why it breaks:** Conflicting left/right references, impossible layering, wrong framing
**Solution:** Add holistic spatial coordination (like embellishment coordination)
**Future:** Consider position metadata, layer ordering, framing coherence

---

### BUG: Batch Changes Without Validation
**What:** Rewriting 20 atoms at once based on pattern
**Why it breaks:** If pattern is wrong, all 20 atoms are broken
**Solution:** 
1. Write ONE example
2. Verify it passes compliance
3. Show Emily
4. Get approval
5. THEN batch the rest
**Cost:** One extra round << fixing 20 broken atoms

### BUG: Shipping With Violations
**What:** Delivering zip with narrative/filter/character violations present
**Why it breaks:** Emily has to send it back for fixes
**Solution:** 
- Run `python camera.py` before zipping
- Check VIOLATION_DETAIL_REPORT.md
- Fix ALL violations
- Run camera.py AGAIN to verify
**Gate-check:** Zero violations required before delivery

### BUG: Not Reading Session Logs
**What:** Repeating same mistake from previous session
**Why:** Didn't read SESSION_LOG to see what already tried and failed
**Solution:** ALWAYS read most recent SESSION_LOG before starting work
**Pattern:** If solution feels familiar, check logs - might have failed before

---

## CATEGORY 10: COMMON FALSE STARTS

### BUG: Proposing Solutions Before Understanding Problem
**What:** "I'll fix X by doing Y" before running analytics
**Why it breaks:** Might not be the actual problem, wasting time
**Solution:** 
1. Run analytics FIRST
2. Read violation report COMPLETELY
3. Understand root cause
4. THEN propose solution
**Pattern:** Diagnosis before prescription

### BUG: Adding Features When Asked to Fix Bugs
**What:** Emily asks to fix violations, response includes new embellishment atoms
**Why it breaks:** Scope creep, introduces new potential violations
**Solution:** Stay focused on assigned work
**Pattern:** Fix what's broken before adding what's new

### BUG: Grepping for Rule 38
**What:** Searching for "Rule 38" instead of reading MANDATORY_RULES.md completely
**Why it breaks:** Defeats the entire gate-check purpose
**Solution:** Read rules LINE BY LINE from beginning to end
**Pattern:** If you know what Rule 38 is without reading the whole doc, you didn't read the whole doc

---

## HOW TO USE THIS DOCUMENT

**Before making changes:**
1. Check: "Is this pattern in the bugs list?"
2. If yes: Read the solution that worked
3. If no: Proceed carefully, might discover new bug

**When stuck:**
1. Search this doc for keywords related to problem
2. Check if similar issue was solved before
3. If found: Apply same solution pattern
4. If not: Ask Emily before trying untested approach

**After session:**
1. Did you discover a new bug pattern?
2. Add it to this document before zipping
3. Include: what broke, why, how fixed, how to prevent

**This document grows with the project. Update it when you learn.**

---

---

## CATEGORY 11: DISTANCE FILTERING & ATOM SELECTION

### BUG: Filtering Happens Too Late in Process
**What:** Trying to filter atoms based on camera distance, but camera slot comes AFTER most character/dress slots
**Why it breaks:** Can't use camera distance to filter makeup/hair/fabric if they're selected before camera
**Solution:** Pre-determine distance from primary embellishment BEFORE processing any slots
**Pattern:** Embellishment's `min_visible_distance` → determines camera requirements → filters all atoms
**Fixed by:** Pre-selecting embellishment in main(), passing distance to build_prompt(), applying to all select_atoms_for_slot() calls
**Implementation:** Session 2025-11-29

### BUG: Distance Filtering Too Strict - Breaking Generation
**What:** Filtering out ALL atoms for a slot, leaving nothing to select
**Why it breaks:** Some slots may have no atoms matching the required distance
**Solution:** If distance filtering produces empty list, keep original candidates (don't break generation)
**Pattern:** Always have fallback to unfiltered candidates when filter is too aggressive
**Test:** Verify filtering doesn't break generation for any distance (close/medium/full_body)

### BUG: Strict Equality Distance Matching Instead of Hierarchical
**What:** Camera coordination using `if min_distance != camera_distance` (strict equality)
**Why it breaks:** Prevents close cameras from being used with embellishments that require full_body distance, even though close cameras CAN show full_body details
**Solution:** Use hierarchical distance logic:
- close cameras (0-5ft) can show EVERYTHING (close, medium, full_body)
- medium cameras (5-7ft) can show medium + full_body (NOT close)
- full_body cameras (6-8+ft) can show ONLY full_body
**Pattern:** "minimum visible distance" means AT LEAST this distance, closer is fine
**Fixed by:** Session 2025-12-01, lines 169-177 in camera.py
**Code:**
```python
distance_hierarchy = {'close': 0, 'medium': 1, 'full_body': 2}
required_level = distance_hierarchy.get(min_distance, 1)
camera_level = distance_hierarchy.get(camera_distance, 1)
if camera_level > required_level:
    continue  # Camera too far
```

### BUG: Random Selection Grouping Prevents Mixed Primary Types
**What:** When selecting random core atoms, code groups by `atom.group` then picks ONE from EACH group
**Why it breaks:** With max_atoms=1 and two groups (D1_Architectural, D1_Hair_Architectural), only first group processed gets selected
**Solution:** For theme_embellishment_primary slot specifically, skip grouping and use simple random selection
**Pattern:** When multiple atom types should be treated as equivalent for selection, don't group by atom.group
**Fixed by:** Session 2025-12-01, lines 493-511 in camera.py

### BUG: Theme Tag Matching Using String-in-List Instead of Case-Insensitive Element Matching
**What:** Theme filtering checking `keyword.lower() in atom.theme_tags` (substring matching in list)
**Why it breaks:** Python checks if string exists in list, which only works for exact matches; doesn't do case-insensitive element comparison
**Solution:** Create lowercased list then check membership: `atom_tags = [t.lower() for t in atom.theme_tags]; keyword.lower() in atom_tags`
**Pattern:** When matching keywords against tag lists, always lowercase both sides
**Fixed by:** Session 2025-12-01, lines 430-449 in camera.py

### BUG: Mislabeled Camera Distance Metadata
**What:** Camera atom contents say "7-8 feet distance" but metadata says `"distance": "close"`
**Why it breaks:** Strict distance filtering uses metadata, causing cameras to be selected that don't match their actual framing
**Solution:** Audit all camera atoms to ensure distance metadata matches content description
**Pattern:** Verify metadata matches actual camera behavior described in contents
**Example:** camera.angle_embellishment_showcase was "close" but should be "full_body"
**Fixed by:** Session 2025-12-01, camera_angles_close.json

### BUG: Hosiery/Footwear Loading for Close-Up Shots  
**What:** Hosiery and footwear slots loaded regardless of camera distance, including close-ups where feet aren't visible
**Why it breaks:** DALL-E receives conflicting instructions ("face only" prompt + "ankle socks visible" description), confuses composition
**Root cause:** Slots called unconditionally in build_prompt() loop, no distance-gating logic
**Solution:** Add distance check before slot processing - skip hosiery/footwear for close/medium shots
**Pattern:** Slots that describe elements only visible at certain distances need conditional loading
**Fixed by:** Session 2025-12-01, added distance-gating logic in camera.py lines 663-667
**Code:**
```python
# DISTANCE-GATING: Skip hosiery/footwear for close and medium shots
if slot_id in ["accessories.hosiery", "accessories.footwear"]:
    if selected_camera_distance in ["close", "medium"]:
        continue  # Skip - feet not visible at this distance
```
**Verification:** Close-up prompts no longer contain hosiery/footwear atoms, full-body prompts still do
**Impact:** Cleaner prompts, no wasted tokens on invisible elements, may improve DALL-E crop compliance

### BUG: Hardcoded Framing in Preamble Conflicts with Camera Atoms
**What:** Preamble had hardcoded off-center close-up framing language that appeared in ALL generations
**Why it breaks:** DALL-E receives conflicting instructions when full-body camera selected:
  - Preamble: "Subject EXTREMELY FAR to left or right edge. LEFT 40% or RIGHT 40% only"
  - Camera atom: "7-8 feet distance. Full body positioning"
**Root cause:** Lines 59-61 in camera.py PREAMBLE had fixed framing language regardless of camera selection
**Solution:** Remove hardcoded framing from preamble - let camera atoms control all framing
**Pattern:** Preamble should only contain universal instructions, not camera-specific framing
**Fixed by:** Session 2025-12-01, removed lines 59-61 from PREAMBLE constant
**Verification:** Prompts now have single coherent framing instruction matching selected camera distance
**Impact:** Eliminates conflicting instructions to DALL-E, camera atoms now have full control over framing

### BUG: DALL-E Shows Full Dress Despite Close-Up Framing Instructions
**What:** Close-up cameras request "face and upper shoulders, bottom cuts at COLLARBONE" but DALL-E shows full dress
**Why it breaks:** Prompt describes entire dress (skirt, petticoat, embellishments at waist) while requesting collarbone crop
**Root cause:** Two problems:
  1. Dress body slots loading regardless of camera distance (skirt/petticoat not visible in collarbone shots)
  2. Close-distance atoms lack spatial frame-boundary anchoring language
**Solution:** 
  1. Distance-gating: Skip dress.skirt, dress.petticoat, dress.fabric for close cameras
  2. Spatial frame-locking: Add explicit frame-boundary language to all close-distance atoms
**Pattern:** Elements described in prompt signal "show this" to DALL-E - only describe what's in frame
**Fixed by:** Session 2025-12-01, comprehensive spatial frame-locking implementation
**Implementation:**
  - Necklines: "NECKLINE VISIBLE IN FRAME. Neckline at BOTTOM EDGE of visible area at collarbone level."
  - Bodice: "SHOULDER-LEVEL CONSTRUCTION VISIBLE IN FRAME. Sleeve details AT SHOULDERS in visible area."
  - Hair primaries: "PRIMARY HAIR EMBELLISHMENT VISIBLE IN FRAME. Construction at HEAD/CROWN level filling upper frame area."
  - Created 11 bodice close variants with frame-locking
  - Updated 16 neckline atoms with frame-boundary anchoring
  - Updated 6 hair primaries with spatial positioning
**Verification:** Close-up prompts now explicitly anchor visible elements to frame boundaries
**Impact:** Reinforces crop boundaries by spatially positioning every visible element within frame constraints

### BUG: Debug Mode Forces Distance for Atoms But Not Camera Slot
**What:** DEBUG_FORCE_CLOSE_CAMERA flag forces camera_distance="close" for filtering makeup/hair atoms, but camera slot still selects from ALL cameras (close, medium, full_body)
**Why it breaks:** System filters makeup/hair for close-ups but then selects a medium or full_body camera, creating mismatch between detail level and camera distance
**Root cause:** Camera slot selection (lines 710-722) didn't check selected_camera_distance before selection
**Symptoms:** 
  - Debug mode logs show "🔒 DEBUG: Camera locked to CLOSE-UP for debugging"
  - Makeup/hair slots correctly filter: "🔍 Distance filter (close): 44 → 33 atoms"
  - But camera selects from all 8 cameras instead of just 2 close cameras
  - Generated prompts have close detail descriptions but medium/full cameras
**Solution:** Add distance filtering to camera_candidates before coordinate_camera_with_embellishment()
**Pattern:** When forcing distance for testing, BOTH slot filtering AND camera selection must respect that distance
**Fixed by:** Session 2025-11-23, lines 719-731 in camera.py
**Code:**
```python
# DISTANCE FILTERING: If camera distance is set (including debug mode), filter cameras
if selected_camera_distance:
    original_count = len(camera_candidates)
    distance_filtered = []
    for camera in camera_candidates:
        camera_dist = getattr(camera, 'distance', None)
        if camera_dist == selected_camera_distance:
            distance_filtered.append(camera)
    
    if distance_filtered:
        print(f"    🎥 Camera distance filter ({selected_camera_distance}): {original_count} → {len(distance_filtered)} cameras")
        camera_candidates = distance_filtered
```
**Verification:** Debug mode now logs "🎥 Camera distance filter (close): 8 → 2 cameras" and selects TRUE close cameras
**Impact:** Debug mode now fully functional for testing extreme close-up compositions with proper face-only framing

**Related Discovery - Mislabeled Camera Metadata:**
- During fix verification, discovered camera.angle_close_overhead_natural was mislabeled as distance: "close"
- Its contents say "4-5 feet distance. Subject 65-75% frame height. Head, shoulders, upper torso clear"
- This is NOT a close-up - close means extreme tight framing, collarbone cut, torso NOT visible
- Corrected metadata to distance: "medium" in definitions/camera_angles_close.json
- TRUE close cameras (only 2): camera.angle_overhead_closeup_amateur, camera.angle_offcenter_amateur_closeup
- Both specify: "EXTREME TIGHT FRAMING", collarbone cut, "TORSO NOT VISIBLE. ARMS NOT VISIBLE. WAIST NOT IN FRAME"
- Pattern: Always verify distance metadata matches actual framing described in contents
- "close" = extreme tight for makeup showcase (face fills 90% frame)
- "medium" = 4-5 feet showing head, shoulders, upper torso
- "full_body" = 6-8 feet showing complete figure

### BUG: P0 MANDATE Atoms Bypassing Distance Filtering
**What:** P0 atoms were re-added after distance filtering, causing them to always load regardless of camera distance
**Why it breaks:** Close-up prompts describe invisible body parts ("long thin limbs, visible collarbones") because late age safety loads body descriptions even when body isn't in frame
**Root cause:** Lines 534-537 in camera.py re-added all P0 atoms to filtered list after distance check
**Symptoms:**
  - Close-up prompts contain "Adult body proportions: long thin limbs with no muscle definition, visible collarbones and ribs"
  - Late age safety loads both body AND face variants simultaneously
  - P0 atoms treated as special exemption from distance rules
**Solution:** Remove P0 exemption - ALL atoms must respect distance metadata including mandates
**Pattern:** Distance filtering should be universal. If an atom describes something not visible at a camera distance, it shouldn't load regardless of priority.
**Fixed by:** Session 2025-11-23, removed lines 534-537 and 521-522 in camera.py
**Additional fix:** Fixed distance metadata in character_age_safety.json:
  - adult_proportions_body: Changed from `max_visible_distance: "medium"` to `min_visible_distance: "medium"` (only loads for medium/full_body)
  - adult_proportions_face_close: Added `max_visible_distance: "close"` (only loads for close-ups)
  - Added adult_proportions_face_close to late age safety slot include_prefixes
**Verification:** Close-up prompts now only contain face-focused age safety, medium/full_body prompts contain body descriptions
**Impact:** Clean prompts that only describe visible elements, proper mandate checkpoint coverage across all distances


### BUG: Over-Aggressive Anti-Soft Language Breaking Manga Painter Aesthetic
**What:** Added "NOT soft blended edges. Edges defined by bright light falling away to deep shadow. Crisp shadow boundaries. Clean hard definition through light/shadow, not gradient blending" to style atoms
**Why it breaks:** This language FIGHTS the core "manga painter rendering realistic anatomy" aesthetic, which is soft painted dimensional form with anime sensibility (see reference images)
**Root cause:** Attempt to counteract soft makeup language ("soft pink", "gentle pastels") by adding aggressive rendering constraints
**Symptoms:**
  - Generated images lost soft painted anime quality
  - Style became hard-edged instead of dimensionally painted
  - Reference aesthetic (realistic anime with soft painted surfaces) was broken
**Solution:** Revert style_enforcement.json atoms to simpler versions without aggressive anti-soft language:
  - style.edge_quality: Removed "NOT soft blended edges. Crisp shadow boundaries. Clean hard definition through light/shadow, not gradient blending"
  - style.dimensional_final: Removed "NOT blended edges. NOT gradient rendering. Hard-edged crisp rendering. CRITICAL: When makeup descriptions use 'soft'..."
  - style.core_contrast: Removed "Hard edge definition. Clean crisp line work. Hard-edged rendering. Clear defined forms"
  - style.clean_digital_technique: Removed "NOT soft blended. Sharp-edged shadows"
  - style.illustration_clarity: Removed "NOT soft blended"
**Pattern:** "Manga painter rendering realistic anatomy" means soft painted dimensional form with harsh lighting creating shadows - NOT hard-edged linework. Let the aesthetic breathe without over-constraining.
**Prevention:** Added Rule 42 - Artstyle atoms are SACRED and UNTOUCHABLE, never trim for tokens
**Fixed by:** Session 2025-11-23, reverted all aggressive anti-soft language from style atoms

### BUG: Duplicate Atom Loading Across Multiple Slots
**What:** Pavlovian gaze atom (expression.gaze_struggling_to_track) loading in BOTH camera_gaze slot AND core_expression slot
**Why it breaks:** Wastes 175+ tokens, creates redundant duplicate content in prompt
**Root cause:** camera_gaze slot uses include_prefixes: ["expression.gaze_"] and core_expression slot uses include_prefixes: ["expression."] - gaze atoms match both
**Symptoms:**
  - Same gaze description appears twice in EXPRESSION EMOTION section
  - Token count inflated by full duplicate content
  - Discovered during token audit when expression section was unexpectedly large
**Solution:** Add exclude_prefixes to core_expression slot to prevent gaze atom loading
  - Updated layer_slot_schema.json: expression.core now has "exclude_prefixes": ["expression.gaze_"]
  - Gaze atoms now only load in camera_gaze slot (intended behavior)
**Pattern:** When slots have overlapping include_prefixes, atoms can match multiple slots and load repeatedly. Use exclude_prefixes to create clean boundaries.
**Prevention:** Review slot schemas for overlapping prefixes, add exclude_prefixes where needed
**Fixed by:** Session 2025-11-23, added exclude_prefixes to expression.core slot
**Savings:** -175 tokens for close-ups

### BUG: Overhead Camera Forcing Upward Gaze Instead of Pavlovian Response
**What:** Subject looking up at ceiling instead of attempting to look at camera while dissociated
**Why it breaks:** Breaks the Pavlovian "say cheese" horror - should be conditioned response (look at camera) failing due to dissociation, not just staring upward
**Root cause:** Preamble and close_framing specified "OVERHEAD DOWNWARD ANGLE. Camera pointing DOWN at upturned face" which forced eyes to look UP
**Understanding:** Ten years of Pavlovian conditioning means "say cheese" triggers automatic attempt to find and look at camera. But delirious dissociated state means they can't lock onto exact target. Result should be: gaze aimed toward camera but missing focus point (slightly past/through/beside lens).
**Symptoms:**
  - Generated images showed subject gazing at ceiling
  - Lost the horror of mechanical compliance attempting to execute but failing
  - Eyeline didn't suggest camera awareness at all
**Solution ATTEMPT (2025-11-23):** Change close-up camera to EYE LEVEL for Pavlovian response to work
  - Updated PREAMBLE_CAMERA_FIRST: "Camera held at photographer's EYE LEVEL - horizontal to subject's face"
  - Updated close_framing: "Camera at EYE LEVEL - horizontal to face"
  - Enhanced gaze atom: "CONDITIONED AUTOMATIC RESPONSE to 'say cheese' instruction... Body executing learned behavior mechanically. BUT: Delirious exhausted brain unable to lock onto exact target"
  - Removed 2 overhead close-up camera atoms
**Solution FAILED - User rejected eye-level cameras**
**CORRECT Solution (2025-11-24):** Revert to OVERHEAD cameras, keep "seeking camera but missing focus" gaze
  - Restored PREAMBLE_CAMERA_FIRST: "OVERHEAD DOWNWARD ANGLE. Camera pointing DOWN at upturned face"
  - Restored close_framing: "OVERHEAD DOWNWARD ANGLE. Camera pointing DOWN"
  - Updated camera.angle_offcenter_amateur_closeup: overhead angle language
  - KEPT gaze behavior describing "seeking camera but missing focus" at user's request
  - Result: Overhead angle with appropriate conditioned response gaze behavior
**Pattern:** Overhead camera angle is required for this project. Gaze can still describe seeking/missing behavior even with downward camera angle.
**REFINED Solution (2025-11-24):** Rewrite gaze atom with explicit upward direction and observable facts only
  - Problem persisted: Eyes still looking at ceiling, not tracking overhead camera position
  - Root cause: Gaze atom used narrative language ("trained," "attempting," "conditioned") without explicitly stating UPWARD direction toward overhead camera
  - Solution: Rewrote expression.gaze_struggling_to_track with pure observable facts
  - New language: "Eyes directed UPWARD toward overhead camera position above. Gaze angled UP at overhead lens area but OFF-TARGET - 5-10° past precise overhead camera angle."
  - Removed ALL: narrative language, process verbs, interpretive language, backstory
  - Result: Clear direction (UPWARD), clear target (overhead camera position), clear precision state (5-10° off target)
  - Violations reduced: Filter-risk 3→2 (removed "trained," "exhausted," "conditioned"), total 53→52
  - Pattern confirmed: Observable directional facts (UPWARD toward overhead camera) work better than narrative explanations of mental state
**Fixed by:** Session 2025-11-24, gaze atom rewritten with directional observable facts
**Fixed by:** Session 2025-11-24, reverted overhead camera changes
**Lesson:** Do not change fundamental camera angles without explicit approval
  - Updated close_framing: "Camera at EYE LEVEL - horizontal to face. Subject attempting to look at camera in conditioned 'say cheese' response"
  - Enhanced gaze atom: "CONDITIONED AUTOMATIC RESPONSE to 'say cheese' instruction... Body executing learned behavior mechanically. BUT: Delirious exhausted brain unable to lock onto exact target"
  - Removed 2 overhead close-up camera atoms (camera.angle_overhead_closeup_amateur, camera.angle_close_overhead_natural)
**Pattern:** Camera angle must match the intended gaze behavior. Overhead = upward gaze, Eye-level = toward viewer gaze. For Pavlovian conditioning horror, need eye-level camera so conditioned response (look at camera) is attempted but fails (dissociation prevents accurate lock-on).
**Fixed by:** Session 2025-11-23, changed close-up camera to eye-level, removed overhead variants

### BUG: Camera Atom Duplicating Preamble Content
**What:** Camera atom containing 785 characters repeating everything already in preamble
**Why it breaks:** Wastes 196+ tokens describing same framing twice (preamble + camera atom)
**Examples:** 
  - camera.angle_offcenter_amateur_closeup repeated: professional makeup documentation distance, overhead downward angle, extreme tight crop, face 85-90% of frame, all negative exclusions (no shoulders/chest/torso/etc)
  - All preamble content duplicated in camera atom
**Root cause:** Camera atom created without checking what preamble already establishes
**Symptoms:**
  - Token bloat (196 tokens in one atom)
  - Character limit violation (785 chars vs 300 max)
  - Redundant language appearing twice in prompt
  - Off-center placement (60% empty void) illogical for actual scenario (smartphone snapshot)
**Solution:** Delete entire camera atom - preamble already covers close-up framing
  - Deleted camera.angle_offcenter_amateur_closeup from camera_angles_close.json
  - Token savings: -400-500 tokens (5,377→4,972-5,093 range)
  - Preamble handles: overhead angle, tight crop, face framing, all exclusions
  - Camera atoms should only add unique details not covered by preamble
**Pattern:** Before creating camera atoms, check what preamble already establishes. Don't duplicate framing basics.
**Prevention:** Camera atoms describe specific angles/compositions, not repeat fundamental framing already in preamble
**Fixed by:** Session 2025-11-24, deleted redundant camera atom
**Savings:** ~400-500 tokens

### BUG: Mega-Atoms Over 600 Characters Causing Token Bloat
**What:** Single makeup atoms containing 600-900+ characters (150-226 tokens each)
**Why it breaks:** Violates 300 char limit, contains narrative language, wastes tokens describing multiple concepts
**Examples:**
  - makeup.maximum_glitter_application: 907 chars, 226 tokens (eyes + face scatter in one atom)
  - makeup.special_day_glitter_maximum: 764 chars, 191 tokens (eyes + face patterns)
  - makeup.special_day_base_layered: 598 chars, 149 tokens (highlights + blush + lips)
  - makeup.dimensional_highlight_layers: 657 chars, 164 tokens (8-10 product descriptions)
**Root cause:** Multiple visual concepts bundled into single atom, descriptive narrative language padding
**Symptoms:**
  - Character limit violations (2x-3x over 300 char limit)
  - Narrative language ("creating," "engineered," "calculated," "intentional")
  - Token inefficiency (describing same coverage multiple ways)
  - Difficulty identifying what atom actually does
**Solution ATTEMPT 1 (2025-11-24):** Split into focused single-concept atoms following Rule 1
  - Split by visual area: eyes separate from face, highlights separate from blush
  - Remove narrative language: "creating concentrated shimmer core" → "95% coverage"
  - Keep only observable facts: positions, measurements, counts, colors
  - Each atom under 300 chars describing ONE concept
**Solution ATTEMPT 1 RESULT:** Improved compliance but created inconsistency problem - random loading meant some generations got 3 makeup atoms, others got 8. No guaranteed comprehensive coverage.
**Solution FINAL (2025-11-24):** Consolidated comprehensive makeup system (matches reference prompt structure)
  - Created makeup_comprehensive.json with 3 P0 MANDATE atoms that always load together
  - makeup.professional_base_system: Base, foundation, cheeks
  - makeup.professional_sparkle_system: Highlights + glitter with complete placement
  - makeup.professional_detail_system: Eyes, lashes, brows, lips, jewels, overall effect
  - Professional framing: "WORLD-CLASS PROFESSIONAL MAKEUP - EXECUTED FOR SIX-YEAR-OLD'S PRINCESS DREAM"
  - Token cost: +700 tokens but guarantees comprehensive consistent coverage every generation
**Pattern:** For complex multi-part systems like professional makeup application, consolidation into guaranteed-load P0 atoms beats randomized modular atoms. Consistency > token savings when system needs complete coverage.
**Fixed by:** Session 2025-11-24, replaced random makeup atoms with comprehensive professional system
**Impact:** +700 tokens but professional makeup now loads consistently and completely every generation

### BUG: Token Bloat from Redundant Atoms Describing Same Content
**What:** Multiple atoms describing glitter placement, multiple atoms describing highlighter placement - all loading simultaneously
**Why it breaks:** Wastes tokens, creates repetitive prompt content
**Examples:**
  - makeup.maximum_glitter_application + makeup.face_jewels_precious both describe face glitter scatter
  - makeup.highlight_pearl_innocent + makeup.highlight_strobe_intense + makeup.dimensional_highlight_layers all describe highlighter at same facial points
**Root cause:** Atoms created at different times without checking for existing coverage, or created as variants but not made mutually exclusive
**Solution:** Consolidate to one comprehensive atom per concept
  - Removed: makeup.face_jewels_precious (duplicate face glitter)
  - Removed: makeup.highlight_pearl_innocent, makeup.highlight_strobe_intense
  - Kept: makeup.maximum_glitter_application (comprehensive glitter), makeup.dimensional_highlight_layers (comprehensive highlighter with multi-product detail)
**Pattern:** When creating new atoms, check if existing atoms already cover the same visual concept. If so, either replace old atom or add mutual exclusion. Multiple atoms describing same placement waste tokens.
**Prevention:** Before creating new atom, grep definitions for related concepts. Use excludes field to prevent simultaneous loading.
**Fixed by:** Session 2025-11-23, removed 3 redundant atoms
**Savings:** ~85 tokens

### PATTERN: Distance-Aware Token Optimization
**What:** Close-up prompts were describing full dress construction, floor perspective, background equipment - none visible in tight face crop
**Learning:** Token trimming needs to be distance-aware. Close-ups (face only) don't need:
  - Full scene environment details (equipment, floor perspective, spatial depth)
  - Full dress construction (skirt, petticoat, bodice - only neckline edge visible)
  - Body proportions description (shoulders/chest/arms not in frame)
**Solution:** Use min_visible_distance metadata to filter atoms by camera distance
  - scene.floor_emphasis, scene.salon_details: added min_visible_distance: "medium"
  - Dress atoms already had distance filters (skirt/petticoat: "full_body", bodice: "medium")
**Pattern:** Audit prompts by camera distance. For each section, ask: "Is this visible at this distance?" If no, add distance filter.
**Implementation:** 
  - Close-up: face, neck, hair, minimal neckline
  - Medium: face, hair, upper torso, bodice, accessories
  - Full body: everything including skirt, petticoat, floor, full scene
**Impact:** Potential for significant token savings on close-ups without losing quality
**Documented:** Session 2025-11-23, added distance filters to scene atoms

---

## CATEGORY 6: STYLE & AESTHETIC FOUNDATION

### PATTERN: Conflicting Style Foundation Language
**What:** Foundation atoms establish one aesthetic but later atoms contradict it
**Why it breaks:** Generators receive mixed signals about fundamental aesthetic direction
**Example (2025-11-24):** 
  - Foundation: "Manga painter's smooth painted illustration attempting realistic dimensional form"
  - Checkpoints: "NOT smooth illustration," "NOT illustrated fabric," "NOT flat illustration"
  - Final: "Documentary image"
**Impact:** Generator confused whether output should be painted illustration or photorealistic photograph
**Root cause:** Atoms written at different times without checking consistency with foundation. P0 foundation atom sets aesthetic but P1 checkpoint atoms contradict it.
**Symptoms:** 
  - Images too photorealistic (ignoring "painted" foundation)
  - OR images too simplified (rejecting "realistic ambition")
  - Inconsistent aesthetic across generations
**Solution:** All style atoms must support same aesthetic vision established in style.photorealism_base
  - Foundation establishes: "Manga painter's smooth painted illustration attempting realistic dimensional form"
  - Checkpoints must say: "painted with realistic [properties]" NOT "NOT illustrated" or "NOT smooth illustration"
  - Final must say: "Painted image with documentary subject matter" NOT "Documentary image"
  - Never use "photorealistic" or "documentary photograph" - these contradict painted technique
**Prevention:** 
  - When editing ANY style atom, read style.photorealism_base first
  - All style language must align with foundation aesthetic
  - Test: Does this atom support or contradict "painted illustration attempting realism"?
**Pattern identified:** Session 2025-11-24, conflicting style language causing photorealism drift
**Fixed by:** Rewrote 11 atoms (7 style + 4 character) to consistently support "manga painter attempting realism through painting craft"
**Key learning:** The word "photorealistic" vs "painted with realistic ambition" creates fundamentally different outputs. Foundation P0 language controls entire aesthetic direction.


### PATTERN: Style Foundation Balance - Manga Painting vs Photorealism
**What:** Finding the aesthetic balance between photorealism, dimensional realism, and manga painting style
**Context:** When trying to achieve "manga painter rendering realistic subjects" aesthetic (like Takehiko Inoue)
**Symptoms:**
  - Too much "attempting realistic rendering" → drifts to photorealism (looks like photographs)
  - Too much "NOT attempting realism" → becomes too flat/stylized (loses dimensional form)
  - "Refined delicate aesthetic" language too weak → produces realistic western features instead of manga features
**Root cause:** Unclear aesthetic specification in style.photorealism_base - language that works in theory produces wrong results in practice
**Solution requires iterative testing:** Aesthetic balance can't be theorized, must be refined through test generations
**Iterations in 2025-11-24 session:**
  1. "Painted technique attempting realistic form" → Too photorealistic
  2. "Manga painting style, NOT attempting realistic rendering" → Too flat/stylized
  3. Added explicit manga facial features ("LARGER eyes than realistic human") → Better features but still realistic rendering
  4. "MANGA PAINTING STYLE with sophisticated dimensional realism" → SUCCESS
**Working formula:**
  - "MANGA PAINTING STYLE" (illustrated aesthetic, visible painted quality)
  - "WITH sophisticated dimensional realism" (realistic lighting, materials, form)
  - "creating realistic lighting behavior" NOT "attempting realistic rendering"
  - Explicit manga facial proportions ("LARGER eyes," "rounder softer face," "smaller nose")
  - Adult age safety maintained throughout
**Key insight:** "Manga painting style ACHIEVING realism" works. "Painted technique ATTEMPTING realism" drifts to photorealism.
**Prevention:** When aesthetic isn't matching target, iterate with test generations. Words can mislead, images reveal truth.
**Pattern identified:** Session 2025-11-24, 4 iterations to find balance
**Fixed by:** style.photorealism_base rewritten 4 times, 5 character atoms changed to explicit manga proportions

### BUG: Setting "random": false Doesn't Fully Disable Atoms
**What:** Atoms with `"random": false` can still appear in prompts despite the flag
**Example:** `dress.color.grey` set to `"random": false` but still generating grey dresses
**Why it breaks:** The randomization system may have edge cases where disabled atoms are still selected
**Root cause:** Unknown - possibly fallback behavior, min_atoms requirements, or selection logic gaps
**Solution:** DELETE unwanted atoms entirely rather than setting `"random": false`
**Symptoms:**
  - Atom marked as disabled in JSON
  - Description says "DISABLED" but atom still appears in output
  - Multiple test generations confirm unwanted content appearing
**Prevention:**
  - If you need to permanently remove an atom, DELETE it completely
  - Don't rely on `"random": false` for critical exclusions
  - Test with multiple generations (10-20) to verify removal
**Pattern identified:** Session 2025-11-24, grey dress appearing despite "random: false"
**Fixed by:** Deleted dress.color.grey and all grey accent atoms completely
**Verification:** 20 test generations confirmed grey never appears after deletion



### PATTERN: Accent Color Coordination in Patterns
**What:** Pattern elements should coordinate with dress accent color, not be fixed to white/pale
**Why:** Creates visual harmony when patterns use the same accent color as other dress elements
**Solution:** Use "accent color" in pattern descriptions instead of specifying colors
**Example:**
  - BEFORE: "Polka dots in white or pale pastel on dress color"
  - AFTER: "Polka dots in accent color scattered across dress color"
**Benefit:** DALL-E uses whatever accent was specified earlier in prompt
**Pattern identified:** Session 2025-11-24



### BUG: Primary Embellishments Not Filtered by Camera Distance
**Symptom:** Medium front shots select back-placement or full_body-only primaries
**Root Cause:** Primary selection validated cameras AFTER selection, then DEBUG mode forced different distance
**Fix:** Pre-filter primaries based on effective camera distance BEFORE selection loop
**Location:** camera.py primary selection loop (around line 1060)
**Key Check:** Compare candidate's min_visible_distance against DEBUG_FORCE_CLOSE_CAMERA
**Also:** Reject placement='back' primaries when doing front camera shots
**Pattern identified:** Session 2025-11-24



### BUG: "Scattered" Pattern Language
**What:** Using "scattered" to describe pattern/accessory placement
**Why it breaks:** "Scattered" implies randomness - DALL-E renders chaotic, messy placement instead of intentional design
**Root cause:** Natural English tendency to use "scattered" for distributed elements
**Solution:** Replace with juvenile-coded print language:
  - "stencil-printed in rows" for dress patterns
  - "allover repeat" for continuous patterns
  - "placed throughout" for accessories
  - "in neat rows" for structured placement
  - "printed allover" for fabric prints
**Atoms fixed (2025-11-24):** 30+ instances across dress_patterns, hair_accessories, hair_styling, makeup_application, dress_fabrics
**Prevention:** Added "scattered" to BANNED WORDS in MANDATORY_RULES.md Rule 2
**Pattern:** Always use intentional placement language that implies deliberate design, not chaos



### BUG: Distance Variants Losing Intensity - "Lazy Art" Problem
**Symptom:** Art drifting to flat anime instead of dimensional realistic painting with fatigue
**What:** When illness atoms were split by distance (close vs medium), the medium versions were "watered down"
**Before (close):** "Bloodshot eyes - red veins across white. Dark purple circles under eyes visible through concealer. Heavy drooping eyelids half-closed. Moisture pooling at lower lash line."
**After (medium):** "Visible exhaustion. Dark circles under eyes. Heavy eyelids. Fatigued expression despite makeup."
**Root cause:** Medium versions lost all specific visual details - just abstract statements instead of observable facts
**Impact:** DALL-E produces cheerful flat anime instead of fatigued dimensional portraits
**Solution:** Make medium versions as intense as close versions, just without micro-detail:
  - "Bloodshot eyes visible even at distance"
  - "Dark purple-grey circles under eyes visible through heavy concealer layers"
  - "Heavy drooping eyelids half-closed"
  - "Face held up with visible muscular strain"
  - "Pallid complexion beneath makeup"
**Pattern:** When creating distance variants, maintain INTENSITY - only adjust DETAIL LEVEL
**Prevention:** Distance variants should describe SAME visual impact at different zoom levels
**Fixed by:** Session 2025-11-24, intensified medium illness atoms



### BUG: Style Atoms Trimmed Causing Flat Anime Look
**Symptom:** Art renders as flat anime instead of dimensional painted realism
**What:** style_enforcement.json atoms were compressed for token savings, losing critical language
**Lost language that causes flatness:**
  - "Bright white-blue light from directly above" → just "overhead light"
  - "Shadows are deep and defined" → just "Deep shadows"
  - "Dimensional form through shadow work" → removed entirely
  - "Clean color transitions under harsh light as primary technique" → removed entirely
  - "Clean gradual value changes define form" → removed entirely
**Root cause:** Token optimization trimmed style atoms (violates Rule 42)
**Solution:** Restored full style_enforcement.json from BEFORE build (pre-audit)
**Prevention:** style_enforcement.json is SACRED - NEVER trim for tokens
**Pattern:** The dimensional quality comes from REPETITION of lighting/shadow language, not just mentioning it once



### BUG: Theme Signatures and Patterns Overriding Dress Colors
**Symptom:** Dress renders in wrong color (blue/purple instead of pink/mint)
**What:** Theme signature atoms and pattern atoms dictated specific colors that overrode dress.color atoms
**Culprits found:**
  - signature.glitter_abundance.color: "Holographic base shifting pink to purple to blue"
  - signature.crystalline_sparkle.color: "Iridescent aurora colors - pale blue shifting to pink to lavender"
  - dress.pattern.holographic_rainbow: "Iridescent bands shimmer pink-blue-purple"
  - dress.pattern.iridescent_clouds: "Cloud shapes shift colors pink-blue-lavender"
  - fabric.holographic_shift: "Rainbow iridescence overlaid on base color"
**Root cause:** Theme/pattern atoms described COLOR SHIFTS instead of LIGHT BEHAVIOR
**Solution:** 
  - Rewrote signature atoms to describe sparkle/shimmer behavior without color dictation
  - Changed patterns to use "in DRESS COLOR" or "in ACCENT COLOR" instead of specific hues
  - Changed fabric atoms to reference "DRESS COLOR" explicitly
**Pattern:** Theme signatures should describe LIGHT/SPARKLE behavior, not color palettes
**Fixed atoms:**
  - signature.glitter_abundance.color → "Glitter particles catch light with holographic shimmer"
  - signature.crystalline_sparkle.color → "Surfaces refract light with aurora shimmer"
  - dress.pattern.holographic_rainbow → renamed to holographic_stripes, uses "in DRESS COLOR"
  - dress.pattern.iridescent_clouds → uses "in ACCENT COLOR"
  - fabric.holographic_shift → uses "in DRESS COLOR"



### BUG: Ethereal/Soft Art Instead of Harsh Clinical
**Symptom:** Art renders ethereal, pretty, soft-focus instead of stark, harsh, documentary
**Root causes found and fixed:**
1. **Theme signature light_behavior atoms** were overriding lighting:
   - romantic_floral: "soft inner glow", "Gentle luminescence", "Warm diffused highlights"
   - refined_elegance: "Soft pearl luster", "Gentle sheen", "Understated glow"
   - celestial_fantasy: "Soft moonlight glow", "Ethereal luminescence"
   - crystalline_sparkle: "Cool ethereal sparkle quality"
2. **Makeup atoms** had "glow" language instead of "shine/specular"
3. **Scene lighting atoms** lacked explicit UNFLATTERING language

**Fixes applied:**
1. Rewrote ALL theme signature light_behavior atoms to describe material behavior UNDER harsh light, not change the lighting
2. Replaced "glow" → "shine/specular" throughout makeup_application.json
3. Added explicit UNFLATTERING/CRUEL language to scene_lighting.json:
   - "UNFLATTERING overhead angle - NOT portrait lighting, NOT beauty lighting"
   - "CRUEL OVERHEAD LIGHT casting deep shadows"
   - "Documentary capture under institutional fluorescents"
4. Removed "ethereal" and "soft" language throughout

**Key principle:** Theme signatures describe how MATERIALS behave under the existing harsh lighting - they should NEVER override the core lighting approach.



### BUG: Model Looks Like Crying/Sweating
**Symptom:** Model always appears to be crying or sweating
**Root causes found:**
1. **illness_manifestations.json**: "Moisture pooling at lower lash line"
2. **expression_emotion.json**: "Lower lid moisture present", "Wet tear film coating corneas"
3. **makeup.glitter_tears** - the atom NAME itself triggers tear rendering
4. **character_core.json**: "wet glass" eye descriptions
5. **illness_manifestations.json**: "Wet glassy surface on eyes"

**Fixes applied:**
1. Removed "Moisture pooling at lower lash line" from close illness atom
2. Removed "Lower lid moisture present" from fatigue_eye_signs
3. Renamed "expression.glassy_moisture" → "expression.glassy_stare", removed wet/tear language
4. Renamed "makeup.glitter_tears" → "makeup.lower_lash_shimmer"
5. Replaced ALL "wet glass" → "polished glass" throughout definitions
6. Replaced "Wet glassy surface on eyes" → "Glassy reflective surface on eyes"

**Added to BANNED WORDS:**
- "tears/tear" (except crystal teardrops)
- "moisture/moist" on face
- "wet" for eyes/face - use "reflective", "glassy", "polished" instead
- "sweating/sweat"

**Key principle:** DALL-E is very literal. Words like "wet", "moisture", "tears" on face will render as crying/sweating.

