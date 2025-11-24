# Atom Writing Standards - ModelA

## CRITICAL MANDATE: No Narrative Language

### ❌ FORBIDDEN - Narrative/Backstory Language
Atoms must contain ONLY visual descriptors. Remove ALL narrative, process, motivation, and time-reference language.

**NEVER include:**
- Time references: "hours of", "2-3 hours", "Shows time investment", "requires extensive time"
- Process descriptions: "Each layer buffed", "Applied with brush", "hand-sewn individually"
- Interpretive language: "Reads as", "Creates aesthetic", "Shows", "Demonstrates", "Suggests"
- Motivation/intent: "Professional technique", "Salon precision", "Special occasion"
- Skill descriptions: "Careful application", "Precision work", "Elaborate styling"
- Backstory: "after 12-16 hour session", "endless preparation"

### ✅ CORRECT - Direct Visual Description
Describe only what is VISIBLE in the final render.

**Examples:**

❌ WRONG (narrative):
```
"Foundation applied in multiple thin layers creating buildable coverage. Each layer buffed with beauty sponge or brush in circular motion. 4-5 layers applied over 2-3 hours showing time investment."
```

✅ CORRECT (visual only):
```
"Foundation in multiple thin layers. Slight texture from layering."
```

❌ WRONG (narrative):
```
"Small sections pin-curled and set showing tight curl definition in strategic areas. Old-fashioned setting technique creating spiral details through bob. Time-intensive salon setting visible."
```

✅ CORRECT (visual only):
```
"Small sections pin-curled with tight curl definition. Spiral details through bob."
```

❌ WRONG (narrative):
```
"Sequins densely applied across bodice and scattered throughout skirt tiers - hundreds of individual sequins catching light. This reads as HOURS of hand-applied embellishment work."
```

✅ CORRECT (visual only):
```
"Sequins densely applied across bodice and scattered throughout skirt tiers - hundreds catching light."
```

## Why This Matters

**Token Efficiency:**
- Narrative language wastes 20-30% of atom tokens
- Models ignore process descriptions
- Only final visual state affects render

**Clarity:**
- Direct visual description is clearer
- Removes ambiguity about what to render
- Focuses model on appearance, not backstory

## Revision Checklist

