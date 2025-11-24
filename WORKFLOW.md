# WORKFLOW.md - ModelA Development Patterns

**How we work on this project. Read this before making any changes.**

---

## CORE PRINCIPLES

### 1. ATOMS ARE VISUAL FACTS ONLY
- Describe what a camera would see
- No process language: "stitched," "creates," "layered," "applied"
- No interpretation: "beautiful," "elaborate," "professional," "precious"
- No time: "hours of," "after preparation," "recently"
- No emotion: "grim," "haunting," "resigned," "vacant"

**Test:** Would a camera capture this exact detail? If "maybe," remove it.

### 2. COMPLIANCE FIRST, CREATIVITY SECOND
- Run analytics BEFORE making changes
- Fix violations BEFORE adding features
- Test AFTER every modification
- Never ship with violations

### 3. ITERATIVE VALIDATION
- Never batch-write multiple atoms without validating ONE first
- Show Emily ONE example atom
- Get explicit approval
- THEN batch the rest

**Why:** Cost of one extra round-trip << cost of fixing 21 broken atoms

---

## STANDARD WORKFLOW

### RECEIVING PROJECT
1. Extract zip
2. Read 00_START_HERE_READ_FIRST.md
3. Follow protocol completely
4. Present orientation report
5. Wait for assignment

### MAKING CHANGES
1. Identify specific atoms to modify (from analytics)
2. Make changes to ONE atom as example
3. Verify that ONE atom passes rules
4. Show example to Emily
5. Get approval
6. Apply pattern to remaining atoms
7. Run analytics immediately
8. Verify all changes pass

### BEFORE DELIVERY
1. Run `python camera.py` one final time
2. Verify: Mandate checkpoint PASS
3. Verify: Zero violations
4. Verify: Token budget acceptable (2800-3200)
5. Clean junk files
6. Zip and deliver

---

## TESTING STANDARDS

### Every Change Requires:
- ✅ Code runs without errors
- ✅ All atoms load correctly
- ✅ Mandate checkpoint PASS
- ✅ Zero narrative violations
- ✅ Zero filter-risk violations
- ✅ Zero character-limit violations
- ✅ Token count logged

### Analytics Tools:
- `python camera.py` - Main generator with integrated analytics
- Console output shows: tokens, violations summary, mandate check
- VIOLATION_DETAIL_REPORT.md shows: detailed violations with line numbers
- `python theme_diagnostic.py` - Check theme coordination between ensembles and atoms

### What Each Tool Does:
- **camera.py** - Generates prompt + runs full analytics suite
- **analytics.py** - Library for token counting (used by camera.py)
- **violation_reporter.py** - Scans atoms for compliance (used by camera.py)

**Never run tools individually - just run camera.py**

---

## COMMON PATTERNS THAT WORK

### Token Reduction:
- Target heaviest files first (check analytics output)
- Trim 10-20% across multiple files, not 40% from one
- Character limits: P0/P1 max 300 chars, P2 max 200 chars
- If atom exceeds limit: split into 2 atoms, don't compress

### Atom Writing:
- Start with observable noun: "Beaded fringe," "Lace medallion," "Pearl buttons"
- Measurements: "5mm," "45°," "2in intervals"
- Position: "at shoulder seam," "center front," "left side"
- Count: "3 clusters," "8 buttons," "4 rosettes"
- Visual properties: "glossy," "matte," "translucent," "reflective"
- **SHOW evidence, don't CLAIM quality:**
  - ❌ "Precious masterwork," "bespoke artistry," "virtuoso precision"
  - ✅ "Particles positioned at 1-2mm intervals," "gradient density 95%→70%→40%," "6-7 products stacked"
  - Pattern: Observable precision PROVES world-class work happened

### Schema Changes:
- Test immediately after any layer_slot_schema.json change
- Run `python camera.py` to verify all slots still pull
- Schema changes affect entire system
- If unsure, ask first

### Distance-Aware Filtering:
- Primary embellishment's `min_visible_distance` determines camera requirements
- This distance filters ALL atoms based on their `min_visible_distance` metadata
- Pattern: Pre-select embellishment in main() → determine distance → pass to all slots
- close camera: shows all detail levels (close, medium, full_body)
- medium camera: shows medium + full_body only (NOT close details)
- full_body camera: shows full_body only (NOT close or medium details)
- Atoms without distance metadata pass through (backward compatibility)

### Distance-Aware Max_Atoms:
- Certain slots load MORE atoms when close camera selected
- Makeup slot: 15 atoms for close-ups (vs 8 for medium/full_body)
- Enables comprehensive micro-detail visible at close range
- Implementation: camera.py checks slot_id and camera_distance before atom selection

---

## ATOM ARCHITECTURE

### Priority System:
- **P0 MANDATE** - Non-negotiable, always present (age safety, style foundation, dissonance)
- **P1 CORE** - Main dress details (colors, fabrics, construction, expression)
- **P2 DETAIL** - Optional enhancements (accessories, minor embellishments)

### Embellishment Hierarchy:
- **D1_Architectural** - PRIMARY dress embellishment (one big transformative thing on dress)
- **D1_Hair_Architectural** - PRIMARY hair embellishment (audacious statement pieces 25-40cm, STRICT close-camera only)
- **D0_Core** - COMPLEMENTARY details (small supporting accents)

**Critical:** 
- D0_Core atoms must SUPPORT the primary, not compete with it
- Hair primaries (D1_Hair_Architectural) ONLY work with close cameras (3-5ft)
- Dress and hair primaries compete for theme_embellishment_primary slot

