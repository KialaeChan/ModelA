# DISTANCE-SLOT HOLISTICS AUDIT
**Date:** December 1, 2025
**Critical Issue:** Slots loading regardless of camera distance
**Impact:** DALL-E sees descriptions of invisible elements (feet in close-ups)

---

## EXECUTIVE SUMMARY

**Problem:** Hosiery and footwear slots load for ALL camera distances, including close-ups where feet aren't visible. This confuses DALL-E and wastes tokens describing things outside the frame.

**Root Cause:** These slots aren't being passed through distance filtering in build_prompt()

**Impact:**
- DALL-E gets conflicting instructions ("face only" + "ankle socks visible")
- Wasted tokens on invisible elements
- May contribute to DALL-E ignoring tight crop instructions

---

## SLOT-BY-SLOT AUDIT

### ✅ SLOTS CURRENTLY BEING DISTANCE-FILTERED

**character.makeup_detail:**
- Close: 27 → 2 atoms (makeup visible, detailed)
- Medium: 27 → moderate atoms
- Full-body: 27 → 2 atoms (minimal detail)
- **Status:** WORKING CORRECTLY

**expression.core:**
- Close: 33 → 3 atoms (detailed facial expressions)
- Medium: 33 → moderate
- Full-body: 33 → 3 atoms (overall expression only)
- **Status:** WORKING CORRECTLY

**pose.stance:**
- Close: 22 → 2 atoms (upper body positioning)
- Medium: 22 → moderate
- Full-body: 22 → 2 atoms (full stance visible)
- **Status:** WORKING CORRECTLY

**dress.pattern:**
- Close: 25 → 3 atoms (fine details not visible)
- Full-body: 25 → 3 atoms (pattern readable)
- **Status:** WORKING CORRECTLY

**dress.skirt:**
- Close: Minimal (skirt mostly out of frame)
- Full-body: Full detail
- **Status:** WORKING CORRECTLY

**dress.fabric:**
- Close: 29 → 14 atoms (less fabric visible)
- Full-body: 29 → 14 atoms (full fabric visible)
- **Status:** WORKING CORRECTLY

**dress.details:**
- Close: 20 → 18 atoms (bodice details visible)
- Full-body: 20 → 18 atoms (all details)
- **Status:** WORKING CORRECTLY

**dress.embellishments:**
- Close: 50 → 31 atoms (upper embellishments only)
- Full-body: 50 → 31 atoms (all embellishments)
- **Status:** WORKING CORRECTLY

---

### ❌ SLOTS **NOT** BEING DISTANCE-FILTERED

**accessories.hosiery:**
- Current behavior: ALWAYS loads 1 atom regardless of distance
- Problem: Loads for close-ups where feet aren't visible
- Example violation: "Pastel pink ankle socks..." in face-only shot
- **Status:** BROKEN - needs distance filtering

**accessories.footwear:**
- Current behavior: ALWAYS loads 1 atom regardless of distance  
- Problem: Loads for close-ups where feet aren't visible
- Example violation: "Black patent leather shoes..." in chest-up shot
- **Status:** BROKEN - needs distance filtering

**hair.accessories:**
- Current behavior: Loads regardless of distance
- Question: Should this be filtered? Hair visible in all shots except extreme close-ups
- **Status:** UNCERTAIN - may be correct, needs review

---

## CORRECT BEHAVIOR MATRIX

| Slot | Close (3-5ft) | Medium (5-7ft) | Full-Body (6-8+ft) |
|------|---------------|----------------|-------------------|
| **Makeup** | ✅ Detailed | ✅ Moderate | ✅ Minimal |
| **Expression** | ✅ Detailed | ✅ Moderate | ✅ Overall only |
| **Hair** | ✅ Full detail | ✅ Full detail | ✅ Full detail |
| **Hair Accessories** | ✅ Load | ✅ Load | ✅ Load |
| **Neckline** | ✅ Detailed | ✅ Detailed | ✅ Visible |
| **Bodice** | ✅ Upper only | ✅ Full detail | ✅ Full detail |
| **Sleeves** | ✅ Visible | ✅ Full detail | ✅ Full detail |
| **Skirt** | ❌ DON'T LOAD | ⚠️ Minimal mention | ✅ Full detail |
| **Hosiery** | ❌ DON'T LOAD | ❌ DON'T LOAD | ✅ Load |
| **Footwear** | ❌ DON'T LOAD | ❌ DON'T LOAD | ✅ Load |
| **Petticoat** | ❌ DON'T LOAD | ⚠️ If visible | ✅ Full detail |
| **Hem embellishments** | ❌ DON'T LOAD | ❌ DON'T LOAD | ✅ Load |

