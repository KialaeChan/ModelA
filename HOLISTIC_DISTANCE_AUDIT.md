# HOLISTIC DISTANCE AUDIT REPORT
**Date:** 2025-11-24
**Purpose:** Systematic check for distance-inappropriate content at medium camera distance

---

## INAPPROPRIATE CONTENT FOUND AT MEDIUM DISTANCE

### 1. PUPIL DILATION MEASUREMENTS ❌
**Location:** Expression and illness atoms
**Problem:** Pupil measurements (5-6mm, 6-7mm) at medium distance where eyes are too small
**Examples:**
- `expression.gaze_directed_beyond_camera`: "Pupils dilated 5-6mm" (set to medium!)
- `illness.dissociation_profound`: "Pupils wide - 6-7mm" (NO distance metadata!)
**Fix needed:** Move pupil measurements to close-only atoms

### 2. MOUTH/LIP MEASUREMENTS ❌
**Location:** Expression atoms
**Problem:** Precise mouth measurements at medium distance
**Example:**
- `expression.say_cheese_delirious`: "Mouth corners lifted 5-7mm" (close-only but check if others exist)
**Fix needed:** Remove mm measurements from medium-visible expressions

### 3. HAIR ACCESSORY SPECIFIC SIZES ⚠️
**Location:** Hair accessories
**Current:** "Wide satin ribbon (3-4cm)" at medium distance
**Issue:** Specific centimeter measurements for accessories barely visible at medium
**Fix needed:** Simplify to "wide ribbon" at medium, keep measurements for close only

### 4. NO DISTANCE METADATA (MAJOR ISSUE) ❌
**Many atoms lack distance metadata entirely:**
- Illness atoms (dissociation_profound with pupil measurements)
- Some hair accessories
- Various construction details
**Problem:** These load at ALL distances including full body!
**Fix needed:** Add distance metadata to all atoms with specific measurements

---

## SLOTS WITH DISTANCE FILTERING (WORKING)

✅ character.makeup_comprehensive (6 → 3)
✅ character.face (3 → 2) 
✅ expression.core (29 → 26)
✅ pose.stance (19 → 16)
✅ dress.pattern (25 → 22)
✅ dress.fabric (29 → 18)
✅ dress.embellishments (44 → 35)
✅ scene.room (5 → 3)
✅ style.checkpoints (5 → 4)

---

## SLOTS WITHOUT FILTERING (POTENTIAL ISSUES)

These slots show no distance filtering in logs:
- character.illness
- hair.accessories  
- hair.styling
- hair.core
- dress.construction (bodice, skirt, sleeves)
- dress.neckline
- accessories.hosiery (should be skipped at medium anyway)

---

## RECOMMENDATIONS

### IMMEDIATE FIXES NEEDED:

1. **Add distance metadata to illness atoms**
   - `illness.dissociation_profound` needs min_visible_distance: "close"
   - Any illness atom with measurements needs distance limits

2. **Fix expression distance settings**
   - `expression.gaze_directed_beyond_camera` set to medium but has pupil measurements
   - Need close-only version and medium version without measurements

3. **Create distance variants for detailed atoms**
   - Like we did for makeup: close version with measurements, medium without
   - Apply to: expressions, illness, hair accessories

4. **Add distance metadata to ALL atoms**
   - Every atom with mm/cm measurements should have min_visible_distance
   - Default to "close" for anything with precise measurements

### SYSTEMATIC APPROACH:

1. **Audit all definition files for measurements:**
   ```bash
   grep -h "mm\|cm" definitions/*.json | grep -v "min_visible_distance"
   ```

2. **Create distance variants where needed:**
   - Close: Full detail with measurements
   - Medium: General description without measurements  
   - Full body: Basic presence only

3. **Set conservative defaults:**
   - Any measurement under 10mm → close only
   - Any measurement 1-5cm → close or medium
   - Larger measurements → can be medium/full

---

## ESTIMATED TOKEN SAVINGS

If we properly filter micro-details:
- Expression measurements: ~50-100 tokens
- Illness details: ~50 tokens
- Hair accessory specifics: ~30 tokens
- Other micro-details: ~100+ tokens

**Potential savings: 200-300 tokens**

---

## PRIORITY ORDER

1. Fix illness atoms (no distance metadata at all) - CRITICAL
2. Fix expression atoms with wrong distance settings - HIGH
3. Add distance variants for detailed descriptions - MEDIUM
4. Audit all atoms for missing distance metadata - SYSTEMATIC

---

This audit reveals the same pattern as makeup: we're loading close-up detail at medium distance. The fix is the same: proper distance metadata and distance-appropriate variants.