When writing/revising atoms, remove:
- [ ] All time references (hours, minutes, duration)
- [ ] All process descriptions (how it's done)
- [ ] All "Reads as", "Shows", "Creates", "Demonstrates"
- [ ] All skill/technique descriptions
- [ ] All motivation/intent language
- [ ] All backstory/context not visible in frame

Keep ONLY:
- [ ] Physical appearance descriptors
- [ ] Spatial relationships
- [ ] Color/texture/material properties
- [ ] Dimensional/form qualities
- [ ] Light interaction properties

## Atom Structure Template

```json
{
  "atom.name": {
    "domain": "DOMAIN",
    "tier": 1,
    "description": "Brief visual summary",
    "contents": "[Visual descriptor]. [Another visual descriptor]. [Physical property]. [Dimensional quality].",
    "group": "group_name",
    "priority": "P0: MANDATE",
    "random": false
  }
}
```

**Contents field rules:**
- Short declarative sentences
- Present tense only
- Visual properties only
- No narrative connectors ("showing", "creating", "demonstrating")
- Keep technical descriptors (dimensions, colors, materials)
- Remove human process (application, technique, precision)

## Common Violations to Remove

### Time References
- ❌ "over 2-3 hours"
- ❌ "Shows hours of"
- ❌ "requires extensive time"
- ❌ "time-intensive"
- ❌ "time investment visible"

### Process Language
- ❌ "applied with"
- ❌ "Each layer buffed"
- ❌ "hand-sewn individually"
- ❌ "carefully placed"
- ❌ "precision application"

### Interpretive Language
- ❌ "Reads as"
- ❌ "Creates [aesthetic]"
- ❌ "Shows [quality]"
- ❌ "Demonstrates [skill]"
- ❌ "Suggests [story]"

### Skill/Technique
- ❌ "Professional technique"
- ❌ "Salon precision"
- ❌ "Expert application"
- ❌ "Elaborate styling"
- ❌ "Technical execution"

### Backstory/Context
- ❌ "Special occasion"
- ❌ "Portrait day"
- ❌ "Formal event"
- ❌ "After hours of preparation"

---

## RULE: MAXIMUM POWER WITH MINIMUM LANGUAGE

### LENGTH TARGETS (MANDATORY):
- Simple atoms: 50-100 characters
- Medium atoms: 100-200 characters  
- Complex atoms: 200-300 characters MAX
- **NEVER exceed 300 characters unless absolutely critical**

### What to INCLUDE:
- Visual result (what you see)
- Core facts (color, size, position, material)
- Essential behavior (if it moves, how)

### What to EXCLUDE:
- Process descriptions ("applied with brush", "set for 2 hours")
- Tool specifications ("using pin curls", "with fluffy brush")
- Time investment statements ("shows hours of work")
- Obvious modifiers ("carefully", "precisely", "professionally")
- Redundant style reminders ("realistic digital rendering of", "dimensional")

---

## RULE: ELIMINATE REDUNDANT REINFORCEMENT

❌ WRONG (says "shimmer" FOUR times):
```
"Organza woven with metallic threads creating iridescent shimmer. Crisp transparent structure with dimensional sparkle. Light refracts through fabric creating rainbow shimmer effect. Metallic threads catch light creating glinting highlights throughout."
```

✅ CORRECT:
```
"Metallic organza. Crisp transparent with iridescent shimmer. Light refracts creating rainbow glints."
```

**Don't repeat the same concept multiple times in different words.**

---

## FORBIDDEN PHRASES - DELETE ON SIGHT

1. "Realistic digital rendering of..."
2. "Shows X hours of work/time investment"
3. "Professional salon technique/placement"
4. "Creates dimensional X effect" → just say "X"
5. "Applied with [tool]"
6. "Each layer carefully/precisely..."
7. "Fabric has body and spring" → "Structured fabric"
8. "[Action] with realistic X response" → "[Action] with X behavior" or delete

---

## OVERUSED WORDS - REDUCE BY 70%

- **"dimensional"** - use sparingly, once per atom MAX
- **"creating"** - often unnecessary connector word
- **"realistic"** - CONFLICTS with 2.5D goal
- **"carefully" / "precisely"** - always assumed, delete

---

## RULE: 2.5D LANGUAGE MANDATE

### When describing materials/rendering:

**PREFER:**
- "Painted aesthetic"
- "Stylized"
- "Simplified"
- "Clean gradients"
- "Soft surface quality"

**AVOID:**
- "Realistic"
- "Photographic"
- "Accurate physics"
- "True-to-life"
- "Detailed texture"

**Style enforcement belongs ONLY in style_enforcement.json - don't repeat "realistic digital rendering" in every atom.**

---

## THE GOLDEN RULE

**"If it doesn't change what you see in the final image, delete it."**

Process, tools, time, technique → DELETE  
Visual result, color, position, behavior → KEEP

---

## EDITING CHECKLIST (Use for EVERY atom)

Before saving ANY atom:

- [ ] Under 300 characters (preferably under 200)
- [ ] No process descriptions (how it was made)
- [ ] No tool specifications  
- [ ] No time investment statements
- [ ] No "realistic digital rendering of..." phrases
- [ ] No redundant concepts repeated multiple times
- [ ] "Dimensional" used once or not at all
- [ ] States visual result, not creation process
- [ ] No forbidden phrases listed above
- [ ] Uses 2.5D language, not photorealism language
- [ ] One concept per sentence (no run-ons)

---

## Enforcement

This is a **MANDATORY** standard for all atoms. When revising atoms:
1. Read each sentence
2. Ask: "Is this describing what's VISIBLE or how it GOT there?"
3. If it's process/backstory/time → DELETE
4. If it's visual appearance → KEEP
5. Count characters - if over 300, cut until under 200
6. Check forbidden phrases list - delete any found
7. Check for "realistic" language - replace with 2.5D language
8. Remove repetition of same concept

No exceptions. Visual description only. Maximum efficiency.