---

## CODE FIX REQUIRED

**Location:** camera.py, build_prompt() function

**Current problem:** Hosiery/footwear slots called unconditionally

**Solution:** Add distance check before calling these slots:

```python
# Only load hosiery/footwear for full-body shots
if camera_distance == 'full_body':
    # accessories.hosiery slot
    # accessories.footwear slot
```

**Verification:** After fix, close-up prompts should NOT contain hosiery/footwear atoms

---

## ADDITIONAL FINDINGS

### Issue: Camera Angle Atom Too Long
- camera.angle_chest_up_close: 132 tokens (over 100 token threshold)
- Cause: Nuclear close-up language is very verbose
- Solution: Once we determine optimal close-up language, trim to essentials

### Issue: Skirt Embellishments in Close-Ups
- Some skirt embellishments may load for close shots
- Need to verify hem-level embellishments have proper distance metadata
- Check: Do D1_Architectural atoms at hem have min_visible_distance="full_body"?

### Issue: Petticoat Descriptions
- Petticoat system describes volume projection
- In close-ups, this is irrelevant (not visible)
- May need conditional loading or distance variants

---

## TESTING PROTOCOL

**After fixes applied:**

1. Generate close-up prompt (3ft camera)
   - ✅ Should NOT contain hosiery atoms
   - ✅ Should NOT contain footwear atoms
   - ✅ Should NOT contain hem embellishments
   - ✅ Should contain: hair, makeup, expression, neckline, upper bodice

2. Generate medium prompt (5-6ft camera)
   - ✅ Should NOT contain hosiery atoms
   - ✅ Should NOT contain footwear atoms
   - ✅ Should contain: hair, makeup, bodice, upper skirt (minimal)

3. Generate full-body prompt (6-8ft camera)
   - ✅ Should contain ALL elements including hosiery/footwear

4. DALL-E image test
   - Does removal of feet descriptions help DALL-E respect tight crops?
   - Theory: Less conflicting info = better compliance

---

## RULE 41 DOCUMENTATION REQUIREMENTS

**Bug discovered:** Hosiery/footwear slots not being distance-filtered
**Root cause:** Slots called unconditionally in build_prompt()
**Solution:** Add distance check before loading these slots
**Document in:** BUGS_AND_SOLUTIONS.md

**Workflow improvement:** Created distance-slot matrix for reference
**Document in:** WORKFLOW.md - add "Distance-Appropriate Slot Loading" section

**Architecture change:** Distance filtering needs to gate slot loading, not just atom selection
**Document in:** WORKFLOW.md - update distance filtering documentation

---

## PRIORITY ORDER

**IMMEDIATE (Critical):**
1. Fix hosiery/footwear conditional loading in camera.py
2. Test close-up generation (verify feet descriptions gone)
3. Test DALL-E with cleaned prompt

**HIGH (Important):**
1. Audit all embellishment atoms for proper distance metadata
2. Check petticoat system distance behavior
3. Verify skirt slot filtering working correctly

**MEDIUM (Enhancement):**
1. Trim camera.angle_chest_up_close atom (132 → <100 tokens)
2. Create distance-appropriate variants for petticoat if needed
3. Document final distance-slot matrix in WORKFLOW.md

---

**This audit identifies the critical holistics issue: describing elements outside the frame confuses DALL-E and wastes tokens.**

**Fix: Conditional slot loading based on camera distance.**

---
