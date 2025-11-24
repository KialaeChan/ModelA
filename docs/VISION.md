# ModelA v2 - Vision Document

## Target Aesthetic

**Reference Image Quality:** Realistic digital rendering with dimensional form, clean technique, textured surfaces. Eastern digital art style with realism foundation.

### What This IS:
- ✅ Realistic digital rendering (like high-end 3D render meets 2D illustration)
- ✅ Dimensional form through accurate lighting and shadow
- ✅ Clean digital technique with precise execution
- ✅ Surface texture visible (skin pores, fabric weave, material properties)
- ✅ 2.5D aesthetic - realistic depth with illustration clarity
- ✅ Eastern digital art sensibility (wlop, artgerm, guweiz realistic work)
- ✅ Polished, refined, digitally precise

### What This is NOT:
- ❌ Anime/cel-shaded style
- ❌ Flat cartoon rendering
- ❌ Painterly brushwork aesthetic
- ❌ Simplified manga proportions
- ❌ Line art colored in

## Core Principles

### 1. Realism First
Every element must be grounded in realistic rendering:
- Skin has texture, subsurface scattering, dimensional form
- Fabric shows weight, drape physics, realistic light interaction
- Hair has strand structure and proper anisotropic highlights
- Materials behave according to their properties

### 2. Digital Clean
Clean digital technique, not rough or painterly:
- Precise edges on key forms
- Refined execution
- Polished finish
- Digital precision

### 3. Style Enforcement
Heavy, repeated enforcement of realism throughout prompt:
- Opening statement sets tone
- Reminders after each major section
- Negative prompts (NOT anime, NOT cel-shaded)
- Final reinforcement

## Token Distribution (3000 tokens)

**OLD system:**
- 40% anatomical jargon (useless)
- 20% technical camera specs (useless)
- 20% outfit detail
- 20% everything else

**NEW system:**
- 0% anatomical jargon (deleted)
- 30% style enforcement (realism anchors throughout)
- 30% outfit/couture detail (what we care about)
- 20% character emotion and expression
- 10% scene/environment
- 10% pose/body language

## Atom Categories

### DELETE ENTIRELY:
- rigging.* (all rigging atoms)
- anatomy.medical_terms.* (olecranon, malleoli, etc.)
- camera.lens_physics.* (barrel distortion specs, CA edges)
- All 3D modeling jargon

### KEEP & ENHANCE:
- Character identity (pink bob, blue eyes, pale skin, exhausted)
- Expression & emotion (performed cuteness, fatigue, compliance)
- Outfit construction (lattice, bows, petticoat, lace detail)
- Fabric behavior (drape, weight, compression)
- Scene basics (clinical room, grey floor, neutral walls)

### CREATE NEW:
- style.realism_foundation.* (enforcement atoms)
- style.digital_technique.* (clean rendering)
- style.not_anime.* (negative prompts)
- dress.construction_detail.* (couture specifics)
- fabric.physics_behavior.* (realistic drape)
- material.rendering.* (how surfaces catch light)

## Prompt Structure

### Opening (100 tokens)
Strong realism mandate with negatives:
```
Realistic digital rendering. 2.5D computer-generated art. Dimensional 
form through accurate lighting. Textured surfaces. Clean digital 
technique. Eastern digital art aesthetic. NOT anime, NOT cel-shaded, 
NOT flat rendering. Digital realism with illustration clarity.
```

### Character Core (400 tokens)
- Identity essentials
- Expression & emotion (heavy detail here - this works well)
- Basic pose
- Hair & makeup
- **+ Realism checkpoint**

### Outfit Detail (900 tokens)
- Silhouette & construction
- Bodice detail (lattice, bows, seams)
- Skirt construction (panels, trim, folds)
- Petticoat architecture
- Fabric behavior & physics
- Material rendering notes
- Color palette discipline
- **+ Realism checkpoint**

### Accessories (200 tokens)
- Hosiery (realistic sheer rendering)
- Footwear (material properties)

### Scene (300 tokens)
- Room geometry
- Lighting (accurate, dimensional)
- Camera angle basics
- **+ Realism checkpoint**

### Style Definition (700 tokens)
- Core identity statement
- Digital rendering technique
- Material behavior details
- Detail hierarchy
- Color & value control
- **Heavy negative prompts**
- Artist reference style
- Final enforcement

### Emotional Narrative (200 tokens)
- Story being told
- Tension between appearance and reality

### Buffer (200 tokens)
- Flexibility for variation

## Implementation Plan

### Phase 1: Atom Library Rebuild
1. Delete all anatomical jargon atoms
2. Delete all 3D rigging atoms
3. Create style enforcement atoms (~50 atoms)
4. Expand outfit construction atoms (~100 atoms)
5. Simplify pose atoms (keep emotional core)
6. Create fabric physics atoms (~30 atoms)

### Phase 2: Schema Restructure
1. Remove SKELETON_CORE layer (replace with CHARACTER_CORE)
2. Add STYLE_FOUNDATION layer (mandatory, first)
3. Expand COUTURE_DETAIL layer
4. Add RENDERING_TECHNIQUE layer (mandatory, late)
5. Simplify pose/expression layers
6. Set max_atoms conservatively (2-4 per slot)

### Phase 3: Generator Updates
1. Update preamble to realism statement
2. Ensure style atoms appear multiple times
3. Add realism checkpoints between sections
4. Test token count stays ~3000

### Phase 4: Testing
1. Generate 10 test prompts
2. Verify realism enforcement throughout
3. Check token distribution
4. Iterate on atom strength

## Success Criteria

A prompt passes quality check if:
1. Opens with strong realism mandate
2. "Realistic digital rendering" appears 3+ times
3. "NOT anime" or "NOT cel-shaded" appears 3+ times  
4. "Dimensional" / "textured" / "accurate" appear 10+ times
5. Zero anatomical jargon terms
6. Heavy outfit/fabric detail
7. Clean digital technique emphasized
8. Closes with final style enforcement
9. Token count 2800-3200
10. Generated images match reference quality

## Files to Create

```
ModelA_v2/
├── camera.py (rewritten generator)
├── config.json (updated categories)
├── layer_slot_schema.json (restructured)
├── definitions/
│   ├── style_enforcement.json (NEW)
│   ├── character_core.json (simplified)
│   ├── expression_emotion.json (keep detailed)
│   ├── couture_construction.json (expanded)
│   ├── fabric_physics.json (NEW)
│   ├── material_rendering.json (NEW)
│   ├── scene_lighting.json (simplified)
│   └── accessories.json (keep)
└── docs/
    └── VISION.md (this file)
```

## Next Steps

1. Get approval on vision
2. Rewrite atom definitions
3. Restructure schema
4. Update generator
5. Test and iterate
