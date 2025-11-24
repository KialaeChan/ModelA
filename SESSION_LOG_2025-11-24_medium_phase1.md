# SESSION LOG - Medium Distance Phase 1: Holistic Violations Fix
**Date:** 2025-11-24
**Focus:** Remove elements below medium frame cut (spatial frame-locking Phase 1)
**Status:** ✅ COMPLETE

---

## PROBLEM IDENTIFIED

User feedback: "We've learned that giving DALLE a distance doesn't work. We need to spatially lock what is in the frame."

**Reference image analysis:**
Medium shots show: head, hair, neck, shoulders, upper torso, bodice, waist, upper skirt
Frame cuts at: MID-SKIRT (hip level)
NOT visible: lower skirt, hem, petticoat layers, legs, feet, floor

**Holistic violations found in medium prompts:**
1. Petticoat projection described (not visible - only top edge at waist)
2. Floor/flooring perspective mentioned (below frame cut)
3. Fabric atom mentioning "Petticoat visible through" (petticoat not in frame)
4. "Long thin limbs" implies legs (legs not visible in medium shots)
5. "Floor perspective uneven" in composition flaws (floor not visible)
6. Scene equipment "at depths" (implies floor-level, not visible)

---

## PHASE 1 QUICK FIXES APPLIED

### 1. Petticoat Atoms - Distance Filtering
**Action:** Added `min_visible_distance: "full_body"` to 6 petticoat atoms in petticoat_maximum_puff.json
**Atoms fixed:**
- dress.underskirt_maximum_tulle_cloud
- dress.underskirt_six_tier_ultra_gathered
- dress.underskirt_triple_circle_base
- dress.underskirt_crinoline_cage_tulle
- dress.underskirt_mega_poof_foundation
- dress.petticoat_visible_hem

**Additional fix:** Added `dress.petticoat` to medium-distance slot skip list in camera.py (line 816)
**Why needed:** Petticoat slot wasn't being filtered by atom distance metadata, needed slot-level gate

### 2. Floor Atoms - Distance Filtering & Content Fix
**Files modified:** scene_lighting.json, composition_flaws.json

**scene.luxury_salon_room:**
- Removed: "Polished grey laboratory flooring"
- Kept: Grey walls and laboratory space visible at depth

**scene.floor_emphasis:**
- Changed from `min_visible_distance: "medium"` to `"full_body"`
- Floor only visible in full-body shots

**scene.salon_details:**
- Before: "Equipment at depths - treatment chairs, carts, beauty dispensers"
- After: "Equipment behind subject at table height and wall-mounted - panels, carts, dispensers visible at mid-level"
- Reframed floor equipment as wall-height equipment

**composition.uneven_floor_tilt:**
- Changed from `min_visible_distance: "medium"` to `"full_body"`
- Floor perspective only relevant for full-body shots

### 3. Fabric Atom - Petticoat Reference Removed
**File:** dress_fabrics.json
**Atom:** fabric.batiste_cotton
- Removed: "Petticoat visible through"
- Kept: All other fabric behavior descriptions

### 4. Character Age Safety - Limbs Reference Fixed
**File:** character_age_safety.json
**Atom:** character.adult_proportions_body

Before:
```
Adult body proportions: long thin limbs with no muscle definition, visible collarbones and ribs, mature hands.
```

After:
```
Adult body proportions visible in upper body frame: thin arms visible to elbows with no muscle definition, narrow shoulders, visible collarbones and ribs, mature hands.
```

