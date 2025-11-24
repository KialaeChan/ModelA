# CRITICAL DISCOVERY: P0 MANDATE Atoms & Distance Filtering
**Date:** 2025-11-24
**Issue:** P0 MANDATE skirt atoms loading in medium shots despite min_visible_distance: "full_body"

---

## ROOT CAUSE IDENTIFIED

**Code behavior (camera.py line 312):**
```python
# If we filtered out everything, keep original candidates (don't break generation)
```

**What this means:**
- If ALL candidate atoms for a slot are filtered out by distance, the slot keeps the original candidates anyway
- This prevents generation from breaking when distance filtering is too aggressive
- But it means P0 MANDATE atoms that are ALL marked "full_body" will load even for close/medium shots

---

## SPECIFIC CASE: dress.skirt Slot

**Problem:**
- dress.skirt_short_length_mandate is P0 MANDATE
- It has min_visible_distance: "full_body"
- It's the ONLY skirt atom available for that pattern/style combination
- Distance filter finds NO medium-compatible skirt atoms
- Fallback: loads the full_body atom anyway

**Result in medium-distance prompts:**
```
Skirt Construction: CRITICAL: Skirt EXTREMELY SHORT - iliac crest or above - at fingertip level. 
Six extra-wide ruffle tiers. Each tier 10-12cm wide. Skirt extends 20-30cm wide horizontally...
```

This describes hem location (below medium frame cut), creating holistic violation.

---

## SOLUTION OPTIONS

### Option 1: Create Medium-Specific Skirt Atoms (RECOMMENDED)
Create new atoms that describe ONLY the upper skirt visible in medium frame:

```json
"dress.skirt_upper_volume_medium": {
  "contents": "UPPER SKIRT VISIBLE AT FRAME BOTTOM. Skirt begins to bell out from defined waistline. Upper skirt fabric shows gathering and volume beginning. Waist-to-hip transition visible where bodice meets skirt.",
  "priority": "P1: CORE",
  "min_visible_distance": "medium",
  "max_visible_distance": "medium"
}
```

**Advantages:**
- Describes only visible elements
- No holistic violations
- Natural spatial framing

**Disadvantages:**
- Requires creating medium variants for all skirt types
- More atoms to maintain

### Option 2: Make P0 Skirt Atoms Distance-Aware (Complex)
Rewrite P0 MANDATE skirt atoms to work at all distances:

```json
"contents": "Skirt construction: [always visible waist details]. At full_body distance: [hem details]."
```

**Advantages:**
- Single atom per skirt type
- Less maintenance

**Disadvantages:**
- Awkward conditional language
- Harder to write clearly
- Still describes elements not visible (just conditionally)

### Option 3: Remove Distance Fallback (DANGEROUS)
Modify camera.py to NOT load candidates when distance filtering produces empty set.

**Advantages:**
- Strict distance enforcement

**Disadvantages:**
- Could break generation entirely if no atoms match
- Would require comprehensive coverage at all distances
- High risk

---

## RECOMMENDED APPROACH

**Phase 1: Quick Fix (Today)**
1. Create 2-3 medium-specific skirt atoms covering common cases
2. Add max_visible_distance: "medium" to prevent full_body loading
3. Test medium generation with new atoms

**Phase 2: Comprehensive Coverage**
1. Create medium variants for all major skirt types
2. Create close variants for skirt waistline/upper edge only
3. Ensure every distance has appropriate coverage

**Phase 3: Full-Body Check**
1. Verify full-body atoms still load correctly
2. Test all three distances (close, medium, full_body)
3. Ensure no generation breaks

---

## FILES AFFECTED

1. `skirt_maximum_puff.json` - needs medium-specific variants
2. `dress_patterns.json` - dress.skirt_short_length_mandate needs medium counterpart
3. `couture_construction.json` - may need medium skirt construction atoms

---

## PATTERN TO WATCH

This same issue could affect OTHER slots where:
- ALL atoms are marked with same distance requirement
- Slot is called at a different distance
- Fallback loads inappropriate atoms

**Check these slots:**
- dress.petticoat (all full_body) - OK, slot probably skipped for medium
- accessories.footwear (all full_body) - should check if loading for medium
- accessories.hosiery (all full_body) - should check if loading for medium

---

**Next action:** Create medium-specific skirt atoms?
