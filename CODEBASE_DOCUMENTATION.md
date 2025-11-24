# ModelA Codebase Documentation

## Overview

ModelA is a sophisticated **AI image prompt generation system** designed to create highly detailed, consistent prompts for generating "manga painter's 3D realism" aesthetic images. The system generates prompts for AI image generators (like DALL-E) with a focus on:

- A specific artistic style: manga illustration with dimensional realism
- A specific character: An AMAB nonbinary adult (20-24) with specific features
- A specific aesthetic: Couture dress in clinical/institutional environment
- Thematic coherence through ensemble-based coordination

---

## Architecture Overview

```
ModelA/
├── camera.py                    # Main generator (1,372 lines)
├── analytics.py                 # Token counting and analysis
├── violation_reporter.py        # Compliance checking
├── generation_analytics.py      # Generation tracking/history
├── theme_diagnostic.py          # Theme coordination checker
├── development_protocols.py     # Testing protocols
├── manifest.py                  # Project snapshot generator
├── layer_slot_schema.json       # System architecture
├── config.json                  # Legacy configuration
├── definitions/                 # Atom library (~28 JSON files)
│   ├── style_enforcement.json   # Core art style atoms
│   ├── character_core.json      # Character identity atoms
│   ├── dress_ensembles.json     # Thematic ensemble pools
│   └── [25+ other definition files]
└── docs/                        # Documentation archive
```

---

## Core Components

### 1. `camera.py` - Main Generator

**Purpose:** The primary entry point that generates complete prompts.

**Key Classes/Functions:**

| Component | Description |
|-----------|-------------|
| `Atom` class (L84-110) | Data structure for prompt fragments with metadata (priority, group, distance, theme_tags, etc.) |
| `load_atoms()` (L112-128) | Loads all atoms from JSON definition files |
| `load_schema()` (L237-241) | Loads the layer/slot architecture |
| `coordinate_camera_with_embellishment()` (L130-235) | Filters camera angles based on embellishment placement |
| `select_atoms_for_slot()` (L260-695) | Core selection logic with filtering by distance, theme, groups |
| `build_prompt()` (L697-993) | Assembles the complete prompt from selected atoms |
| `main()` (L1005-1370) | Entry point with analytics, violation checking, and output |

**Key Features:**
- Distance-aware atom filtering (close/medium/full_body)
- Theme-locked slot selection
- Ensemble pool-based randomization
- Camera-embellishment coordination
- Duplicate detection
- Mandate checkpoint verification

**Debug Flag (L65):**
```python
DEBUG_FORCE_CLOSE_CAMERA = "medium"  # Can be False, "close", "medium", "full_body"
```

---

### 2. `analytics.py` - Token Analysis

**Purpose:** Provides accurate token counting and efficiency analysis.

**Key Functions:**
- `count_tokens()` - Uses tiktoken for accurate GPT tokenization
- `analyze_definitions()` - Analyzes all atom files for token usage
- `run_analytics()` - Generates comprehensive analysis report

**Reports:**
- Token budget status
- Priority breakdown (P0/P1/P2)
- Heaviest files by token count
- Narrative language violations
- Character limit violations
- Efficiency metrics (tokens per character)

---

### 3. `violation_reporter.py` - Compliance Checker

**Purpose:** Ensures atoms follow project writing standards.

**Detected Violations:**
1. **Narrative Language** - Words like "shows", "creates", "demonstrates", "appears"
2. **Filter-Risk Language** - Words like "exhausted", "resigned", "vacant" → safe replacements
3. **Character Limits** - Atoms over 300 characters
4. **Token-Heavy Atoms** - Atoms over 80 tokens

**Output:** Generates `VIOLATION_DETAIL_REPORT.md`

---

### 4. `layer_slot_schema.json` - System Architecture

**Purpose:** Defines the layered structure of prompt generation.