**Change:** "limbs" → "arms visible to elbows" (specific to what's actually in medium frame)

### 5. Camera Preamble - Stronger Frame Cut Language
**File:** camera.py (line 670)

Before:
```
UPPER BODY PORTRAIT. Frame shows head, shoulders, upper torso. Bottom of frame cuts at MID-TORSO or WAIST.
```

After:
```
MEDIUM UPPER-BODY PORTRAIT. Frame shows: COMPLETE head and hair, FULL neck and shoulders, COMPLETE upper torso and bodice, WAIST and upper skirt. Bottom of frame CUTS at MID-SKIRT (hip level). Shows waist-to-hip zone. Does NOT show: lower skirt, hem, petticoat layers, legs, feet, floor.
```

**Improvements:**
- Explicit "MID-SKIRT (hip level)" cut point
- Lists what IS visible (complete/full terminology)
- Lists what is NOT visible (explicit negatives)
- Matches reference image framing exactly

### 6. Camera Angle Atoms - Spatial Frame-Locking
**File:** camera_angles_close.json
**Atoms rewritten:** 2 medium-distance camera atoms

**camera.angle_three_quarter_elevated:**
Before: "5-6 feet distance. Three-quarter view: face, torso, dress details."
After: "MEDIUM UPPER-BODY FRAMING. Frame includes: complete head, full shoulders and torso, bodice, waist, upper skirt. Bottom of frame CUTS at mid-skirt (hip level)."

**camera.angle_elevated_quarter_turn:**
Before: "5-6 feet distance. Subject caught mid-turn at 45deg angle."
After: "MEDIUM UPPER-BODY FRAMING. Frame includes: complete head, full shoulders and torso, bodice, waist, upper skirt. Bottom of frame CUTS at mid-skirt (hip level). Subject caught mid-turn at 45deg angle."

**Key change:** Replaced distance language ("5-6 feet") with spatial frame boundaries (what's IN frame, where frame CUTS)

---

## TOKEN IMPACT

**Starting (before fixes):** 5,080 tokens
**After petticoat slot skip:** 4,881 tokens (-199)
**Final (all fixes):** 4,839 tokens (-42)
**Total savings:** -241 tokens

---

## COMPLIANCE VERIFICATION

**System Status:**
- ✅ Code runs without errors
- ✅ All atoms load correctly
- ✅ Mandate checkpoint: PASS
- ✅ Token count: 4,839 (improved)
- ✅ Violations: 56 (unchanged - no new violations introduced)

**Holistic violations verification:**
```bash
grep -i "petticoat\|floor.*perspective\|floor.*visible\|long thin limbs" prompt.txt
```
**Result:** Only mentions are in preamble saying they're NOT visible ✓

---

## FILES MODIFIED (9 total)

1. `definitions/petticoat_maximum_puff.json` - Added full_body filter to 6 atoms
2. `definitions/scene_lighting.json` - Removed floor mentions, reframed equipment height
3. `definitions/composition_flaws.json` - Changed floor flaw to full_body only
4. `definitions/dress_fabrics.json` - Removed petticoat reference from fabric atom
5. `definitions/character_age_safety.json` - Fixed "limbs" to "arms visible to elbows"
6. `definitions/camera_angles_close.json` - Rewrote 2 medium camera atoms with spatial frame-locking
7. `camera.py` - Added petticoat to medium slot skip list + strengthened preamble
8. `MEDIUM_DISTANCE_FRAME_AUDIT.md` - Created comprehensive audit document
9. `SESSION_LOG_2025-11-24_medium_phase1.md` - This log

---

## WHAT'S NEXT (Phase 2)

**Phase 1 COMPLETE:** Removed holistic violations (elements below frame cut)

**Phase 2 TODO:** Add spatial frame-locking to visible elements
- Bodice atoms: "BODICE VISIBLE IN FRAME. Construction fills upper torso from shoulders to waist."
- Neckline atoms (medium): Add frame position anchoring
- Upper skirt atoms: "UPPER SKIRT VISIBLE AT FRAME BOTTOM. Begins to bell from waist."
- Scene atoms: Verify wall-height equipment appropriate

**Testing needed:**
- Generate 3-5 medium prompts
- Verify NO elements below frame cut described
- Verify spatial anchoring effective when added

---

## KEY LEARNINGS

**What worked:**
1. Slot-level gating (dress.petticoat skip) more reliable than atom distance filters for mandate atoms
2. Explicit frame cut language ("MID-SKIRT (hip level)") clearer than vague "waist"
3. Lists of what's NOT visible as effective as what IS visible
4. Reframing equipment "height" rather than removing entirely maintains scene atmosphere

**For Phase 2:**
- Medium-distance atoms need less aggressive frame-locking than close-ups (more visible area)
- Focus on anchoring PRIMARY elements (bodice, neckline) to frame boundaries
- Upper skirt can use "begins to bell at waist" language (top edge visible)

---

**Phase 1 complete. Medium shots no longer describe elements below frame cut. Ready for Phase 2 spatial frame-locking.**