### Group Usage:
- P0 atoms are protected - ask before deleting
- D1_Architectural = the star of the dress
- D1_Hair_Architectural = audacious head-focused statement (forces close cameras)
- D0_Core = supporting cast
- Never let D0 compete with D1

---

## FILE ORGANIZATION

### Definition Files:
- One concept per file (e.g., dress_colors.json, hair_styling.json)
- Keep related atoms together
- Don't scatter theme atoms across multiple files

### Naming Conventions:
- Atom IDs: `category.specific_name` (e.g., `dress.color.lavender`)
- Files: `category_subcategory.json` (e.g., `dress_patterns.json`)
- Logs: `SESSION_LOG_YYYY-MM-DD.md`

### What Goes Where:
- definitions/ - All atom JSON files
- docs/ - Vision, standards, architecture docs
- Root - Python scripts, schema, config
- Logs/reports in root (not in subdirs)

---

## DELIVERY PROTOCOL

### What to Include:
- All modified files
- New SESSION_LOG documenting changes
- Updated _INTERNAL_PROJECT_STATE.md
- Fresh analytics run (console output in log)

### Delivery Format:
- Zip entire ModelA directory
- Place in /mnt/user-data/outputs/
- Provide computer:// link
- Brief summary: "Fixed [what]. [Result]. Ready."

### Delivery Message Style:
- Direct and concise
- State what changed
- State verification results
- No flowery language
- No excessive summaries
- Just: problem → solution → link

**Example:** "6 atoms rewritten for embellishment coordination. Zero violations. Ready."

---

## WHAT NOT TO DO

### ❌ Never:
- Skip reading orientation documents
- Propose solutions before presenting findings
- Batch changes without validating one first
- Ship with violations
- Delete P0 atoms without asking
- Change schema without testing
- Make assumptions about what Emily wants
- Add features when asked to fix bugs
- Grep for Rule 38 (read the whole doc)

### ⚠️ Always Ask First:
- Before deleting any P0 MANDATE atom
- Before major schema restructuring
- Before changing core architectural concepts
- When unsure about atom compliance
- When solution requires trade-offs

---

## SESSION DISCIPLINE

### Start of Session:
1. Read all orientation docs
2. Run analytics
3. Present findings
4. Wait for direction

### During Session:
1. Follow assigned work
2. Stay focused on the goal
3. Validate incrementally
4. Report progress briefly

### End of Session:
1. Final analytics run
2. Verify zero violations
3. Update logs and state
4. Zip and deliver

**The workflow exists to prevent mistakes, not slow you down. Follow it.**

---

## TOKEN OPTIMIZATION: DISTANCE-AWARE TRIMMING PROTOCOL

**When to use**: Token count exceeds budget and needs reduction

### Step 1: Identify Camera Distance Context
- Close-up: Face-only framing (makeup documentation distance)
- Medium: Upper body (head, shoulders, torso, bodice)
- Full body: Complete figure (head to feet, full dress, floor visible)

### Step 2: Audit Sections by Visibility

**For CLOSE-UPS** (face-only):
- ✅ Keep: Makeup (all details), hair, expressions, illness, face-level style
- ⚠️ Trim: Neckline (only edge visible)
- ❌ Cut: Full dress construction, skirt, petticoat, bodice details, body proportions below neck
- ❌ Cut: Floor perspective, background equipment, spatial depth, scene details

**For MEDIUM** (upper body):
- ✅ Keep: Makeup, hair, expressions, bodice, neckline, upper dress, accessories visible on upper body
- ⚠️ Trim: Full skirt construction, detailed petticoat description
- ❌ Cut: Floor details below mid-torso

**For FULL BODY**:
- ✅ Keep: Everything (all atoms relevant)

### Step 3: Implement Distance Filters
Add `min_visible_distance` or `max_visible_distance` metadata to atoms:
```json
"min_visible_distance": "medium"  // Only loads for medium/full_body, not close
"max_visible_distance": "close"   // Only loads for close, not medium/full_body
```

### Step 4: Check for Duplicate Atoms Across Slots
- Review layer_slot_schema.json for overlapping include_prefixes
- Add exclude_prefixes where needed to prevent duplicate loading
- Example: expression.core should exclude "expression.gaze_" since camera_gaze already loads those

### Step 5: Consolidate Redundant Atoms
- Search definitions for atoms describing same visual concept
- Keep most comprehensive version
- Delete or add mutual exclusion to others
- Example: Multiple highlighter atoms describing same facial points → keep one comprehensive version

### Step 6: Trim Individual Atom Verbosity (Last Resort)
- Remove filler words: "very," "quite," "somewhat," "rather"
- Remove redundant descriptors: "soft gentle" → "soft"
- Consolidate repetitive phrasing
- ⚠️ Never trim: measurements, specific positions, observable facts

### Token Savings Priority
1. Distance filtering (highest impact, no quality loss)
2. Fix duplicate loading bugs (pure savings)
3. Consolidate redundant atoms (moderate savings, slight variant loss)
4. P2 DETAIL max_atoms reduction (reduces variety)
5. Individual atom trimming (last resort, can impact quality)

### What NEVER to Trim (Rule 42)
- Style enforcement atoms (artstyle is sacred)
- P0 MANDATE atoms (critical requirements)
- Age safety checkpoints (compliance requirement)
- Core aesthetic language ("manga painter rendering realistic anatomy")

**Session where developed**: 2025-11-23 token audit (5,027 → 4,683 tokens)
