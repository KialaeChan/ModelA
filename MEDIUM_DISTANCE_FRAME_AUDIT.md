# MEDIUM-DISTANCE SPATIAL FRAME AUDIT
**Date:** 2025-11-24
**Reference:** Portrait framing showing head, shoulders, upper torso, bodice, waist + upper skirt
**Frame Cut:** Bottom edge cuts at MID-SKIRT (hip/upper thigh level)

---

## REFERENCE ANALYSIS

Based on uploaded reference image, medium framing includes:

**VISIBLE IN FRAME:**
- Complete head with hair and hair accessories
- Full neck and shoulders
- Complete upper torso (chest, upper back)
- Bodice construction (neckline, sleeves, bodice embellishments)
- Waist definition
- Upper skirt where it meets bodice (waistline + 4-6 inches below)
- Arms visible to elbow/mid-forearm area

**CUTS AT (NOT VISIBLE):**
- Mid-skirt level (hip to upper thigh)
- Lower skirt (bell, hem, full volume)
- Petticoat layers (only top edge of volume visible)
- Legs, feet, floor
- Full scene depth/perspective
- Background equipment at floor level

---

## CURRENT PROMPT ANALYSIS (Generated Medium-Distance)

### ✅ CORRECT SPATIAL FRAMING (Line 2)
```
UPPER BODY PORTRAIT. Frame shows head, shoulders, upper torso. Bottom of frame cuts at MID-TORSO or WAIST. Face and upper body fill frame. NOT full body shot. Legs NOT visible. Feet NOT visible.
```
**Assessment:** Good start but needs strengthening - says "mid-torso or waist" but reference shows cut is BELOW waist in upper skirt

### 🚨 HOLISTIC VIOLATIONS (Elements Described But Not Visible)

**1. PETTICOAT (Line 54)**
```
PETTICOAT EXTREME WIDTH PROJECTION. Skirt stands OUT horizontally from body in wide bell dome.
```
**Problem:** Full petticoat projection not visible - only top edge of skirt volume visible at waist
**Fix Needed:** Either remove for medium distance OR reframe as "upper skirt volume begins to bell out at waist"

**2. FLOOR/PERSPECTIVE (Line 61)**
```
Polished grey laboratory flooring. Laboratory flooring visible with perspective.
```
**Problem:** Floor completely below frame cut
**Fix Needed:** Remove floor mentions for medium distance OR add distance filter

**3. FABRIC BEHAVIOR (Line 55)**
```
Silk georgette. Subtle crepe texture with bounce. Holds pleats and gathers with springy volume. Semi-sheer with pebbled surface. Lively movement.
```
**Problem:** Describes full skirt fabric behavior when only upper portion visible
**Fix Needed:** Reframe for bodice/upper skirt fabric only

**4. SKIRT HEM (Line 53)**
```
Hem edge finished with scalloped wave pattern. Each scallop identical curved arc.
```
**Problem:** Hem edge far below frame cut
**Fix Needed:** Remove hem descriptions for medium distance

**5. LIMBS (Line 71)**
```
long thin limbs with no muscle definition
```
**Problem:** Legs not visible in medium shot, only arms to elbow
**Fix Needed:** Specify "thin arms visible to elbows" NOT "limbs" (implies legs)

**6. SCENE DEPTH (Line 61)**
```
Space extends beyond immediate surroundings. Room details showing laboratory facility. Equipment at depths - treatment chairs, carts, beauty dispensers.
```
**Problem:** Floor-level equipment not visible when frame cuts at upper body
**Fix Needed:** Reframe as "wall-mounted equipment" or "equipment at table height behind subject"

---

## SPATIAL FRAME-LOCKING STRATEGY

### Pattern from Close-Up Success:
Close-ups use: "VISIBLE IN FRAME. [Element] at [FRAME POSITION]. Detail visible in overhead view."

### Adapt for Medium Distance:

**1. Camera/Frame Introduction (Strengthen Line 2)**
```
MEDIUM UPPER-BODY PORTRAIT. Frame shows: COMPLETE head and hair, FULL neck and shoulders, COMPLETE upper torso and bodice, WAIST and upper skirt. Bottom of frame CUTS at MID-SKIRT (hip level). Shows waist-to-hip zone. Does NOT show: lower skirt, hem, petticoat layers, legs, feet, floor. Face and upper body fill vertical frame.
```

**2. Bodice/Dress Elements - Add Frame Anchoring**
```
BODICE VISIBLE IN FRAME. Bodice construction fills upper torso area from shoulders to waist. [construction details]. Bodice detail visible in upper body framing.
```

**3. Skirt - Reframe to Visible Portion Only**
```
UPPER SKIRT VISIBLE AT FRAME BOTTOM. Skirt begins to bell out from waist. Upper skirt edge visible where bodice meets skirt at waistline. Waist definition clear. Skirt volume begins in lower portion of frame.
```

**4. Scene - Remove Floor, Keep Wall/Depth**
```
Grey laboratory walls and equipment behind subject at table/wall height. Cold sterile environment visible at mid-level depth. Background equipment (wall-mounted panels, standing equipment) visible behind subject.
```

**5. Age Safety Late - Fix Limbs Reference**
```
Adult body proportions visible in frame: thin arms to elbows, narrow shoulders, visible collarbones, delicate upper body build. Waifish petite adult frame visible in upper body.
```

---

## ATOMS NEEDING MODIFICATION

### HIGH PRIORITY - Remove/Reframe:
1. **dress.petticoat_* atoms** - Add max_visible_distance: "full_body" OR reframe for upper portion only
2. **scene floor atoms** - Add max_visible_distance: "full_body" 
3. **dress.skirt hem descriptions** - Add max_visible_distance: "full_body"
4. **character.adult_proportions_body** - Remove "limbs", specify "arms visible to elbows"

### MEDIUM PRIORITY - Add Frame-Locking:
1. **dress.bodice_* atoms** - Add "BODICE VISIBLE IN FRAME" anchoring
2. **dress.neckline_*_medium atoms** - Add frame position language
3. **Camera angle atoms** - Strengthen frame cut description

### LOW PRIORITY - Verify Appropriate:
1. **dress.fabric atoms** - Check if describing full skirt or bodice fabric
2. **scene.room atoms** - Verify mentioning floor vs wall-height details

---

## RECOMMENDED APPROACH

**Phase 1: Quick Fix (Today)**
1. Add max_visible_distance filters to obvious violations (petticoat, floor, hem)
2. Fix character.adult_proportions_body limbs reference
3. Strengthen camera frame cut language

**Phase 2: Comprehensive Frame-Locking (Next)**
1. Add spatial anchoring to all bodice/dress atoms
2. Create medium-specific scene atoms (wall-height not floor)
3. Reframe skirt atoms for "upper skirt visible at frame bottom"

**Phase 3: Test & Iterate**
1. Generate 3-5 medium-distance prompts
2. Verify no elements described below frame cut
3. Verify spatial anchoring working

---

**Next step:** Proceed with Phase 1 quick fixes?
