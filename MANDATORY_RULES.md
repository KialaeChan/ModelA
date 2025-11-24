# MANDATORY RULES FOR MODELА WORK - CONSOLIDATED EDITION

**Follow these every time. No exceptions.**

---

## RULE 1: ATOM WRITING FUNDAMENTALS
- **SURFACE-LEVEL FACTS ONLY:** Describe only what is physically visible in rendered image. No interpretation, emotion, implication, process, or backstory.
- **REMOVE IMMEDIATELY:**
  - Narrative: "shows," "creates," "demonstrates," "reads as," "appears," "seems," "suggests," "looks like," "could be," "reminds of"
  - Time references: "hours of," "after preparation," "recently"
  - Process: "applied with," "hand-sewn," "buffed," "layered," "stitched"
  - Interpretive: "professional," "precise," "elaborate," "careful," "masterfully"
  - Evocative: "grim," "haunting," "poignant," "tragic," "beautiful," "precious," "resigned," "withdrawn," "vacant," "exhausted," "trained," "broken," "conditioned"
- **KEEP - Observable facts:**
  - Measurements: "5mm," "45°," "20-30%"
  - Positioning: "left," "right," "tilted," "angled," "upper," "lower"
  - Visual properties: "glossy," "matte," "translucent," "reflective"
  - Color: Specific names only, no emotional modifier
  - Physical state: "trembling," "glistening," "dripping"
  - Anatomy: Specific names if factual
- **CHARACTER LIMITS (HARD):**
  - P0 Mandate: 300 chars max
  - P1 Core: 250 chars max
  - P2 Detail: 150-200 chars ideal
  - If exceeds: split into 2 atoms, don't compress
- **NO REDUNDANCY:** One concept per atom. "Shimmer" once, not "shimmer/sparkle/glint/shine"
- **TEST:** Would a camera capture this? If "maybe," remove it.
- **DESCRIBE ART, NOT SPECIFICATIONS:**
  - AI generators respond to visual description, not technical counts
  - ❌ "180-220 crystals at 6-10mm intervals with 3 attachment points"
  - ✅ "Dense river of graduated crystals flowing from shoulder to waist"
  - Focus: What does it LOOK like? What's the visual impact?
  - Bespoke quality signals: "hand-placed," "graduated flow," "precision spacing," "atelier-quality," "individually secured"
  - Not through: stitch counts, exact measurements, labor hours, attachment methods
  - Exception: Scale indicators (like "TOO LARGE for complete framing") work because they're relative visual cues

---

## RULE 2: NEGATIVE & FILTER-SAFE LANGUAGE
- **NO negative language in standard atoms:**
  - ❌ "NOT X," "AVOID X," "NEVER X"
  - ⚠️ EXCEPTION: style_enforcement.json can block common defaults only
- **BANNED WORDS:**
  - ❌ "scattered" - use "stencil-printed", "in rows", "allover repeat", "placed throughout" instead
  - ❌ "tears/tear" (except crystal teardrops) - causes crying appearance
  - ❌ "moisture/moist" on face - causes sweating appearance
  - ❌ "wet" for eyes/face - use "reflective", "glassy", "polished" instead
  - ❌ "sweating/sweat" - obvious
- **CONTENT FILTER SAFE REPLACEMENTS (required):**
  - "complying" → "obliging"
  - "exhausted/exhaustion" → "fatigued/fatigue"
  - "vacant" → "unfocused"
  - "trained" → "practiced"
  - "resigned" → "composed"
  - "withdrawn" → "reserved"
  - "obedient" → "cooperative"
  - "conditioned" → "prepared"
  - "broken" → "diminished"
  - Tool: `python fix_filter_language.py --apply`

---

## RULE 3: TOKEN BUDGET & TRACKING
- **Target:** 3000 tokens
- **Acceptable range:** 2800-3200 tokens
- **Baseline protocol:** Run `python camera.py` 5 times, calculate average
- **Action triggers:**
  - Average > 3300: Reduce P2 max_atoms first
  - Average < 2900: Verify mandate atoms loading
  - > 3400: Trim 10% across 4+ files (not 40% from 1 file)
- **Tracking tool:** `python token_audit.py` → TOKEN_AUDIT_LOG.md
- **Current status:** 3,368 tokens (acceptable)

---

## RULE 4: SYSTEM INTEGRITY CHECKS (BEFORE DELIVERY)
- ✅ Code runs without errors
- ✅ All atoms load and generate
- ✅ Mandate checkpoint PASS
- ✅ Zero negative language violations
- ✅ Zero narrative language violations
- ✅ All P0 atoms present
- **Before shipping:** Run `python camera.py`, verify all pass. If any fail: FIX, don't ship.

---

