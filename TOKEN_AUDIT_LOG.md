# Token Audit & Compliance Report
**Generated:** 2025-11-23T11:31:21.264063
**Tiktoken Available:** No (using math estimation)
**Total Atoms:** 551
**Total Tokens:** 22755
**Target Tokens:** 3000
**Budget Status:** 22755 vs 3000 (✗ 19755 over)

---
## Token Breakdown by File

| File | Atoms | Tokens | Avg/Atom | Avg Chars/Atom |
|------|-------|--------|----------|----------------|
| accessories_hosiery_shoes.json | 12 | 484 | 40.3 | 163 |
| advanced_tailoring.json | 18 | 302 | 16.8 | 68 |
| camera_angles_close.json | 8 | 623 | 77.9 | 313 |
| camera_relationship.json | 6 | 173 | 28.8 | 116 |
| character_age_safety.json | 5 | 238 | 47.6 | 192 |
| character_core.json | 23 | 1000 | 43.5 | 175 |
| composition_flaws.json | 12 | 430 | 35.8 | 144 |
| couture_construction.json | 57 | 3018 | 52.9 | 213 |
| dress_colors.json | 51 | 389 | 7.6 | 32 |
| dress_ensembles.json | 9 | 108 | 12.0 | 48 |
| dress_fabrics.json | 28 | 1170 | 41.8 | 169 |
| dress_patterns.json | 26 | 788 | 30.3 | 123 |
| expression_emotion.json | 33 | 1140 | 34.5 | 140 |
| hair_accessories.json | 38 | 2398 | 63.1 | 254 |
| hair_styling.json | 36 | 1281 | 35.6 | 144 |
| illness_manifestations.json | 16 | 513 | 32.1 | 129 |
| makeup_application.json | 44 | 3321 | 75.5 | 303 |
| petticoat_maximum_puff.json | 6 | 123 | 20.5 | 84 |
| pose_body_language.json | 30 | 837 | 27.9 | 113 |
| response_timing.json | 4 | 68 | 17.0 | 68 |
| scene_dissonance.json | 5 | 186 | 37.2 | 150 |
| scene_lighting.json | 9 | 349 | 38.8 | 157 |
| shiny_embellishments.json | 50 | 2415 | 48.3 | 195 |
| skirt_maximum_puff.json | 6 | 318 | 53.0 | 214 |
| style_enforcement.json | 19 | 1083 | 57.0 | 229 |

## Token Breakdown by Priority

**P0 (Mandatory):** 47 atoms, 2202 tokens
**P1 (Mandatory):** 368 atoms, 15918 tokens
**P2 (Mandatory):** 136 atoms, 4635 tokens

---
## Compliance Violations

### Rule 2 Violation: Characters over 300 (48 atoms)

- **camera_angles_close.camera.angle_overhead_closeup_amateur**: 622 chars (over by 322)
- **camera_angles_close.camera.angle_offcenter_amateur_closeup**: 837 chars (over by 537)
- **couture_construction.dress.neckline_peter_pan_lace**: 312 chars (over by 12)
- **couture_construction.dress.neckline_gathered_modest_mid**: 306 chars (over by 6)
- **couture_construction.dress.neckline_high_square**: 326 chars (over by 26)
- **couture_construction.dress.neckline_round_gathered**: 339 chars (over by 39)
- **couture_construction.dress.neckline_empire_ruffled**: 335 chars (over by 35)
- **couture_construction.dress.neckline_ribbon_tie_front**: 332 chars (over by 32)
- **couture_construction.dress.neckline_puffed_collar**: 308 chars (over by 8)
- **couture_construction.dress.neckline_rosette_accent**: 317 chars (over by 17)
... and 38 more

### Rule 1 Violation: Narrative Language (8 atoms)

