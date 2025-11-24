# Camera Atom Inventory - Complete Catalog
**Date:** December 1, 2025
**Purpose:** Systematic review for DALL-E composition tuning

---

## OVERVIEW

Total camera-related atoms across 2 files:
- **camera_angles_close.json**: 7 atoms (angles with distance metadata)
- **camera_relationship.json**: 6 atoms (body positioning/rotation states)

---

## DISTANCE CATEGORIES

### CLOSE CAMERAS (3-5 feet) - 2 atoms

**1. camera.angle_chest_up_close**
- Distance: 3 feet
- Current status: **MODIFIED WITH AGGRESSIVE LANGUAGE** (testing)
- Contents: "CLOSE-UP PORTRAIT. 3 feet camera distance. TIGHT FRAMING: Bottom of frame cuts at waist level. Legs NOT visible, feet NOT in frame, skirt hem NOT visible..."
- Reveals: bodice_center, front
- Locked: YES (for testing)
- **Issue:** DALL-E ignores this, renders full-body instead
- **Test pending:** Waiting for DALL-E to work

**2. camera.angle_close_overhead_natural**
- Distance: 4-5 feet
- Current language: "4-5 feet distance. Subject 65-75% frame height. Head, shoulders, upper torso clear..."
- Reveals: bodice_center, shoulder, front
- **Issue:** Likely also ignored by DALL-E (not yet tested)
- **Needs:** Aggressive language like chest_up_close

---

### MEDIUM CAMERAS (5-7 feet) - 2 atoms

**3. camera.angle_three_quarter_elevated**
- Distance: 5-6 feet
- Current language: "5-6 feet distance. Three-quarter view: face, torso, dress details. Subject 60-70% frame height..."
- Reveals: front, side, shoulder
- **Status:** Unknown if DALL-E respects this
- **Needs testing**

**4. camera.angle_elevated_quarter_turn**
- Distance: 5-6 feet
- Current language: "5-6 feet distance. Subject caught mid-turn at 45deg angle. Face in three-quarter view..."
- Reveals: front, side, diagonal_side
- **Status:** Unknown if DALL-E respects this
- **Needs testing**

---

### FULL-BODY CAMERAS (6-8+ feet) - 3 atoms

**5. camera.angle_medium_full_body_detail**
- Distance: 6-7 feet
- Current language: "6-7 feet distance. Full body head to feet, subject 75-85% frame height..."
- Reveals: front, side, back, hem
- **Status:** Likely works (DALL-E defaults to full-body)
- **Low priority for tuning**

**6. camera.angle_medium_overhead_full**
- Distance: 6-8 feet
- Current language: "6-8 feet distance. Full body head to feet, subject 75-80% frame..."
- Reveals: front, hem, skirt, circumference
- **Status:** Likely works (DALL-E defaults to full-body)
- **Low priority for tuning**

**7. camera.angle_embellishment_showcase**
- Distance: 7-8 feet
- Current language: "7-8 feet distance. Full body positioning with elevated angle..."
- Reveals: front, bodice_center, shoulder, diagonal_side
- **Status:** Likely works (DALL-E defaults to full-body)
- **Low priority for tuning**

---

## CAMERA RELATIONSHIP ATOMS (6 atoms)

These describe body positioning/rotation state, not distance. All marked as "medium" distance in metadata but function as modifiers to angle atoms.

**All 6 atoms:**
1. camera.turn_just_completed - "Body square to lens. Dress swaying from recent rotation..."
2. camera.turn_three_quarter - "Body 45deg from frontal. Shoulders rotating toward lens..."
3. camera.turn_overshot_correcting - "Body rotated beyond camera position..."
4. camera.turn_halfway_stalled - "Body 60deg from frontal. Partial rotation then stopped..."
5. camera.head_leads_body_lags - "Face oriented to lens, neck twisted, shoulders still rotating..."
6. camera.body_leads_head_follows - "Body square to camera, shoulders and torso frontal. Head still turning in..."

**Issue:** These work independently of distance atoms, could cause conflicts.

---

## PRIORITY TUNING ORDER

### PHASE 1: CLOSE CAMERAS (CRITICAL)
**Problem:** DALL-E completely ignores close-up framing, renders full-body instead
**Status:** Testing aggressive language on chest_up_close
**Next:** If test works, apply to close_overhead_natural

### PHASE 2: MEDIUM CAMERAS (HIGH)
**Problem:** Unknown if DALL-E respects 5-6 feet framing
**Status:** Not yet tested
**Next:** Test current language, then apply aggressive pattern if needed

### PHASE 3: FULL-BODY CAMERAS (LOW)
**Problem:** Likely already working (DALL-E defaults here)
**Status:** Probably fine
**Next:** Verify they don't need changes

---

## AGGRESSIVE LANGUAGE PATTERN (from chest_up_close test)

**Elements that might help DALL-E:**
1. "CLOSE-UP PORTRAIT" (composition type)
2. "TIGHT FRAMING" (explicit crop intent)
3. "Bottom of frame cuts at waist level" (specific crop line)
4. "Legs NOT visible, feet NOT in frame" (negative exclusions)
5. "Subject fills 85-90% of frame height" (fill percentage)
6. "NOT full body shot, NOT distant framing" (negative blocking)
7. "Waist-up cropping only" (explicit crop type)

**To test:** Does this actually work, or does DALL-E still ignore it?

---

## QUESTIONS FOR TESTING

1. **Does aggressive language work for close cameras?** (pending test)
2. **Do medium cameras need aggressive language?** (unknown)
3. **Are full-body cameras already working?** (probably yes)
4. **Do camera_relationship atoms interfere with distance?** (unknown)
5. **Should distance be in PREAMBLE instead?** (escalation option)

---

## NEXT STEPS

**WAITING:** Test result from aggressive chest_up_close language
**IF SUCCESS:** Apply pattern to all close + medium cameras
**IF FAILURE:** Escalate to preamble-level distance specification
**AFTER:** Systematic testing of all 3 distance categories

---