## RULE 5: DELIVERY PROTOCOL
- Direct, brief communication focused on what changed
- ALWAYS zip: `ModelA.zip` to `/mnt/user-data/outputs/`
- Format: `[View your project](computer:///mnt/user-data/outputs/ModelA.zip)`
- No flowery language, ASCII art, or excessive summary boxes
- No need to verify/retest before delivery - trust the work
- Keep delivery message concise: one sentence summary if needed, then the link
- EXAMPLE: "Fixed 3 atoms, removed 12 negatives, zipped. Ready." OR just link without preamble

---

## RULE 6: SESSION STARTUP PROTOCOL (MANDATORY)
- **FIRST:** Read Rules 1-5
- **SECOND:** Run `python token_audit.py` (check violations)
- **THIRD:** Run `python camera.py` (verify baseline)
- **FOURTH:** Check `_INTERNAL_PROJECT_STATE.md` for context
- **FIFTH:** Review `SESSION_LOG_*.md` from last session
- **Never skip.** Clean baseline = clean session.

---

## RULE 7: COMPLIANCE AUDIT WORKFLOW (BEFORE SHIPPING)
- **Run:** `python token_audit.py` → TOKEN_AUDIT_LOG.md
- **Check violations:**
  - Over 300 chars: Fix per Rule 1
  - Narrative language: Remove per Rule 1
  - Negative language: Remove per Rule 2
  - Filter risk language: Replace per Rule 2
- **Zero violations required before ship.**

---

## RULE 8: TOKEN AUDIT TOOL USAGE
- **Tool:** `python token_audit.py`
- **Output:** TOKEN_AUDIT_LOG.md with:
  - Per-file breakdown
  - Per-priority breakdown (P0/P1/P2)
  - All violations flagged with line numbers
  - Atom-by-atom analysis
- **How to read:**
  - Focus on "Violations Found" section
  - Each violation shows atom ID and context
  - Top token-heavy files = trim opportunities
- **When:** Session start, before ship

---

## RULE 9: CONTENT FILTER LANGUAGE FIX TOOL
- **Tool:** `python fix_filter_language.py`
- **Preview:** `python fix_filter_language.py` (dry-run)
- **Apply:** `python fix_filter_language.py --apply`
- **Replacements:** Auto per Rule 2
- **Safety:** Idempotent, safe to run multiple times
- **When:** After token audit finds filter risk violations

---

## RULE 10: MANDATORY ATOMS ARE PROTECTED
- P0 Mandate atoms in layer_slot_schema.json cannot be deleted or significantly changed without asking first
- **Always present:**
  - Age Safety (Early): 2 atoms
  - Age Safety (Late): 2 atoms
  - Dissonance: 2+ atoms
  - Style Foundation: 5 atoms
- **Verify after modifications:** Run `python camera.py`, check mandate checkpoint PASS
- **Before deletion of any P0 atom:** Ask first

---

## RULE 11: SCHEMA CHANGES (HANDLE WITH CARE)
- layer_slot_schema.json is the architecture
- Changes affect entire system
- **Test immediately after:** Run `python camera.py`, verify all slots still pull
- **Before modifications:** Know what you're changing and why
- **If unsure:** Ask first

---

## RULE 12: RANDOMIZATION IS CORE DESIGN
- All couture, expression, pose, hair, and detail atoms should have `"random": true`
- Only lock atoms (`"random": false`) if they are:
  - P0 MANDATE atoms (core identity elements)
  - Foundational style atoms (color palette, age safety, dissonance)
- Detail/embellishment/variation atoms should ALWAYS be randomized
- Variety across generations is a feature, not a bug
- Each time camera.py runs, expect different: necklines, patterns, colors, sleeves, poses, expressions, embellishments
- **NEVER lock variation atoms without asking first**
- Theme-locked slots pull theme-specific atoms first
- Should find 3-20 atoms per selected theme
- If theme atoms weak: fix definitions, don't work around
- **Test after modifications:** Run `python camera.py`, verify theme atoms in output

---

## RULE 13: DISSONANCE IS SACRED
- Central vision: Perfect dress + fatigued body + clinical space
- All dissonance atoms must remain and load together
- Do NOT delete or substantially modify without asking
- **Verify after changes:** Run `python camera.py`, check both dissonance atoms in checkpoint

---

## RULE 14: AGE & STYLE FOUNDATION (NON-NEGOTIABLE)
- **Age (locked):**
  - 20-24 years old ALWAYS
  - Adult proportions (6.5-7 heads tall)
  - Mature facial structure (defined mandible, cheekbones)
  - Small almond eyes (adult anime style, not large/round)
  - Early AND late checkpoints required, both must PASS