- **hair_accessories.hair.primary.theatrical_bow_palace** (keyword: 'layered'): PRIMARY HAIR EMBELLISHMENT VISIBLE FROM OVERHEAD. Construction at crown/top of h...
- **hair_styling.hair.style.twisted_crown_elaborate** (keyword: 'layered'): 6-8 small sections twisted individually and pinned to create dimensional crown a...
- **pose_body_language.pose.post_session_context** (keyword: 'after'): Subject is young adult aged 20-24. After extensive preparation. fatigue but obli...
- **response_timing.timing.facial_strain_close** (keyword: 'showing'): Facial strain evident. Jaw tension visible. Eyes showing effort....
- **scene_dissonance.dissonance.pose_strain_visible** (keyword: 'showing'): Body maintains pose while showing visible strain. Pose held but visibly strained...
- **scene_lighting.scene.salon_details** (keyword: 'showing'): Room details showing laboratory facility. Equipment at depths - treatment chairs...
- **scene_lighting.scene.environment_rendering** (keyword: 'showing'): Digital environment with spatial depth showing cold sterile grey space. Dimensio...
- **style_enforcement.style.fabric_rendering** (keyword: 'showing'): Fabric rendered showing material weight and drape. Bright white-blue overhead li...

### Rule 3 Violation: Negative Language (32 atoms)

- **camera_angles_close.camera.angle_overhead_closeup_amateur** (keyword: 'NOT'): PROFESSIONAL MAKEUP DOCUMENTATION DISTANCE. Beauty shot for portfolio. Cosmetics...
- **camera_angles_close.camera.angle_offcenter_amateur_closeup** (keyword: 'NOT'): PROFESSIONAL MAKEUP DOCUMENTATION DISTANCE. Beauty shot for portfolio. Cosmetics...
- **character_age_safety.character.adult_proportions_face_close** (keyword: 'not'): Eyes noticeably smaller relative to head (adult anime style). Almond-shaped, nar...
- **character_age_safety.character.adult_eye_proportion** (keyword: 'not'): Eyes noticeably smaller relative to head (adult anime style). Almond-shaped, nar...
- **character_core.character.cool_undertone** (keyword: 'not'): Cool-neutral pale skin with soft blush undertones. Photorealistic rendering. Sat...
- **character_core.character.cool_undertone_close** (keyword: 'not'): Cool-neutral pale skin with soft blush undertones. Photorealistic rendering. Sat...
- **composition_flaws.composition.environmental_clutter** (keyword: 'avoid'): Background equipment positioned awkwardly - jutting from subject or distracting ...
- **couture_construction.dress.neckline_ribbon_tie_front** (keyword: 'not'): NECKLINE VISIBLE FROM OVERHEAD. Neckline forms boundary at perimeter where frame...
- **expression_emotion.expression.mouth_parted** (keyword: 'not'): Lips separated 3-5mm. Jaw muscles relaxed. Upper and lower teeth not visible. Ey...
- **expression_emotion.expression.eyes_unfocused** (keyword: 'not'): Pupils not converging on any point. Eyes open but seeing nothing. Gaze empty and...
... and 22 more

### Content Filter Risk: Sensitive Language (4 atoms)

- **expression_emotion.expression.performed_cuteness** (keyword: 'trained')
  Suggestion: Replace 'trained' with alternative (e.g., 'obliging' for 'complying')
  Context: Smile present but strained. Visible fatigue. Heavy eyelids slightly closed. Expr...

- **expression_emotion.expression.fatigued_overall_fullbody** (keyword: 'trained')
  Suggestion: Replace 'trained' with alternative (e.g., 'obliging' for 'complying')
  Context: Subject fatigued with diminished energy. Overall composed but strained appearanc...

- **scene_dissonance.dissonance.pose_strain_visible** (keyword: 'trained')
  Suggestion: Replace 'trained' with alternative (e.g., 'obliging' for 'complying')
  Context: Body maintains pose while showing visible strain. Pose held but visibly strained...

- **style_enforcement.style.core_unified** (keyword: 'trained')
  Suggestion: Replace 'trained' with alternative (e.g., 'obliging' for 'complying')
  Context: Manga painter technique under harsh bright overhead LED light. Bright white-blue...


---
## Summary

- Character limit violations: 48
- Narrative language violations: 8
- Negative language violations: 32
- Filter risk violations: 4
- **Total violations: 92