**Structure:**
```
Layers (spatial order):
├── ENSEMBLE_VISION (0)        # Theme selection
├── THEME_SIGNATURES (0.5)     # Theme-specific elements
├── STYLE_FOUNDATION (2)       # Core art style mandates
├── CHARACTER_AGE_SAFETY (1.5) # Adult age enforcement
├── CHARACTER_CORE (2)         # Identity, skin, face, makeup, hair
├── EXPRESSION_EMOTION (3)     # Gaze and expression
├── ILLNESS_STATE (4)          # Fatigue/illness markers
├── POSE_BODY (5)              # Stance and body language
├── HAIR_ACCESSORIES (6)       # Hair clips, bows
├── HAIR_STYLING (7)           # Salon styling
├── COUTURE_DRESS (8)          # Dress construction (largest)
├── ACCESSORIES (9)            # Hosiery, footwear
├── SCENE_ENVIRONMENT (10)     # Room, lighting, camera
├── SCENE_DISSONANCE (10.5)    # Beauty vs. breakdown tension
├── CHARACTER_AGE_SAFETY_LATE (11.5) # Age reinforcement
├── STYLE_CHECKPOINT (11)      # Style reminders
└── STYLE_FINAL (12)           # Closing style enforcement
```

**Slot Properties:**
- `include_prefixes` - Which atom keys to include
- `exclude_prefixes` - Which atom keys to exclude
- `min_atoms`/`max_atoms` - Quantity constraints
- `theme_locked` - Requires theme matching
- `theme_dependent` - Uses ensemble theme preferences

---

### 5. Definition Files (definitions/)

**Core Definition Files:**

| File | Purpose | Atom Count |
|------|---------|------------|
| `style_enforcement.json` | Art style mandates | ~20 |
| `character_core.json` | Character identity | ~20 |
| `character_age_safety.json` | Adult age enforcement | ~4 |
| `illness_manifestations.json` | Fatigue/exhaustion visuals | ~4 |
| `dress_ensembles.json` | 8 thematic ensembles | 8 |
| `shiny_embellishments.json` | D0/D1 embellishments | ~30 |
| `dress_colors.json` | Color palette | ~10 |
| `couture_construction.json` | Dress construction | ~30 |
| `scene_lighting.json` | Environment/lighting | ~15 |
| `camera_angles_close.json` | Camera positions | ~10 |

**Atom Metadata Fields:**
```json
{
  "domain": "STYLE|CHARACTER|DRESS|SCENE",
  "tier": 0-2,
  "priority": "P0: MANDATE|P1: CORE|P2: DETAIL",
  "group": "D0_Core|D1_Architectural|mandate|...",
  "random": true|false,
  "theme_tags": ["crystalline", "sparkle"],
  "theme_locked": "crystalline_sparkle",
  "requires": ["other.atom.key"],
  "excludes": ["conflicting.atom.key"],
  "min_visible_distance": "close|medium|full_body",
  "max_visible_distance": "close|medium|full_body",
  "placement": "bodice_center|shoulder|head|...",
  "contents": "The actual prompt text"
}
```

---

### 6. Ensemble System

**Purpose:** Creates thematic coherence across all dress elements.

**8 Ensemble Themes:**
1. `crystalline_sparkle` - Maximum light-catching brilliance
2. `romantic_floral` - Garden elegance, dimensional flowers
3. `bow_devotion` - Ribbon obsession, bow clusters
4. `refined_elegance` - Understated luxury, pearls
5. `lace_heirloom` - Delicate precision, vintage
6. `glitter_abundance` - Layered sparkle saturation
7. `gingham_tradition` - Classic check aesthetic
8. `celestial_fantasy` - Night sky elegance

**Each Ensemble Contains:**
- `embellishment_pool` - Compatible embellishments
- `pattern_pool` - Compatible patterns
- `fabric_pool` - Compatible fabrics
- `tailoring_pool` - Compatible tailoring details
- `hair_accessory_pool` - Compatible hair accessories
- `hosiery_pool` - Compatible hosiery
- `embellishment_focus` - Keywords for theme filtering

---

### 7. Priority System

| Priority | Name | Purpose | Protected |
|----------|------|---------|-----------|
| P0 | MANDATE | Non-negotiable atoms (age safety, style, dissonance) | Yes |
| P1 | CORE | Main content (dress, expression, pose) | Trim last |
| P2 | DETAIL | Optional enhancements (accessories) | Trim first |