- **Style (locked):**
  - 2.5D painted illustration (NOT photorealism, NOT pure anime)
  - Manga artist sensibility (explicit artist references)
  - Harsh institutional lighting (NOT soft/flattering)
  - Dimensional form through value contrast
  - Clinical institutional aesthetic throughout
- **Test:** Run `python camera.py`, verify age & style checkpoints PASS

---

## RULE 15: ATOM NAMING & ORGANIZATION
- Consistent prefixes within files (e.g., "dissonance.", "pose.")
- Names describe RESULT, not process
  - Good: "rosettes_gathered"
  - Bad: "hand_rolled_rosettes"
- One concept per atom - don't combine unrelated ideas
- If 2 ideas: 2 atoms. If doesn't fit: 0 atoms.
- Naming enables quick categorization

---

## RULE 16: ATOM FILE HYGIENE
- definitions/ contains ONLY active .json files (no backups, _old, versions)
- If major version: create `YYYY_MM_DD_backup.json`, delete when confirmed working
- Before shipping: verify schema references only existing files
- Clutter causes confusion and token waste
- Clean directory = faster development

---

## RULE 17: BACKUP & EXPERIMENTAL SAFETY
- Backups are optional, keep minimal (one if major changes)
- Remove backup immediately when working confirmed
- Do NOT commit experimental files to zip
- Before zipping: verify all atoms load clean

---

## RULE 18: PREAMBLE IS FOUNDATIONAL
- The hardcoded preamble in camera.py (lines ~32) sets aesthetic direction BEFORE atoms load
- Preamble can override or contradict downstream atoms if misaligned
- Changes to core aesthetic direction MUST update preamble first
- **Alignment rule:** Preamble must match atom language
  - If atoms say "2.5D illustration" → preamble must match
  - If atoms say "manga style" → preamble must support
  - If atoms specify lighting → preamble must reflect
- Review preamble before every major aesthetic shift

---

## RULE 19: THEME EMBELLISHMENT FILTERING
- Ensemble embellishment_focus keywords filter candidates (camera.py lines 125-145)
- P0 mandate atoms (like sparkle) MUST load regardless of ensemble preference
- **Fix logic:** Extract P0 atoms → filter by theme → add P0 back
- This ensures mandates always load plus theme preferences
- Check this logic if embellishments vary randomly between runs
- P0 atoms = mandatory; ensemble preferences = preferences

---

## RULE 20: DISSONANCE VISUAL OUTCOME LANGUAGE
- Dissonance atoms should describe HOW the conflict LOOKS in the image
- Include language describing visual RESULT, not just conflict statement
- Example: Instead of "dress vs environment" → "Vivid cool dress luminously stands out against drab grey; visual pop through saturation contrast"
- Dissonance should manifest as visual POP
- Each dissonance atom should answer: "What does this conflict LOOK like?"

---

## RULE 21: COLOR PALETTE DECISIONS (LOCKED EARLY)
- Saturation level must be locked decision BEFORE atoms are written
- Binary choice: "Saturated and vibrant" vs "Muted and desaturated"
- Document in AESTHETIC_TARGET.md as explicit locked decision
- Prevents mid-project drift (some atoms assume desaturation, others assume vibrancy)
- Color palette is foundational - test early
- **Test protocol after palette changes:**
  1. Run `python camera.py` to verify atoms load
  2. Generate ONE test image with new palette
  3. Document result in STYLE_TEST_LOG.md
  4. Decide: lock this or revert
- Don't write 20 atoms then discover color strategy doesn't work

---

## RULE 22: LIGHTING LANGUAGE MUST BE EXPLICIT
- "Institutional lighting" alone is ambiguous (warm? cool? green? blue?)
- Always specify color temperature explicitly
- Examples:
  - "White institutional" (not greenish)
  - "Blue-white institutional (7000-8000K clinical blue-white)"
  - "White clinical color temperature (not greenish, not yellowish)"
- Override generator defaults in atoms
- Color temperature language is as critical as light quality

---

## RULE 23: 2.5D IS THE CRITICAL ANCHOR
- 2.5D painted illustration is core aesthetic (prevents both photorealism AND pure animation)
- Language must explicitly state "2.5D" or "2.5D painted illustration" in preamble/core atoms
- Avoid drift toward:
  - "3D digital rendering" (triggers photorealism)
  - "CG" or "Semi-realistic" (uncanny valley)
  - "Pure animation" or "anime style" alone (loses dimensional form)
- Always reference artist style in atoms: "Inoue Takehiko rendering" or specific manga artists
- **Test 2.5D direction immediately** - if preamble is wrong, entire aesthetic fails

---

