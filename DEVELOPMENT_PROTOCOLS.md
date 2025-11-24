# DEVELOPMENT PROTOCOLS FOR MODELA

**These protocols prevent common logic errors and ensure clean development**

---

## PROTOCOL 1: Pre-Change State Capture
Before making ANY modifications:
```python
# Capture current state
tokens_before = run_camera() -> extract_token_count()
violations_before = run_violation_report() -> count
atom_counts_before = count_atoms_by_group_and_priority()
```

## PROTOCOL 2: Slot Isolation Testing
After modifying any slot logic:
1. Generate 5+ test prompts
2. Extract each slot's content
3. Check for atom duplication across slots
4. Verify correct group assignments (D0_Core vs D1_Architectural)
5. Document: "Tested - no cross-contamination"

## PROTOCOL 3: The Deduplication Check
After EVERY camera.py run during development:
```python
# Check for atoms appearing multiple times
all_atoms_in_prompt = extract_all_atoms()
duplicates = [a for a in all_atoms if count(a) > 1]
if duplicates: STOP and FIX
```

## PROTOCOL 4: Group Assignment Verification
When adding/modifying embellishments:
- D1_Architectural → ONLY in theme_embellishment_primary slot
- D0_Core → ONLY in dress.embellishments slot
- Run test: atom appears in correct slot across 10 generations

## PROTOCOL 5: Priority Reality Check
Remember priority behavior:
- P0: MANDATE → Always included
- P1: CORE → Randomly selected up to max_atoms
- P2: DETAIL → Only if room after P0+P1
- Changing P1→P2 may make atom never appear!

## PROTOCOL 6: The "Will This Actually Work?" Test
Before declaring any fix complete:
```python
for i in range(10):
    generate_prompt()
    check_no_duplication()
    check_correct_slots()
    check_theme_matching()
    check_variety()
```

## PROTOCOL 7: Cascade Impact Analysis
Before structural changes, map dependencies:
1. Which slots pull from this file?
2. Which atoms have "requires" pointing here?
3. What happens if this atom never loads?
4. Test all downstream elements after change

## PROTOCOL 8: Max_Atoms vs Pool Size Check
```python
if slot.max_atoms > len(available_atoms_in_pool):
    WARNING: "Will cause repetition!"
```

## PROTOCOL 9: Surgical Changes Only
NEVER use:
- `rm -f *.py` (too broad)
- Mass updates without specific targeting
- Global replacements without context

ALWAYS use:
- `rm -f test_*.py debug_*.py` (specific patterns)
- Updates with `if key == 'specific_key'`
- Full context string replacements

## PROTOCOL 10: Test Output, Not Logic
Don't assume code logic = correct output
ALWAYS verify through actual generation:
- Generate prompt
- Check what actually appears
- Verify it matches intention

## PROTOCOL 11: The Restoration Safety Net
Before major changes:
```bash
cp -r definitions/ definitions_backup_$(date +%s)/
```

## PROTOCOL 12: Multi-Generation Variety Test
```python
def test_variety(n=10):
    unique_signatures = set()
    unique_complements = set()
    
    for i in range(n):
        prompt = generate()
        unique_signatures.add(extract_theme_embellishment())
        unique_complements.add(extract_shiny_embellishments())
    
    if len(unique_signatures) < n/2:
        WARNING: "Not enough variety in signatures"
    if len(unique_complements) < n/2:
        WARNING: "Not enough variety in complements"
```

## PROTOCOL 13: Pre-Delivery Checklist
```bash
# Must all pass before delivery
[ ] No test_*.py or debug_*.py files
[ ] camera.py runs without errors
[ ] No atom duplication in prompt
[ ] D0/D1 groups correctly assigned
[ ] Token count logged
[ ] Violations logged
[ ] Run development_protocols.py → ALL PASS
```

## PROTOCOL 14: The "What Pulls From This?" Map
Before modifying any definition file:
```bash
grep -n "filename.json" layer_slot_schema.json
# List every slot that sources from it
# Note prefixes, groups, min/max atoms
```

## PROTOCOL 15: Ensemble-to-Embellishment Path Trace
When embellishments don't match themes:
1. Verify ensemble has `embellishment_focus`
2. Check focus keywords exist in target atoms
3. Add debug output showing selection path
4. Trace: ensemble → focus → matching atoms → selected

---

## QUICK REFERENCE COMMANDS

**Test current state:**
```bash
python development_protocols.py
```

**Test embellishment slots specifically:**
```bash
python test_embellishment_slots.py
```

**Check for duplication:**
```bash
python camera.py && grep "Theme Embellishment" prompt.txt && grep "Shiny Embellishments" prompt.txt
```

**Verify groups:**
```python
python -c "import json; e=json.load(open('definitions/shiny_embellishments.json')); 
d0=[k for k,v in e.items() if v.get('group')=='D0_Core']; 
d1=[k for k,v in e.items() if v.get('group')=='D1_Architectural']; 
print(f'D0: {len(d0)}, D1: {len(d1)}')"
```

---

**Follow these protocols to avoid logic errors and rework!**

---

## DIAGNOSTIC: DUPLICATE ATOM DETECTION

camera.py now includes automatic duplicate detection. If any atom appears in multiple slots, you'll see:

```
🚨 DUPLICATE ATOM DETECTION
────────────────────────────────────────────────────────────
  ⚠️  expression.gaze_aimed_unfocused
      Appears in: expression.camera_gaze, expression.core

  FIX GUIDANCE:
  ─────────────
  1. Check atom's 'group' field in definitions/*.json
     - D0_Core atoms → should ONLY appear in 'dress.embellishments'
     - D1_Architectural atoms → should ONLY appear in 'theme_embellishment_primary'
  2. If group is correct, check camera.py filtering logic:
     - Lines ~150-175: Group filters for each slot
     - Verify slot_id matching is exact
  3. Check layer_slot_schema.json for slot configuration
     - Verify include_prefixes don't overlap
  4. Run: python development_protocols.py for deeper analysis
────────────────────────────────────────────────────────────
```

**Common causes:**
- Overlapping `include_prefixes` in layer_slot_schema.json
- Missing or incorrect `group` field on atoms
- Missing slot-specific filters in camera.py select_atoms_for_slot()
- Atom key matches multiple slot patterns

**Fix checklist:**
1. Identify which slots are pulling the same atom
2. Check if slots have overlapping prefixes
3. Add group filtering if embellishment-related
4. Add explicit exclusion if slots should be mutually exclusive