---

### 8. Group System

| Group | Role | Slot Assignment |
|-------|------|-----------------|
| `D1_Architectural` | PRIMARY embellishment (one big thing) | `theme_embellishment_primary` |
| `D1_Hair_Architectural` | PRIMARY hair statement (close-camera only) | `theme_embellishment_primary` |
| `D0_Core` | COMPLEMENTARY details (subtle accents) | `dress.embellishments` |
| `mandate` | Protected style atoms | `style.core_mandate` |

---

### 9. Distance-Aware Filtering

**Camera Distances:**
- `close` - Face/makeup documentation (3-5ft)
- `medium` - Upper body/bodice (5-8ft)
- `full_body` - Complete figure (8-12ft)

**Filtering Logic:**
- `min_visible_distance: "medium"` = Only shows at medium or farther
- `max_visible_distance: "close"` = Only shows at close distance
- No metadata = Shows at all distances

**Slot Skipping by Distance:**
- Close-ups skip: hosiery, footwear, silhouette, skirt, petticoat, pattern
- Medium shots skip: hosiery, footwear, petticoat

---

## Utility Scripts

### `theme_diagnostic.py`
Checks theme coordination between ensembles and atom tags.

### `development_protocols.py`
Testing suite for:
- Slot contamination detection
- Group assignment verification
- Multiple generation variety testing

### `manifest.py`
Creates `project_context.md` snapshot of entire codebase.

### Auxiliary Scripts (in root):
- `analyze_tokens.py` - Token analysis
- `audit_distance_metadata.py` - Distance metadata audit
- `compress_prissy.py` - Atom compression
- `prune_atoms.py` - Unused atom removal
- `remove_unicode.py` - Unicode character cleanup
- `replace_victorian.py` - Language replacement
- `theme_signature_audit.py` - Theme signature verification

---

## Proposed Improvements

### High Priority

#### 1. **Code Architecture Improvements**

**a) Extract Atom Selection Logic into Separate Module**
```python
# Create: atom_selector.py
class AtomSelector:
    def __init__(self, atoms, schema, ensemble_prefs):
        ...
    def select_for_slot(self, slot, camera_distance):
        ...
    def filter_by_distance(self, candidates, distance):
        ...
    def filter_by_theme(self, candidates, theme):
        ...
```
*Benefit:* `camera.py` is 1,372 lines. Extracting the ~500 lines of selection logic improves maintainability.

**b) Create Configuration Class**
```python
# Create: config.py
@dataclass
class GenerationConfig:
    token_target: int = 3000
    definitions_dir: str = "definitions"
    debug_camera_lock: Optional[str] = None
    ...
```
*Benefit:* Centralize configuration, reduce magic constants scattered throughout.

**c) Type Hints Throughout**
```python
def select_atoms_for_slot(
    slot: Dict[str, Any],
    all_atoms: Dict[str, Atom],
    ensemble_prefs: Optional[Dict[str, Any]] = None,
    camera_distance: Optional[str] = None
) -> List[Atom]:
```
*Benefit:* Better IDE support, catch bugs earlier, self-documenting code.

---

#### 2. **Validation Improvements**

**a) Schema Validation**
```python
# Add JSON schema validation for definition files
from jsonschema import validate

ATOM_SCHEMA = {
    "type": "object",
    "required": ["contents", "priority"],
    "properties": {
        "contents": {"type": "string", "maxLength": 300},
        "priority": {"enum": ["P0: MANDATE", "P1: CORE", "P2: DETAIL"]},
        ...
    }
}
```
*Benefit:* Catch invalid atoms at load time rather than runtime failures.

**b) Pre-flight Validation**
```python
def validate_system_integrity():
    """Run before generation to catch issues early"""
    issues = []
    # Check all referenced atoms exist
    # Check ensemble pools reference valid atoms
    # Check required_atoms exist
    # Check no circular excludes/requires
    return issues
```

---

#### 3. **Testing Infrastructure**