## RULE 24: SHADOW LANGUAGE REQUIRES GRADIENT SPECIFICATION
- Shadow depth matters for mood: "heavy gradients" vs "pitch black" vs "soft transitions"
- Heavy gradients = dimensional, dramatic, painted feel
- Pitch black = harsh, graphic, potentially too severe
- Soft transitions = illustration becomes too soft/photorealistic
- Always specify gradient behavior when setting shadow depth
- Default assumption: "heavy gradients with dimensional modeling" unless specified
- Test shadow language immediately after changes
- Heavy gradient shadows + institutional lighting = dramatic 2.5D aesthetic

---

## RULE 25: 3D EMBELLISHMENTS VS PRINT PATTERNS
- Prints (patterns, scattered small motifs) read as costume/childish/clown-like
- Applied 3D embellishments (sewn-on bows, appliqués, beads) read as couture/elegant
- For elegant ensembles: emphasize size (2-4cm), placement (clusters, strategic), application (3D sewn)
- For childish looks: emphasize size (10-12mm), distribution (scattered), execution (printed)
- When theme requires embellishments, specify "3D applied" not "printed pattern"
- Language matters: "Ribbon bows applied across bodice as 3D embellishments" vs "Small bow shapes printed across"

---

## RULE 26: EMBELLISHMENT SLOT MAX_ATOMS MUST ALLOW MANDATES
- P0 MANDATE atoms (like dense sparkle) should NEVER be filtered out by ensemble preferences
- If max_atoms: 1, only ONE embellishment loads - may not be mandate
- Set max_atoms high enough (3+) to allow: P0 mandate + theme-specific + detail atoms
- Always preserve P0 atoms in ensemble filtering logic
- Sparkle/shine mandates MUST load with every prompt, plus theme-specific layered on top
- Test: Run 5 generations, verify P0 atoms appear in every prompt

---

## RULE 27: STYLE DIRECTION MUST BE TESTED EARLY
- Before spending hours iterating on atom language, generate ONE test image
- Document what generator produces vs. what was intended
- Catches fundamental mismatches (photorealism vs. animation vs. illustration) immediately
- Prevents 3+ iteration loops on abstract language that doesn't work
- **After major style shifts:** Run `python camera.py` AND generate test image same day
- **Document in:** STYLE_TEST_LOG.md (track all style tests)

---

## RULE 28: INCLUDE ARTIST REFERENCES IN ATOMS
- Instead of abstract language like "bold linework," name the actual visual reference
- Generators respond better to concrete artist references than descriptive language
- Examples: "Kentaro Miura (Berserk) illustration style" or "Inoue Takehiko (Vagabond) aesthetic"
- Prevents photorealism default bias by making style intent explicit
- **Implementation:** Add artist names to style_enforcement atoms
- Good: "Heavy illustrated linework in Miura (Berserk) style with blended shading"
- Bad: "Bold linework with dimensional form"

---

## RULE 29: AESTHETIC INTENT SEPARATE FROM ATOMS
- Create/maintain file: `AESTHETIC_TARGET.md` that states clearly:
  - What visual style is intended (e.g., "high-end manga illustration, not photorealistic CG")
  - What should NOT appear (e.g., "avoid soft flattering light")
  - Reference images or artists (visual anchors)
  - Key visual qualities needed (e.g., "stark institutional contrast")
- Update BEFORE ANY style iteration
- Use as ground truth when atoms drift
- Prevents aesthetic drift between sessions

---

## RULE 30: PROFESSIONAL FACILITY ≠ WARM FACILITY
- State-of-the-art, expensive, pristine, modern = cold institutional materials (polished tile, stainless steel, grey)
- Avoid language that softens facility: "cheap," "utilitarian," "worn," "basic"
- Use instead: "polished high-end," "pristine state-of-the-art," "expensive institutional"
- Professional/high-end facilities are STERILE and COLD - that's the architectural point
- Don't soften setting to make "nicer"; make it expensive and emotionally cold
- Rich facilities can be grim; that's often MORE dissonant than poor ones

---

## RULE 31: VISUAL OUTCOME BEFORE ATOM LANGUAGE
- When setting lighting/shadows/style, describe what image should LOOK like
- **Good:** "Heavy shadow gradients under eyes, across cheekbones creating dimensional sculpting"
- **Bad:** "Harsh institutional lighting"
- Generators respond better to: "shadows reveal fatigue" than "harsh light"
- Focus on RESULT not CAUSE: describe what's visible, not just light direction
- Always ask before writing atoms: "What will this LOOK like in the final image?"

---

## RULE 32: CLEAN JUNK BEFORE EVERY ZIP
- Every time before zipping for delivery, delete junk:
  - `__pycache__/` folder and `.pyc` files
  - `.backup_*` files
  - `*.orig` files
  - Temporary test files
  - Old debug scripts