**a) Unit Tests**
```python
# tests/test_atom_selection.py
def test_distance_filtering_close():
    atoms = load_test_atoms()
    filtered = filter_by_distance(atoms, "close")
    assert all(a.max_visible_distance != "medium" for a in filtered)

def test_theme_locking():
    ...
```
*Benefit:* Prevent regressions, enable confident refactoring.

**b) Integration Tests**
```python
def test_full_generation_produces_valid_prompt():
    prompt = generate_prompt()
    assert 2800 <= count_tokens(prompt) <= 3200
    assert "ADULT 20-24" in prompt
```

---

### Medium Priority

#### 4. **Documentation Improvements**

**a) Inline Documentation**
- Add docstrings to all functions
- Document the "why" not just the "what"
- Add examples in docstrings

**b) Architecture Decision Records (ADRs)**
Document why certain design decisions were made:
- Why distance-aware filtering?
- Why D0/D1 group separation?
- Why ensemble pools vs fixed combinations?

---

#### 5. **Performance Improvements**

**a) Lazy Loading**
```python
class AtomLibrary:
    _atoms: Optional[Dict[str, Atom]] = None

    @classmethod
    def get_atoms(cls) -> Dict[str, Atom]:
        if cls._atoms is None:
            cls._atoms = load_atoms()
        return cls._atoms
```
*Benefit:* Faster startup when running multiple generations.

**b) Caching**
```python
@functools.lru_cache(maxsize=100)
def count_tokens(text: str) -> int:
    return len(encoding.encode(text))
```

---

#### 6. **Error Handling Improvements**

**Current:** Bare `except:` clauses throughout
```python
try:
    import tiktoken
except:  # Too broad!
    pass
```

**Improved:**
```python
try:
    import tiktoken
    encoding = tiktoken.get_encoding("cl100k_base")
except ImportError:
    logger.warning("tiktoken not installed, using estimation")
    encoding = None
except Exception as e:
    logger.error(f"Unexpected tiktoken error: {e}")
    encoding = None
```

---

### Lower Priority

#### 7. **Observability Improvements**

**a) Structured Logging**
```python
import logging
logger = logging.getLogger(__name__)

logger.info("Generating prompt", extra={
    "ensemble": ensemble_name,
    "camera_distance": camera_distance,
    "token_target": TOKEN_TARGET
})
```

**b) Metrics Export**
Export generation metrics to Prometheus/Grafana format for trend analysis.

---

#### 8. **CLI Improvements**

**Current:** Only `python camera.py`

**Improved:**
```bash
python camera.py generate --distance=close --theme=crystalline
python camera.py analyze --file=prompt.txt
python camera.py validate --all
python camera.py stats
```

Using `argparse` or `click` for proper CLI interface.

---

#### 9. **Definition File Organization**

**Current:** Flat structure with 28+ files

**Consider:**
```
definitions/
├── character/
│   ├── core.json
│   ├── age_safety.json
│   └── illness.json
├── style/
│   ├── enforcement.json
│   └── checkpoints.json
├── dress/
│   ├── colors.json
│   ├── construction.json
│   ├── patterns.json
│   └── embellishments.json
└── scene/
    ├── lighting.json
    └── cameras.json
```
*Benefit:* Easier navigation, clearer ownership.

---

## Summary of Key Files

| File | Lines | Complexity | Purpose |
|------|-------|------------|---------|
| `camera.py` | 1,372 | High | Main generator |
| `analytics.py` | 329 | Medium | Token analysis |
| `violation_reporter.py` | 271 | Medium | Compliance checking |
| `generation_analytics.py` | 387 | Medium | History tracking |
| `layer_slot_schema.json` | 759 | High | System architecture |
| `config.json` | 199 | Low | Legacy config |
| `definitions/*.json` | ~3000+ | Medium | Atom definitions |

---

## Conclusion

ModelA is a well-designed prompt generation system with sophisticated features for thematic coherence, distance-aware filtering, and compliance checking. The main opportunities for improvement are:

1. **Code organization** - Breaking up the large `camera.py`
2. **Type safety** - Adding type hints and validation
3. **Testing** - Adding automated tests
4. **Error handling** - More specific exception handling

The system successfully achieves its goal of generating consistent, high-quality prompts for AI image generation with a specific artistic vision.