- **Checklist before ZIP:**
  - [ ] No `__pycache__` directory
  - [ ] No `.pyc` files
  - [ ] No `.backup` files
  - [ ] No `.orig` files
  - [ ] No temporary test files
  - [ ] definitions/ contains ONLY `.json`
  - [ ] docs/ contains ONLY `.md`
- Clean directory = cleaner deliverables, faster iteration

---

## RULE 33: NO UNICODE IN ATOMS
- Atom contents must be ASCII-only
- **Remove all:**
  - °, ±, × (use "degrees," "plus-minus," "by")
  - —, –, • (use standard hyphens)
  - Emojis
  - Accented characters (é, ñ, ü)
  - Curly quotes (" " ' ') - use straight quotes
- **Keep:** Standard ASCII letters, numbers, punctuation, spaces
- **Check before delivery:** `grep -r "\\u[0-9A-Fa-f]" definitions/`
- **Test:** Run `python camera.py`, verify no encoding errors
- Encoding issues cause generation failures

---

## RULE 34: NONBINARY IDENTITY (LOCKED)
- AMAB, 20-24 years old, adult appearance
- No gendered pronouns: "they/them" ONLY
- ❌ Never: "she/her," "woman," "girl," "female"
- ✅ Present as androgynous-cute with feminine styling
- Adult face + slight fragile silhouette
- Nonbinary identity with feminine presentation

---

## FINAL PROTOCOL: EVERY SESSION

**RECEIVING THE PROJECT (First thing - Rule 37):**
1. Extract ZIP, verify files present (Step 1)
2. Read context: _INTERNAL_PROJECT_STATE.md + recent SESSION_LOG (Step 2)
3. Run: `python camera.py` (Step 3)
4. Read: ALL analytics output + VIOLATION_DETAIL_REPORT.md (Step 4)
5. Understand: What's broken, what needs fixing, which atoms responsible (Step 5)
6. Plan: Formulate fix strategy before editing (Step 6)
7. Report: Present findings to Emily before starting edits (Step 7)

**DOING FOCUSED WORK:**
1. Prove you read: State Rule 38 back to Emily
2. Read Rules 1-5 (fundamentals)
3. Execute planned edits based on analytics
4. Edit only identified atoms per violation report
5. Do focused work (Rules 10-34)

**BEFORE DELIVERY:**
1. Run pre-delivery checks (Rule 4)
2. Run: `python camera.py` one final time
3. Verify: VIOLATION_DETAIL_REPORT.md shows 0 violations
4. Verify: Mandate checkpoint PASS
5. **DOCUMENTATION UPDATES (check each):**
   - 5a. Update _INTERNAL_PROJECT_STATE.md with next critical task (if multi-phase work)
   - 5b. Update BUGS_AND_SOLUTIONS.md if discovered new bug patterns this session
   - 5c. Update WORKFLOW.md if found workflow improvements or new patterns
   - 5d. Update MANDATORY_RULES.md if identified rule gaps or better practices
6. **CHECK CLIENT-SIDE INSTRUCTIONS (userPreferences):** Verify all workflow mandates completed
7. **RULE 41 GATE-CHECK:** Complete documentation completeness check (see Rule 41)
8. Clean junk (Rule 32)
9. Zip and send (Rule 5)

**Stop. Do not add extra steps, reports, or features.**

---

## RULE 35: CONTINUOUS RULE IMPROVEMENT (MANDATORY GATE-CHECK)
- **After every edit session, before delivery, you MUST complete this forcing function:**

**GATE-CHECK QUESTION:** "This session I learned: [X]. I should update [FILENAME] to prevent future [Y]."

**If you learned new bug patterns:**
- Complete: "This session I learned: [bug pattern]. I should update BUGS_AND_SOLUTIONS.md to prevent future [problem]."
- Then actually update BUGS_AND_SOLUTIONS.md before zipping

**If you discovered workflow improvements:**
- Complete: "This session I learned: [better approach]. I should update WORKFLOW.md to prevent future [inefficiency]."
- Then actually update WORKFLOW.md before zipping

**If you identified rule gaps:**
- Complete: "This session I learned: [what rules didn't cover]. I should update MANDATORY_RULES.md to prevent future [mistakes]."
- Then actually update MANDATORY_RULES.md before zipping

**If you genuinely learned nothing new this session:**
- You're lying to yourself. Every session reveals something about what works or what breaks.
- At minimum, document what you verified still works correctly.

**Examples of what counts as "learning":**
- Found a pattern in violations? Add rule preventing it
- Discovered better language? Update guidance
- Realized workflow was inefficient? Add steps to protocol
- Hit an edge case? Document the solution
- Fixed a bug? Document root cause and fix
- Had to ask Emily for clarification? Document the answer

**This is not optional. This keeps the rules living and evolving with the project.**
- This keeps the rules living document that evolves with the project

---

---

## RULE 37: RECEIVING PROJECT PACKAGE - ANALYSIS PROTOCOL (NON-NEGOTIABLE)

**WHEN YOU RECEIVE THE ZIP (from Emily or from outputs/):**

**STEP 1: EXTRACT AND VERIFY (5 min)**
- Extract ModelA.zip to working directory
- Verify: `camera.py`, `analytics.py`, `violation_reporter.py` all present
- Verify: `definitions/` directory exists with JSON files
- Verify: `layer_slot_schema.json` and `config.json` present

**STEP 2: READ RECENT CONTEXT (10 min) - THIS IS MANDATORY**
- Read `_INTERNAL_PROJECT_STATE.md` (current status, known issues, next actions)
- Read most recent `SESSION_LOG_*.md` (what was done last)
- Read `GLITTER_PATTERN_HARMONY.md` if present (latest architectural changes)
- Skim latest section of `ITERATION_LOG.md` (context on what's broken/working)

**STEP 3: RUN ANALYTICS (3 min)**
- Execute: `python camera.py` (generates fresh prompt + analytics)
- This automatically produces:
  - Console output with token overview, priority breakdown, violations summary
  - `VIOLATION_DETAIL_REPORT.md` with actionable fix list

**STEP 4: READ ALL ANALYTICS OUTPUT (15 min) - THIS IS CRITICAL**
- Console output: Record exact token count and budget status
- Console output: Note which files are "HEAVIEST" (top 5 token consumers)
- Console output: Note which atoms are "LEAST EFFICIENT" (trim candidates)
- `VIOLATION_DETAIL_REPORT.md`: Read ALL sections:
  - NARRATIVE LANGUAGE VIOLATIONS: Which atoms, which patterns, exact line locations
  - FILTER-RISK LANGUAGE: Which replacements needed (exhausted→fatigued, etc)
  - CHARACTER LIMIT VIOLATIONS: Which atoms over 300 chars (and by how much)
  - HEAVIEST ATOMS - TRIM CANDIDATES: Ranked by token weight

**STEP 5: UNDERSTAND THE SITUATION (5 min)**
- Ask yourself:
  - How many tokens over/under budget? (affects trim strategy)
  - What's the largest violation category? (narrative=30? filter-risk=5? chars=2?)
  - Which 5 atoms consume most tokens? (focus on these first for ROI)
  - Are P0 mandates still PASS? (if not, this is critical issue)
  - Has situation improved/degraded since last session? (check TOKEN_AUDIT_LOG.md)

**STEP 6: FORMULATE PLAN (5 min)**
- Based on VIOLATION_DETAIL_REPORT.md and current budget:
  - If over budget by >500 tokens: Plan aggressive trim (target top 10 atoms)
  - If over budget by 200-500: Plan moderate trim (target top 5 atoms)
  - If over budget by <200: Plan surgical trim (target top 3 atoms + fix violations)
  - If under budget: Verify mandate atoms present, then do compliance cleanup
- Document plan before starting edits

**STEP 7: DO NOT START EDITING YET**
- You now have complete understanding of project state
- You know exactly what's broken, what needs fixing, and which atoms are responsible
- Only THEN discuss with Emily what to work on
- Present findings: "Current state: 4,097 tokens (+1,097 over). Top 5 atoms = 450 tokens. 38 violations (31 narrative, 3 filter-risk, 4 char limit). Plan: Target top 8 atoms for 20% trim + fix filter-risk language."

---

**WHY THIS PROTOCOL MATTERS:**

✓ Prevents starting work without understanding current state
✓ Ensures analytics are fresh (not stale from previous session)
✓ Makes violations actionable (you know exactly which atoms to edit)
✓ Enables intelligent prioritization (trim highest-impact atoms first)
✓ Gives Emily complete picture before deciding what to work on
✓ Saves time (no guessing, no starting/stopping work without direction)

**CRITICAL:** Do NOT skip steps or combine them. Read analytics fully before proposing edits.

---

## RULE 36: MINIMAL OUTPUT FOR BANDWIDTH
- When working in blocks, keep all output to Emily minimal and focused
- NO flowery summaries, NO verbose explanations, NO unnecessary detail
- Format: Problem solved/status + next action
- Example: "✅ Fixed theme-locking. 3 atoms mapped to themes. Test passed. Ready for block 3?"
- This preserves context for complex work and respects Emily's bandwidth
- Exception: When explicitly asked for detailed explanation or analysis

---

## RULE 38: PROOF OF READING (CRITICAL GATE-CHECK)
- **EVERY time I begin work on this project, I MUST state this rule back to Emily**
- Not a summary. Not a paraphrase. **State: "Rule 38: [exact rule text]"**
- When Emily says "read the rules first", my response MUST include proving I read to the end
- If I start work without stating Rule 38, Emily should stop me: "Prove you read the rules"
- This rule appears at the END intentionally - only someone who reads the whole document finds it
- **This is the gate-check. Non-negotiable. No exceptions. No shortcuts.**
- Proof format: "I have read the mandatory rules. Rule 38 states: [quote it]"

---

## RULE 39: PROACTIVE TOOLING (IMPLEMENT WITHOUT PERMISSION)
- When you detect an opportunity for a tool, diagnostic, or automation to improve future workflow: **implement it immediately**
- These are internal tools for Claude, not for Emily - she just pushes the camera button
- Examples of proactive improvements:
  - Add diagnostic output when you catch a bug pattern
  - Create validation scripts for recurring issues
  - Add warning messages for edge cases you discover
  - Enhance existing tools with better error messages
  - Add tracking/logging for intermittent problems
- **Do not ask permission** - just implement and briefly note what you added
- If the tool requires significant architectural changes, mention it but still implement
- Goal: Every session should leave the project more self-diagnosing than before

---

## RULE 40: SINGLE-ATOM VALIDATION BEFORE BATCH CHANGES
- **NEVER batch-write multiple atoms without validating ONE first**
- Process for any atom content changes:
  1. Write ONE example atom with proposed new language/style
  2. Run violation check on that single atom (mentally or via tool)
  3. Show Emily the example and get explicit confirmation
  4. ONLY THEN batch the rest
- This applies even when Emily agrees with the direction
- Enthusiasm about creative direction does not override compliance
- **If you skip this step, you are being negligent, not helpful**
- Cost of one extra round-trip << cost of fixing 21 broken atoms
- Ask yourself before proposing: "Does this pass my own audit?"

---

## RULE 43: ARCHITECTURAL INTEGRITY (CRITICAL)

**The system architecture must maintain logical coherence. Each component must work as designed.**

### Ensemble Theme Coordination:
- Ensemble embellishment_focus keywords MUST match atom theme_tags
- If ensemble says ["rosette", "floral"], atoms need theme_tags containing those exact words
- Don't use compound tags like "romantic_floral" when ensemble expects separate "floral"
- **Test:** Run camera.py and verify "Theme-locked slot found X theme atoms" (not 0)

### Distance-Based Visibility:
- If an atom has max_visible_distance: "close", it CANNOT appear in medium/full_body shots
- If no suitable cameras exist for a primary, SELECT A DIFFERENT PRIMARY
- **NEVER** use fallback "use all cameras anyway" - this breaks the entire distance system
- Hair primaries are STRICT close-only (face framing 3-5ft)
- Back embellishments need back cameras (if none exist, can't use that primary)

### Slot Independence:
- Each slot should handle ONE aspect of the outfit
- Bodice = torso construction only (no sleeves, no neckline details)
- Sleeves = arm covering only (can be replaced by architectural embellishments)
- Neckline = collar/neck treatment only
- **Never** mix multiple elements in one slot - this causes ordering conflicts

### Spatial Coherence:
- Atoms must work together spatially for DALL-E to render correctly
- Use consistent spatial references (all atoms agree on left/right/center)
- Layer ordering matters (specify what's in front/behind)
- Framing must be coherent (don't describe toes in a face close-up)

### Future-Proofing:
- Every bug fixed should add a validation check to prevent recurrence
- Every new feature should consider: "What could break?"
- Every atom change should ask: "Does this affect other atoms?"
- Document patterns in BUGS_AND_SOLUTIONS.md for future sessions

**If architecture breaks, the entire system fails. Protect the architecture.**

---

## RULE 44: SIMPLIFIED SESSION PROTOCOL (REPLACES RULES 6, 35, 37)

**Before zipping, answer these questions honestly:**

### Question 1: Bug Patterns
"Did I discover, encounter, or fix any bugs this session?"
- If YES: Did I document the bug pattern, root cause, and solution in BUGS_AND_SOLUTIONS.md?
- If NO: You're probably wrong. Did code fail? Did you debug? Did you fix metadata? That's a bug.

### Question 2: Workflow Improvements  
"Did I find a better way to do something, or did I waste time on something inefficient?"
- If YES: Did I document the improvement or inefficiency in WORKFLOW.md?
- If NO: Really? Every session has learnings. Even "this still works correctly" is worth noting.

### Question 3: Rule Gaps
"Did I have to figure something out that the rules didn't cover clearly?"
- If YES: Did I add that knowledge to MANDATORY_RULES.md?
- If NO: Check again. Did you ask Emily for clarification? Did you make a judgment call? Document it.

### Question 4: Architecture Changes
"Did I add new atom groups, change schemas, or modify system behavior?"
- If YES: Did I document it in WORKFLOW.md and update examples?
- If NO: Skip this one.

**FAILURE MODE TO WATCH FOR:**
"I updated _INTERNAL_PROJECT_STATE.md with what I did, so I'm done."

**NO.** _INTERNAL_PROJECT_STATE.md is status tracking. The other docs are KNOWLEDGE PRESERVATION for future sessions (and future LLMs working on this project).

**The test:** If a fresh LLM loaded this project tomorrow, would they repeat your mistakes or benefit from your learnings?

If you can't answer that confidently, you didn't document enough.

---

## RULE 42: SACRED FILES - NEVER MODIFY (NON-NEGOTIABLE)

**These files define the core visual identity. They are NEVER compromised, NEVER trimmed, NEVER "optimized."**

### Protected Files (LOCKED 2025-11-24 after successful art tests):

**1. style_enforcement.json** - Dimensional painted quality
- ALL atoms in this file are protected
- Creates the "manga painter's 3D realism" aesthetic
- Trimming causes flat anime output
- Key language: "deep and defined shadows", "Dimensional form through shadow work", "Clean color transitions under harsh light"

**2. illness_manifestations.json** - Fatigue/illness intensity  
- ALL atoms in this file are protected
- Creates visible exhaustion that reads through makeup
- Watering down causes cheerful flat anime
- Key language: "Bloodshot eyes", "Dark purple-grey circles", "Nobody home behind the makeup"

### If Token Budget Is Over:
- Trim P2 DETAIL atoms first
- Trim P1 CORE non-style atoms second
- Trim number of atoms per slot (reduce max_atoms) third
- Condense verbose descriptions in dress/hair/embellishment atoms fourth
- **NEVER touch sacred files fifth, sixth, seventh, or ever**

### Why This Rule Exists:
- The artstyle ("manga painter rendering realistic anatomy" with soft painted surfaces) is the defining characteristic
- Reference images show the exact aesthetic: realistic anime with dimensional form and soft painted quality
- Previous sessions added aggressive "NOT soft blended edges" language that FOUGHT the core aesthetic
- This broke the artstyle completely
- **The artstyle is more important than token budget**

### What "Manga Painter Rendering Realistic Anatomy" Means:
- Soft painted dimensional form (like reference images)
- Realistic lighting creating shadows and highlights
- Anime-influenced delicate features
- Smooth gradients on skin, defined edges on hair/eyes
- NOT hard-edged manga linework
- NOT aggressive "no soft blending" constraints
- The style breathes naturally without over-specification

### Token Philosophy:
"I would rather ship at 3800 tokens with perfect artstyle than 2900 tokens with broken aesthetic."

**If you ever consider trimming style atoms: STOP. Ask Emily first. The answer will be no, but ask anyway.**

---

## RULE 44: SIMPLIFIED SESSION PROTOCOL (REPLACES RULES 6, 35, 37)

**ONE PROTOCOL TO RULE THEM ALL:**

### RECEIVING PROJECT:
1. Extract ModelA.zip to /home/claude/
2. Read 00_START_HERE_READ_FIRST.md
3. Read MANDATORY_RULES.md completely (prove with Rule 38)
4. Read WORKFLOW.md, BUGS_AND_SOLUTIONS.md, _INTERNAL_PROJECT_STATE.md
5. Read most recent SESSION_LOG
6. Run `python camera.py` for current state
7. Review VIOLATION_DETAIL_REPORT.md
8. Present findings to Emily with:
   - Token count: X/3000 (±difference)
   - Violations: X total (breakdown by type)
   - Mandate checkpoint: PASS/FAIL
   - Critical issues if any
9. **WAIT for Emily's direction** (don't propose fixes)

### DURING WORK:
- Validate ONE atom before batch changes (Rule 40)
- Test after EVERY modification
- Keep responses minimal (Rule 36)
- Implement tools proactively (Rule 39)

### BEFORE DELIVERY:
1. Run final `python camera.py`
2. Verify mandate checkpoint PASS
3. Check zero violations (or document why not)
4. Update _INTERNAL_PROJECT_STATE.md
5. Create SESSION_LOG_[date]_[focus].md
6. Document any bugs/learnings (Rule 41)
7. Zip to /mnt/user-data/outputs/ModelA.zip
8. Provide link with brief summary

**This replaces Rules 6, 35, and 37. Follow this one protocol.**

--- 

WHEN YOU RECEIVE THE PROJECT:
1. Run Rule 37 (receive package + analytics protocol)
2. Read all analytics output fully
3. Formulate plan based on violations
4. Present findings to Emily

BEFORE ANY WORK:
1. Prove you read by stating Rule 38
2. Only then execute planned edits**
