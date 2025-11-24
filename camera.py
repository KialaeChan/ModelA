#!/usr/bin/env python3
"""
ModelA v2 - Realistic Digital Rendering Generator
Focus: Realism enforcement, couture detail, emotional storytelling
NO anatomical jargon, NO 3D rigging terms
"""

import os
import json
import random
import sys
import subprocess
from typing import Dict, List

# Try to import tiktoken for accurate token counting
TIKTOKEN_AVAILABLE = False
encoding = None

try:
    import tiktoken
    encoding = tiktoken.get_encoding("cl100k_base")  # GPT-3.5/4 encoding
    TIKTOKEN_AVAILABLE = True
except ImportError as e:
    # Try alternative import path for Windows compatibility
    try:
        from tiktoken import get_encoding
        encoding = get_encoding("cl100k_base")
        TIKTOKEN_AVAILABLE = True
    except Exception as e2:
        pass
except Exception as e:
    # Catch other potential errors
    pass

# Import analytics toolkit
try:
    from analytics import run_analytics, TIKTOKEN_AVAILABLE as ANALYTICS_TIKTOKEN
except ImportError:
    run_analytics = None
    ANALYTICS_TIKTOKEN = False
except Exception as e:
    print(f"Warning: Unexpected error importing analytics: {e}")
    run_analytics = None
    ANALYTICS_TIKTOKEN = False

# Import generation tracking
try:
    from generation_analytics import track_generation, print_analytics_dashboard
except ImportError:
    track_generation = None
    print_analytics_dashboard = None
except Exception as e:
    print(f"Warning: Unexpected error importing generation_analytics: {e}")
    track_generation = None
    print_analytics_dashboard = None

# Import violation reporter
try:
    from violation_reporter import ViolationAnalyzer
except ImportError:
    ViolationAnalyzer = None
except Exception as e:
    print(f"Warning: Unexpected error importing violation_reporter: {e}")
    ViolationAnalyzer = None

# Configuration
DEFINITIONS_DIR = "definitions"
SCHEMA_FILE = "layer_slot_schema.json"
OUTPUT_FILE = "prompt.txt"
TOKEN_TARGET = 3000

# ═══════════════════════════════════════════════════════════════════
# DEBUG: CAMERA DISTANCE LOCK
# Options: False (normal), "close", "medium", "full_body"
# Set to specific distance to force that camera distance for testing
DEBUG_FORCE_CLOSE_CAMERA = "medium"
# ═══════════════════════════════════════════════════════════════════

# Preamble - FRAMING MUST BE FIRST, THEN STYLE/CHARACTER
PREAMBLE_CAMERA_FIRST = """AMATEUR SNAPSHOT. Casual documentation. VERTICAL FORMAT - 9:16 aspect ratio, portrait orientation. VIEWER STANDING (6'1"), SUBJECT SHORTER (5'1"). OVERHEAD DOWNWARD ANGLE. Perspective pointing DOWN at upturned face. Hasty casual capture."""

PREAMBLE_BODY = """
CRITICAL: Head oriented toward focus. Eyes directed AT focal point, pupils aimed at point of focus. BUT focal depth set beyond focus - staring through focal point rather than at it. Direction mechanically correct, engagement absent. Gaze alignment appears aimed at viewer but focal depth wrong. Eyes converging on focal point but focused far beyond it.

ADULT 20-24 YEARS OLD - LEGALLY ADULT, COMPLETELY MATURE. Realistic adult proportions: 7+ heads tall, mature facial structure, adult features, defined mandible, prominent cheekbones, mature skull geometry. Adult face with mature bone structure. Looks distinctly adult.

UNPROFESSIONAL SNAPSHOT: Hasty careless framing. Utilitarian capture without compositional care. Raw snapshot. Zero skill. First take only. Snapshot quality.

MANGA PAINTER RENDERING REALISTIC ANATOMY. Manga artist painting real person under harsh overhead institutional light. Fine anatomical detail with sharp light-shadow contrast. Manga painter sensibility applied to realistic proportions and anatomy. Smooth painted surfaces with clean color transitions - NOT cel-shading, NOT linework, NOT brushy watercolor. Harsh white-blue LED (6000-7000K) casting sharp downward shadows. COLD CLINICAL LIGHT - NOT warm, NOT golden, NOT flattering. Painted illustration with stark grim subject matter."""





class Atom:
    def __init__(self, key: str, data: dict):
        self.key = key
        self.contents = data.get("contents", "")
        self.domain = data.get("domain", "UNKNOWN")
        self.priority = data.get("priority", "P2: DETAIL")
        self.random = data.get("random", False)
        self.group = data.get("group", "")
        self.theme_tags = data.get("theme_tags", [])  # NEW: Support theme metadata
        self.theme_locked = data.get("theme_locked", None)  # NEW: Theme this atom is locked to
        self.requires = data.get("requires", [])  # NEW: Atoms this one requires
        self.excludes = data.get("excludes", [])  # NEW: Atoms this one excludes
        self.placement = data.get("placement", None)  # NEW: Where embellishment is located
        self.visibility_angles = data.get("visibility_angles", [])  # NEW: Which camera angles show it
        self.min_visible_distance = data.get("min_visible_distance", None)  # NEW: Camera distance needed for this atom to be visible
        self.max_visible_distance = data.get("max_visible_distance", None)  # NEW: Maximum camera distance for this atom
        self.distance = data.get("distance", None)  # NEW: Camera distance (for camera atoms)
        self.reveals = data.get("reveals", [])  # NEW: What camera reveals (for camera atoms)
        
    def get_tokens(self) -> int:
        if TIKTOKEN_AVAILABLE:
            try:
                return len(encoding.encode(self.contents))
            except (AttributeError, TypeError) as e:
                # Fallback if encoding fails or contents is invalid
                return len(self.contents) // 4
        else:
            return len(self.contents) // 4

def load_atoms() -> Dict[str, Atom]:
    """Load all atoms from definition files"""
    atoms = {}
    definitions_path = os.path.join(os.path.dirname(__file__), DEFINITIONS_DIR)
    
    for filename in os.listdir(definitions_path):
        if not filename.endswith('.json'):
            continue
            
        filepath = os.path.join(definitions_path, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        for key, atom_data in data.items():
            atoms[key] = Atom(key, atom_data)
    
    return atoms

def coordinate_camera_with_embellishment(primary_embellishment: Atom, camera_atoms: List[Atom]) -> List[Atom]:
    """
    Filter camera angles based on primary embellishment placement and visibility needs.
    Ensures the camera angle will show the PRIMARY embellishment effectively.
    
    SPECIAL CASE: Hair primaries (D1_Hair_Architectural) ONLY work with close cameras.
    """
    if not primary_embellishment:
        return camera_atoms
    
    # Get embellishment placement info
    placement = getattr(primary_embellishment, 'placement', None)
    min_distance = getattr(primary_embellishment, 'min_visible_distance', 'medium')
    visibility_angles = getattr(primary_embellishment, 'visibility_angles', [])
    is_hair_primary = getattr(primary_embellishment, 'group', '') == 'D1_Hair_Architectural'
    
    # If no placement info, return all cameras
    if not placement and not visibility_angles:
        print(f"    ⚠ No placement metadata for {primary_embellishment.key}")
        return camera_atoms
    
    print(f"    🎯 Coordinating camera for {placement} placement, needs {min_distance} distance")
    if is_hair_primary:
        print(f"    💇 Hair primary: STRICT close-camera requirement")
    
    # Filter cameras based on embellishment needs
    suitable_cameras = []
    
    for camera in camera_atoms:
        # Check if camera has reveals metadata
        camera_reveals = getattr(camera, 'reveals', [])
        camera_distance = getattr(camera, 'distance', 'medium')
        camera_angle = getattr(camera, 'viewing_angle', None)
        
        # Use metadata if available, fallback to content parsing
        if camera_reveals:
            # Check if camera reveals the embellishment placement
            placement_visible = False
            
            # Direct placement match
            if placement in camera_reveals:
                placement_visible = True
            # Check special cases
            elif placement == 'bodice_center' and 'front' in camera_reveals:
                placement_visible = True
            elif placement == 'shoulder' and ('front' in camera_reveals or 'side' in camera_reveals):
                placement_visible = True
            elif placement == 'diagonal_side' and ('side' in camera_reveals or 'front' in camera_reveals):
                placement_visible = True
            elif placement == 'circumference' and len(camera_reveals) > 1:  # Circumference visible from multiple angles
                placement_visible = True
            elif placement == 'skirt' and ('front' in camera_reveals or 'side' in camera_reveals):
                placement_visible = True
            elif placement == 'head' or placement == 'side_head':  # Hair placement special handling
                # Head placement visible from most angles except back
                if 'back' not in camera_reveals:
                    placement_visible = True
            
            if not placement_visible:
                continue
            
            # STRICT distance requirement for hair primaries
            if is_hair_primary:
                # Hair primaries ONLY work with close cameras
                if camera_distance != 'close':
                    continue  # Skip non-close cameras
            else:
                # Check distance compatibility with metadata - HIERARCHICAL MATCHING
                # Embellishment requires minimum distance, closer cameras can also show it
                # Hierarchy: close can show everything, medium can show medium+full_body, full_body shows only full_body
                distance_hierarchy = {'close': 0, 'medium': 1, 'full_body': 2}
                required_level = distance_hierarchy.get(min_distance, 1)
                camera_level = distance_hierarchy.get(camera_distance, 1)
                
                # Camera must be at least as close as (or closer than) required distance
                if camera_level > required_level:
                    continue  # Camera too far for this embellishment
            
        else:
            # Fallback to content parsing for cameras without metadata
            camera_content = camera.contents.lower()
            
            # Check distance compatibility
            if min_distance == 'close' and ('8-10 feet' in camera_content or 'far' in camera_content):
                continue
            elif min_distance == 'full_body' and ('4-5 feet' in camera_content or 'close' in camera_content):
                continue
            
            # Check angle compatibility with placement
            if placement == 'back' and 'back' not in camera_content:
                continue
            elif placement == 'front' and 'back' in camera_content:
                continue
        
        suitable_cameras.append(camera)
    
    print(f"    📷 Found {len(suitable_cameras)}/{len(camera_atoms)} suitable cameras")
    
    # If we filtered too aggressively and have no cameras, we need to handle this properly
    if not suitable_cameras:
        print(f"    ⚠ No suitable cameras for {placement} placement at {min_distance} distance")
        print(f"    🔄 Need to select different primary embellishment")
        # Return empty list to signal need for re-selection
        return []
    
    return suitable_cameras

def load_schema() -> dict:
    """Load the slot schema"""
    schema_path = os.path.join(os.path.dirname(__file__), SCHEMA_FILE)
    with open(schema_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def match_atom_to_slot(atom: Atom, slot: dict, all_atoms: Dict[str, Atom]) -> bool:
    """Check if atom matches slot prefixes and doesn't match exclude_prefixes"""
    prefixes = slot.get("include_prefixes", [])
    exclude_prefixes = slot.get("exclude_prefixes", [])
    
    # Check if excluded
    for exclude_prefix in exclude_prefixes:
        if atom.key.startswith(exclude_prefix):
            return False
    
    # Check if included
    for prefix in prefixes:
        if atom.key.startswith(prefix):
            return True
    
    return False

def select_atoms_for_slot(slot: dict, all_atoms: Dict[str, Atom], ensemble_prefs: dict = None, ensemble_pools: dict = None, previously_selected: List[Atom] = None, camera_distance: str = None, exclude_atoms: List[Atom] = None) -> List[Atom]:
    """Select atoms for a slot based on priority and randomization
    
    If ensemble_pools provided, picks randomly from compatible pools for that slot type.
    Otherwise uses ensemble preferences for filtered selection.
    
    If camera_distance provided, filters atoms based on min_visible_distance metadata.
    """
    import random
    
    # Debug makeup selection
    if slot and "makeup" in slot.get("slot_id", ""):
        print(f"    🔍 Selecting atoms for makeup slot with camera_distance={camera_distance}")
    
    # Find all matching atoms
    candidates = []
    for atom in all_atoms.values():
        if match_atom_to_slot(atom, slot, all_atoms):
            candidates.append(atom)
    
    if not candidates:
        return []
    
    # Exclude atoms that were already attempted and failed
    if exclude_atoms:
        candidates = [c for c in candidates if c not in exclude_atoms]
        if not candidates:
            return []
    
    # THEME SIGNATURES: Filter by selected theme if slot is theme-dependent
    if slot.get("theme_dependent") and ensemble_prefs:
        theme_name = ensemble_prefs.get("theme", "")
        if theme_name:
            theme_filtered = []
            for atom in candidates:
                # Check if atom is theme-locked to current theme
                if hasattr(atom, 'theme_locked') and atom.theme_locked == theme_name:
                    theme_filtered.append(atom)
            
            if theme_filtered:
                candidates = theme_filtered
                # For signatures, return all 5 signature types
                if "signature" in slot.get("slot_id", ""):
                    print(f"    🎨 Theme signatures found: {len(theme_filtered)} for theme {theme_name}")
                    return theme_filtered  # Return all signatures for this theme
            else:
                # No signatures for this theme
                if "signature" in slot.get("slot_id", ""):
                    print(f"    ⚠ No signatures found for theme: {theme_name}")
                return []
    
    # NEW: Filter candidates by camera distance if provided
    if camera_distance:
        original_count = len(candidates)
        distance_compatible = []
        for atom in candidates:
            atom_min_distance = getattr(atom, 'min_visible_distance', None)
            atom_max_distance = getattr(atom, 'max_visible_distance', None)
            
            # If atom has no distance metadata, include it (backward compatibility)
            if not atom_min_distance and not atom_max_distance:
                distance_compatible.append(atom)
                continue
            
            # Define distance hierarchy: close < medium < full_body
            distance_order = {'close': 0, 'medium': 1, 'full_body': 2}
            current_distance_level = distance_order.get(camera_distance, 1)
            
            # Check min_visible_distance (closest distance atom can appear at)
            include_atom = True
            if atom_min_distance:
                min_level = distance_order.get(atom_min_distance, 0)
                # If camera is closer than atom's minimum, exclude it
                if current_distance_level < min_level:
                    include_atom = False
            
            # Check max_visible_distance (farthest distance atom can appear at)
            if atom_max_distance:
                max_level = distance_order.get(atom_max_distance, 2)
                # If camera is farther than atom's maximum, exclude it
                if current_distance_level > max_level:
                    include_atom = False
            
            if include_atom:
                distance_compatible.append(atom)
        
        # Update candidates to distance-filtered set
        if distance_compatible:
            filtered_count = len(distance_compatible)
            if filtered_count < original_count:
                # Only log when we actually filtered something
                slot_id = slot.get("slot_id", "unknown")
                print(f"    🔍 Distance filter ({camera_distance}): {original_count} → {filtered_count} atoms for {slot_id}")
                # Debug makeup filtering results
                if "makeup" in slot_id:
                    print(f"    📄 After distance filter, makeup candidates are:")
                    for atom in distance_compatible:
                        print(f"      - {atom.key}")
            candidates = distance_compatible
        # If we filtered out everything, keep original candidates (don't break generation)
    
    # NEW: Filter out atoms that are excluded by previously selected atoms
    if previously_selected:
        selected_keys = [a.key for a in previously_selected]
        # Collect all exclusions from previously selected atoms
        excluded_by_previous = []
        for selected_atom in previously_selected:
            if hasattr(selected_atom, 'excludes'):
                excluded_by_previous.extend(selected_atom.excludes)
        
        # Filter out excluded candidates
        if excluded_by_previous:
            original_count = len(candidates)
            candidates = [a for a in candidates if a.key not in excluded_by_previous]
            filtered_count = len(candidates)
            if filtered_count < original_count:
                slot_id = slot.get("slot_id", "unknown")
                print(f"    🚫 Exclusion filter: {original_count} → {filtered_count} atoms for {slot_id}")
    
    # NEW: Handle mutual exclusion WITHIN candidates (for distance variants)
    # If multiple candidates exclude each other, keep only the best one for current camera distance
    if camera_distance and len(candidates) > 1:
        # Build exclusion map: which atoms exclude which
        exclusion_map = {}
        for atom in candidates:
            if hasattr(atom, 'excludes') and atom.excludes:
                exclusion_map[atom.key] = atom.excludes
        
        # Find mutually exclusive groups
        if exclusion_map:
            distance_order = {'close': 0, 'medium': 1, 'full_body': 2}
            current_distance_level = distance_order.get(camera_distance, 1)
            
            # Track which atoms we've already processed (chosen or excluded)
            processed_keys = set()
            filtered_candidates = []
            
            for atom in candidates:
                # Skip if already processed as part of another exclusion group
                if atom.key in processed_keys:
                    continue
                
                # Check if this atom excludes any other candidates
                if hasattr(atom, 'excludes') and atom.excludes:
                    competing_atoms = [a for a in candidates 
                                      if a.key in atom.excludes and a.key not in processed_keys]
                    
                    if competing_atoms:
                        # Choose the atom most appropriate for current distance
                        all_variants = [atom] + competing_atoms
                        
                        # Score each variant by distance appropriateness
                        def distance_score(a):
                            a_min = getattr(a, 'min_visible_distance', None)
                            a_max = getattr(a, 'max_visible_distance', None)
                            
                            if a_min and not a_max:
                                min_level = distance_order.get(a_min, 0)
                                return abs(current_distance_level - min_level)
                            elif a_max and not a_min:
                                max_level = distance_order.get(a_max, 2)
                                return abs(current_distance_level - max_level)
                            elif a_min and a_max:
                                min_level = distance_order.get(a_min, 0)
                                max_level = distance_order.get(a_max, 2)
                                if min_level <= current_distance_level <= max_level:
                                    return 0
                                else:
                                    return min(abs(current_distance_level - min_level), 
                                             abs(current_distance_level - max_level))
                            else:
                                return 999  # No distance preference
                        
                        # Pick the variant with best distance score
                        best_variant = min(all_variants, key=distance_score)
                        filtered_candidates.append(best_variant)
                        
                        # Mark all variants in this group as processed
                        for variant in all_variants:
                            processed_keys.add(variant.key)
                    else:
                        # No competing atoms (they were already processed), include this one
                        filtered_candidates.append(atom)
                        processed_keys.add(atom.key)
                else:
                    # No exclusions, include this atom
                    filtered_candidates.append(atom)
                    processed_keys.add(atom.key)
            
            if len(filtered_candidates) < len(candidates):
                slot_id = slot.get("slot_id", "unknown")
                print(f"    ⚖️ Mutual exclusion resolved: {len(candidates)} → {len(filtered_candidates)} atoms for {slot_id}")
                candidates = filtered_candidates
    
    # NEW: For "theme_embellishment_primary" slot, select ONLY D1_Architectural signature atoms OR D1_Hair_Architectural
    if slot.get("slot_id") == "theme_embellishment_primary":
        candidates = [
            a for a in candidates 
            if hasattr(a, 'group') 
            and (a.group == 'D1_Architectural' or a.group == 'D1_Hair_Architectural')
        ]
        # If no D1_Architectural/D1_Hair_Architectural atoms available, return empty (don't contaminate with D0_Core)
        if not candidates:
            return []
    
    # NEW: For "dress.embellishments" slot, select ONLY D0_Core complementary details
    if slot.get("slot_id") == "dress.embellishments":
        # Track what was already selected as theme_embellishment_primary
        excluded_keys = []
        if previously_selected:
            for selected_atom in previously_selected:
                # Exclude any architectural embellishment that was already selected (dress OR hair)
                if (selected_atom.key.startswith("embellish.") or selected_atom.key.startswith("hair.primary.")) and \
                   hasattr(selected_atom, 'group') and \
                   (selected_atom.group == 'D1_Architectural' or selected_atom.group == 'D1_Hair_Architectural'):
                    excluded_keys.append(selected_atom.key)
        
        # Filter to ONLY D0_Core atoms (the subtle complements)
        # Exclude any D1_Architectural/D1_Hair_Architectural atoms and any already-selected atoms
        candidates = [
            a for a in candidates 
            if hasattr(a, 'group') 
            and a.group == 'D0_Core' 
            and a.key not in excluded_keys
        ]
        
        # If no D0_Core atoms available, use empty list (better than duplicating architectural)
        if not candidates:
            candidates = []
    
    # NEW: Filter candidates based on 'requires' field (for other atoms that require something)
    if previously_selected and not (slot.get("slot_id") == "dress.embellishments"):
        selected_keys = [a.key for a in previously_selected]
        filtered_by_requires = []
        for atom in candidates:
            requires = atom.requires if hasattr(atom, 'requires') else []
            if requires:
                # If atom has requirements, check if all are met
                if all(req in selected_keys for req in requires):
                    filtered_by_requires.append(atom)
            else:
                # If atom has no requirements, include it
                filtered_by_requires.append(atom)
        
        if filtered_by_requires:
            candidates = filtered_by_requires
    
    # NEW: If we have ensemble pools and this slot type is in pools, pick randomly from pool
    # EXCEPT for dress.embellishments which should only use D0_Core atoms (already filtered above)
    slot_id = slot.get("slot_id", "")
    if ensemble_pools and slot_id != "dress.embellishments":
        # Map slot types to pool keys
        pool_mapping = {
            "embellish": "embellishment_pool",
            "pattern": "pattern_pool",
            "fabric": "fabric_pool",
            "tailoring": "tailoring_pool",
            "hair.accessories": "hair_accessory_pool",
            "hosiery": "hosiery_pool"
        }
        
        # Find which pool this slot belongs to
        pool_key = None
        for slot_type, pool_name in pool_mapping.items():
            if slot_type in slot_id:
                pool_key = pool_name
                break
        
        # If we found a matching pool, pick randomly from it
        if pool_key and pool_key in ensemble_pools:
            pool_atom_keys = ensemble_pools[pool_key]
            
            # Filter to atoms that actually exist and match the slot
            valid_atoms = []
            for atom_key in pool_atom_keys:
                if atom_key in all_atoms and match_atom_to_slot(all_atoms[atom_key], slot, all_atoms):
                    valid_atoms.append(all_atoms[atom_key])
            
            if valid_atoms:
                # Pick one randomly
                return [random.choice(valid_atoms)]
    
    # FALLBACK: If this is a pattern/color/embellishment slot and we have ensemble preferences, filter candidates
    if ensemble_prefs and slot_id:
        # For pattern slots, prefer ensemble pattern_preference
        if "pattern" in slot_id and "pattern_preference" in ensemble_prefs:
            filtered = []
            for atom in candidates:
                # Check if atom contains any of the preferred pattern keywords
                for pattern_pref in ensemble_prefs.get("pattern_preference", []):
                    if pattern_pref.lower() in atom.key.lower():
                        filtered.append(atom)
            if filtered:
                candidates = filtered
        
        # For color slots, prefer ensemble color_preference
        elif "color" in slot_id and "color_preference" in ensemble_prefs:
            filtered = []
            for atom in candidates:
                # Check if atom contains any of the preferred color keywords
                for color_pref in ensemble_prefs.get("color_preference", []):
                    if color_pref.lower() in atom.key.lower():
                        filtered.append(atom)
            if filtered:
                candidates = filtered
        
        # For embellishment slots, prefer ensemble embellishment_focus
        elif "embellish" in slot_id and "embellishment_focus" in ensemble_prefs:
            filtered = []
            for atom in candidates:
                # Check if atom contains any of the embellishment focus keywords
                # ENHANCED: Check BOTH key AND theme_tags fields
                for emb_focus in ensemble_prefs.get("embellishment_focus", []):
                    atom_tags = [t.lower() for t in atom.theme_tags] if hasattr(atom, 'theme_tags') else []
                    
                    # Check keyword in atom key or as substring in any tag
                    if (emb_focus.lower() in atom.key.lower() or 
                        any(emb_focus.lower() in tag for tag in atom_tags)):
                        filtered.append(atom)
                        break  # Don't add same atom twice for multiple keyword matches
            
            if filtered:
                candidates = filtered
            else:
                # Log warning if no theme atoms found, but don't fail silently
                print(f"⚠ No atoms matched embellishment_focus for {slot_id}: {ensemble_prefs.get('embellishment_focus', [])}")
    
    # NEW: Handle theme-locked slots - MUST only return theme-matching atoms
    if slot.get("theme_locked") and ensemble_prefs:
        theme_atoms = []
        emb_focus = ensemble_prefs.get("embellishment_focus", [])
        
        for atom in candidates:
            for keyword in emb_focus:
                # Check if keyword is in atom key OR matches any theme tag (case-insensitive)
                atom_tags = [t.lower() for t in atom.theme_tags] if hasattr(atom, 'theme_tags') else []
                
                # Check if keyword appears in atom key
                keyword_in_key = keyword.lower() in atom.key.lower()
                
                # Check if keyword appears in ANY theme tag (as substring)
                keyword_in_tags = any(keyword.lower() in tag for tag in atom_tags)
                
                if keyword_in_key or keyword_in_tags:
                    theme_atoms.append(atom)
                    break
        
        if theme_atoms:
            candidates = theme_atoms
            print(f"✓ Theme-locked slot '{slot_id}': Found {len(candidates)} theme atoms")
        else:
            print(f"⚠ Theme-locked slot '{slot_id}': NO theme atoms found, using full pool as fallback")
    
    # Separate by priority and random status
    mandatory = [a for a in candidates if "P0" in a.priority]
    core = [a for a in candidates if "P1" in a.priority]
    detail = [a for a in candidates if "P2" in a.priority or "P3" in a.priority]
    
    selected = []
    
    # Always include mandatory
    selected.extend(mandatory)
    
    # NEW: Handle required_atoms - specific atoms that must appear in this slot
    required_atom_keys = slot.get("required_atoms", [])
    if required_atom_keys:
        for req_key in required_atom_keys:
            # Find the atom in candidates
            req_atom = next((a for a in candidates if a.key == req_key), None)
            if req_atom and req_atom not in selected:
                selected.append(req_atom)
    
    
    # Get min/max from slot
    min_atoms = slot.get("min_atoms", 1)
    max_atoms = slot.get("max_atoms", 3)
    
    # DISTANCE-AWARE MAX_ATOMS: Increase makeup detail for close-ups
    slot_id = slot.get("slot_id", "")
    if slot_id == "character.makeup_detail" and camera_distance == "close":
        max_atoms = 15  # Load ALL close-distance makeup atoms for micro-detail
    
    # Add core atoms
    if len(selected) < max_atoms:
        random_core = [a for a in core if a.random and a not in selected]  # Exclude already-selected
        non_random_core = [a for a in core if not a.random and a not in selected]  # Exclude already-selected
        
        # Respect max_atoms when adding non-random core atoms
        remaining = max_atoms - len(selected)
        if remaining > 0 and non_random_core:
            # If multiple non-random cores, pick one randomly
            if len(non_random_core) > remaining:
                selected.extend(random.sample(non_random_core, remaining))
            else:
                selected.extend(non_random_core[:remaining])
        
        # Randomly select from random core atoms if needed
        remaining = max_atoms - len(selected)
        if remaining > 0 and random_core:
            # For theme_embellishment_primary slot, don't group by atom.group since D1_Architectural 
            # and D1_Hair_Architectural should be treated as equivalent primaries
            if slot.get("slot_id") == "theme_embellishment_primary":
                # Simple random selection without grouping
                selected.extend(random.sample(random_core, min(remaining, len(random_core))))
            else:
                # Group random atoms by group for other slots
                groups = {}
                for atom in random_core:
                    if atom.group not in groups:
                        groups[atom.group] = []
                    groups[atom.group].append(atom)
                
                # Pick one from each group
                for group_atoms in groups.values():
                    if len(selected) < max_atoms:
                        selected.append(random.choice(group_atoms))
    
    # Add detail atoms if still under max
    if len(selected) < max_atoms and detail:
        remaining = max_atoms - len(selected)
        random_detail = [a for a in detail if a.random and a not in selected]  # Exclude already-selected
        if random_detail:
            sample_size = min(remaining, len(random_detail))
            selected.extend(random.sample(random_detail, sample_size))
        else:
            selected.extend(detail[:remaining])
    
    # Ensure we hit minimum
    if len(selected) < min_atoms and candidates:
        remaining_candidates = [a for a in candidates if a not in selected]
        if remaining_candidates:
            need = min_atoms - len(selected)
            additional = random.sample(remaining_candidates, min(need, len(remaining_candidates)))
            selected.extend(additional)
    
    return selected

def build_prompt(all_atoms: Dict[str, Atom], schema: dict, pre_selected_ensemble_atom: Atom = None, pre_determined_camera_distance: str = None, pre_selected_primary_embellishment: Atom = None) -> str:
    """Build the complete prompt
    
    Uses pre-selected ensemble atom to establish coordinated theme preferences,
    then uses those preferences to influence all downstream slot selections.
    
    Uses pre-determined camera distance (from primary embellishment) to filter all atoms
    based on their min_visible_distance metadata.
    
    Uses pre-selected primary embellishment for camera coordination.
    """
    sections = []
    
    # Add preamble with camera-specific framing
    sections.append(PREAMBLE_CAMERA_FIRST)
    sections.append("")
    
    # Insert camera-specific framing based on pre-determined distance
    if pre_determined_camera_distance == "close":
        close_framing = """PROFESSIONAL MAKEUP ARTIST PORTFOLIO SHOT. Cosmetics documentation distance. Beauty photography for makeup demonstration. OVERHEAD DOWNWARD ANGLE. Camera pointing DOWN at upturned face. EXTREME TIGHT CROP focusing on makeup application. Visible area: top of head, face, neck, NECKLINE EDGE. Crop ends at shoulders. Face fills 85-90% of frame.

VISIBLE AT FRAME PERIMETER: Neckline treatment, upper bodice edge, sleeve caps at shoulders. Dress elements visible only at perimeter edge where neck meets shoulders.

CRITICAL EXCLUSIONS - NOT VISIBLE: body below shoulders, chest, torso, arms below shoulder, hands, waist, full bodice, full sleeves. Frame boundary at shoulder line.

Purpose: document makeup work at professional demonstration distance. Outfit provides color context and pretty dress details at neckline perimeter."""
        sections.append(close_framing)
        sections.append("")
    elif pre_determined_camera_distance == "medium":
        medium_framing = """MEDIUM UPPER-BODY PORTRAIT. Frame shows: COMPLETE head and hair, FULL neck and shoulders, COMPLETE upper torso and bodice, WAIST and upper skirt. Bottom of frame CUTS at MID-SKIRT (hip level). Shows waist-to-hip zone. Does NOT show: lower skirt, hem, petticoat layers, legs, feet, floor. Face and upper body fill vertical frame."""
        sections.append(medium_framing)
        sections.append("")
    # For full_body, no additional framing needed - camera atom handles it
    
    sections.append(PREAMBLE_BODY)
    sections.append("")
    
    # TRACK ALL SELECTED ATOMS for requires field checking
    all_selected_atoms = []
    
    # Track selected camera distance for distance-aware atom filtering
    # Use pre-determined distance from primary embellishment if provided
    selected_camera_distance = pre_determined_camera_distance
    
    # Track primary embellishment for camera coordination
    # Use pre-selected embellishment if provided
    primary_embellishment = pre_selected_primary_embellishment
    
    # DUPLICATE DETECTION - Track which atoms appear in which slots
    atom_slot_map = {}  # atom.key -> list of slot_ids
    
    # CHECKPOINT TRACKING - These atoms are CRITICAL to mandate
    checkpoint_tracker = {
        "age_safety_early": [],
        "age_safety_late": [],
        "dissonance": [],
        "style_foundation": []
    }
    
    # Use pre-selected ensemble atom instead of re-selecting
    ensemble_prefs = {}
    ensemble_pools = {}  # NEW: Pool data for random selection
    ensemble_name = ""
    
    if pre_selected_ensemble_atom:
        ensemble_atom = pre_selected_ensemble_atom
        # Extract theme name for assertion
        ensemble_name = ensemble_atom.key.split(".")[-1].replace("_", " ").title()
        # Parse ensemble preferences from atom data
        for atom_key, atom_data in load_atoms().items():
            if atom_key.startswith("ensemble.") and atom_key.split(".")[-1] in ensemble_atom.key:
                # Load full ensemble data with pools
                for def_file in os.listdir(os.path.join(os.path.dirname(__file__), DEFINITIONS_DIR)):
                    if def_file == "dress_ensembles.json":
                        with open(os.path.join(os.path.dirname(__file__), DEFINITIONS_DIR, def_file)) as f:
                            ensemble_data = json.load(f)
                            for key, val in ensemble_data.items():
                                if key == atom_key:
                                    ensemble_prefs = val
                                    # NEW: Extract pool definitions
                                    pool_keys = [
                                        "embellishment_pool",
                                        "pattern_pool",
                                        "fabric_pool",
                                        "tailoring_pool",
                                        "hair_accessory_pool",
                                        "hosiery_pool"
                                    ]
                                    for pool_key in pool_keys:
                                        if pool_key in val:
                                            ensemble_pools[pool_key] = val[pool_key]
                                    break
    else:
        # Fallback: select ensemble if not provided (for backward compatibility)
        for layer in schema.get("layers", []):
            if layer.get("layer_id") == "ENSEMBLE_VISION":
                for slot in layer.get("slots", []):
                    selected_atoms = select_atoms_for_slot(slot, all_atoms)
                    if selected_atoms:
                        ensemble_atom = selected_atoms[0]
                        # Extract theme name for assertion
                        ensemble_name = ensemble_atom.key.split(".")[-1].replace("_", " ").title()
                        # Parse ensemble preferences from atom data
                        for atom_key, atom_data in load_atoms().items():
                            if atom_key.startswith("ensemble.") and atom_key.split(".")[-1] in ensemble_atom.key:
                                # Load full ensemble data with pools
                                for def_file in os.listdir(os.path.join(os.path.dirname(__file__), DEFINITIONS_DIR)):
                                    if def_file == "dress_ensembles.json":
                                        with open(os.path.join(os.path.dirname(__file__), DEFINITIONS_DIR, def_file)) as f:
                                            ensemble_data = json.load(f)
                                            for key, val in ensemble_data.items():
                                                if key == atom_key:
                                                    ensemble_prefs = val
                                                    # NEW: Extract pool definitions
                                                    pool_keys = [
                                                        "embellishment_pool",
                                                        "pattern_pool",
                                                        "fabric_pool",
                                                        "tailoring_pool",
                                                        "hair_accessory_pool",
                                                        "hosiery_pool"
                                                    ]
                                                    for pool_key in pool_keys:
                                                        if pool_key in val:
                                                            ensemble_pools[pool_key] = val[pool_key]
                                                    break
                break
    
    # Process each layer
    for layer in schema.get("layers", []):
        layer_id = layer.get("layer_id")
        layer_title = layer_id.replace("_", " ")
        
        # Collect all slot outputs for this layer first
        layer_contents = []
        
        # Process each slot in layer
        for slot in layer.get("slots", []):
            slot_name = slot.get("name", "Unknown")
            slot_id = slot.get("slot_id", "")
            
            # DISTANCE-GATING: Skip slots based on camera distance
            # Close-ups (face/neck only for makeup) skip everything except neckline edge and colors
            if selected_camera_distance == "close":
                skip_slots_close = [
                    "accessories.hosiery", 
                    "accessories.footwear",
                    "dress.silhouette",  # Full-body shape not visible
                    "dress.skirt",
                    "dress.petticoat", 
                    "dress.fabric",  # Fabric behavior describes skirt flow
                    "dress.embellishments",  # Usually at waist/skirt level
                    "dress.details",  # Construction details often below frame
                    "dress.elegant_details",
                    "dress.pattern"  # Pattern not visible in face/neck only framing
                    # KEEP: neckline (perimeter edge), bodice (shoulder/neckline edge), primary_color, accent_color, hair primaries
                ]
                # Special case: hair primaries ARE visible, dress primaries are NOT
                if slot_id == "theme_embellishment_primary":
                    # Check if pre-selected embellishment is hair-based
                    if pre_selected_primary_embellishment and hasattr(pre_selected_primary_embellishment, 'domain'):
                        if pre_selected_primary_embellishment.domain == 'HAIR_PRIMARY':
                            # Hair primary - keep it, don't skip
                            pass
                        else:
                            # Dress primary - skip it
                            continue
                    else:
                        # No pre-selected embellishment, skip this slot for close-ups
                        continue
                elif slot_id in skip_slots_close:
                    continue  # Skip - not visible in extreme close-up
            
            # Medium shots skip hosiery/footwear/petticoat
            if selected_camera_distance == "medium":
                if slot_id in ["accessories.hosiery", "accessories.footwear", "dress.petticoat", "dress.skirt"]:
                    continue  # Skip - feet/legs/full skirt not visible at medium distance
            
            # Special handling for camera slot - coordinate with primary embellishment
            if slot_id == "scene.camera" and primary_embellishment:
                # Get all camera atoms that match this slot
                camera_candidates = []
                for atom in all_atoms.values():
                    if match_atom_to_slot(atom, slot, all_atoms):
                        camera_candidates.append(atom)
                
                # DISTANCE FILTERING: If camera distance is set (including debug mode), filter cameras
                if selected_camera_distance:
                    original_count = len(camera_candidates)
                    distance_filtered = []
                    for camera in camera_candidates:
                        # Camera atoms have a 'distance' field that indicates what they shoot
                        camera_dist = getattr(camera, 'distance', None)
                        if camera_dist == selected_camera_distance:
                            distance_filtered.append(camera)
                    
                    if distance_filtered:
                        print(f"    🎥 Camera distance filter ({selected_camera_distance}): {original_count} → {len(distance_filtered)} cameras")
                        camera_candidates = distance_filtered
                    else:
                        # If filtering removed everything, keep originals (don't break generation)
                        print(f"    ⚠️  No {selected_camera_distance} cameras found, keeping all {original_count} candidates")
                
                # Apply camera-embellishment coordination
                coordinated_cameras = coordinate_camera_with_embellishment(primary_embellishment, camera_candidates)
                
                # If no suitable cameras, we need a different primary embellishment
                if not coordinated_cameras:
                    print(f"    ❌ Cannot use {primary_embellishment.key} - no suitable cameras")
                    print(f"    🔄 Selecting alternative primary embellishment...")
                    # Mark this primary as unsuitable and select another
                    # For now, just select a random camera as fallback
                    # TODO: Implement proper re-selection of primary
                    selected_atoms = [random.choice(camera_candidates)] if camera_candidates else []
                else:
                    selected_atoms = [random.choice(coordinated_cameras)]
            else:
                # Normal slot selection with camera distance filtering
                
                # Debug theme signatures
                if slot_id == "theme.signatures":
                    print(f"    📝 Processing theme.signatures slot")
                    print(f"    📝 Ensemble theme: {ensemble_prefs.get('theme', 'NONE') if ensemble_prefs else 'NO PREFS'}")
                
                # Skip sleeve slot if primary embellishment replaces sleeves
                if slot_id == "dress.sleeves" and primary_embellishment:
                    # Check if primary embellishment is a sleeve replacement (like wing sleeves)
                    if hasattr(primary_embellishment, 'key') and 'wing_sleeve' in primary_embellishment.key:
                        # Skip this slot - architectural sleeves replace standard sleeves
                        selected_atoms = []
                        print(f"    🔄 Sleeve slot skipped - replaced by {primary_embellishment.key}")
                    else:
                        selected_atoms = select_atoms_for_slot(slot, all_atoms, ensemble_prefs, ensemble_pools, all_selected_atoms, selected_camera_distance)
                # Special case: if this is theme_embellishment_primary and we have pre-selected, use that
                elif slot_id == "theme_embellishment_primary" and pre_selected_primary_embellishment:
                    selected_atoms = [pre_selected_primary_embellishment]
                else:
                    selected_atoms = select_atoms_for_slot(slot, all_atoms, ensemble_prefs, ensemble_pools, all_selected_atoms, selected_camera_distance)
            
            # Capture primary embellishment when selected (for cases where it wasn't pre-selected)
            if slot_id == "theme_embellishment_primary" and selected_atoms and not primary_embellishment:
                primary_embellishment = selected_atoms[0]
                # Distance should already be set from pre-determination, but handle fallback
                if not selected_camera_distance and hasattr(primary_embellishment, 'min_visible_distance'):
                    selected_camera_distance = primary_embellishment.min_visible_distance
            
            # Add to tracking list
            all_selected_atoms.extend(selected_atoms)
            
            # DUPLICATE DETECTION: Track which slot each atom appears in
            for atom in selected_atoms:
                if atom.key not in atom_slot_map:
                    atom_slot_map[atom.key] = []
                atom_slot_map[atom.key].append(slot_id)
            
            if selected_atoms:
                # CHECKPOINT TRACKING
                for atom in selected_atoms:
                    # Debug makeup selection
                    if "makeup" in slot_id:
                        print(f"    📄 Makeup atom selected: {atom.key}")
                    
                    if "age_safety_early" in slot_id:
                        checkpoint_tracker["age_safety_early"].append(atom.key)
                    elif "age_safety_late" in slot_id:
                        checkpoint_tracker["age_safety_late"].append(atom.key)
                    elif "dissonance" in slot_id:
                        checkpoint_tracker["dissonance"].append(atom.key)
                    elif "style.core_mandate" in slot_id:
                        checkpoint_tracker["style_foundation"].append(atom.key)
                
                # Group atoms by contents for this slot
                atom_contents = [a.contents for a in selected_atoms if a.contents]
                if atom_contents:
                    layer_contents.append(f"{slot_name}: {' '.join(atom_contents)}")
        
        # Only add layer section if it has content
        # SKIP ENSEMBLE_VISION - it's internal metadata, not needed by image generator
        if layer_contents and layer_id != "ENSEMBLE_VISION":
            sections.append(f"═══ {layer_title} ═══")
            sections.extend(layer_contents)
            sections.append("")
    
    # DUPLICATE DETECTION REPORT
    duplicates_found = {k: v for k, v in atom_slot_map.items() if len(v) > 1}
    build_prompt.duplicate_data = duplicates_found
    
    # Store checkpoint data for console logging
    build_prompt.checkpoint_data = checkpoint_tracker
    
    # FINAL NEGATIVE ENFORCEMENT for close-ups
    if selected_camera_distance == "close":
        sections.append("═══ FRAMING ENFORCEMENT ═══")
        sections.append("FINAL REMINDER: HEADSHOT. Face and neck only. Frame ends at neck base.")
        sections.append("")
    
    return "\n".join(sections)

def count_tokens(text: str) -> int:
    """Count tokens using tiktoken if available, fallback to math estimation"""
    if TIKTOKEN_AVAILABLE:
        try:
            return len(encoding.encode(text))
        except (AttributeError, TypeError) as e:
            # Fallback if encoding fails or text is invalid
            return len(text) // 4
    else:
        return len(text) // 4

def main():
    import sys
    import subprocess
    
    # Show tiktoken status with diagnostics
    if TIKTOKEN_AVAILABLE:
        print("✓ Using tiktoken for accurate token counting")
    else:
        print("⚠ tiktoken not available - using math estimation (len // 4)")
        print("  To use tiktoken: pip install tiktoken")
        print("  Verify with: python -c \"import tiktoken; print('tiktoken OK')\"")
    
    print("Generating prompt with coordinated ensemble theming...")
    print()
    
    all_atoms = load_atoms()
    schema = load_schema()
    
    print(f"Loaded {len(all_atoms)} atoms")
    print()
    
    # Extract ensemble selection ONCE, pass to both console and prompt builder
    ensemble_name = "Unknown"
    selected_ensemble_atom = None
    for layer in schema.get("layers", []):
        if layer.get("layer_id") == "ENSEMBLE_VISION":
            for slot in layer.get("slots", []):
                selected_atoms = select_atoms_for_slot(slot, all_atoms)
                if selected_atoms:
                    import random
                    selected_ensemble_atom = random.choice(selected_atoms)
                    # Extract theme name from atom key (e.g., "ensemble.bow_bonanza" -> "bow_bonanza")
                    ensemble_name = selected_ensemble_atom.key.split(".")[-1].replace("_", " ").title()
            break
    
    print(f"🎀 Ensemble Theme Selected: {ensemble_name}")
    print()
    
    # PRE-SELECT PRIMARY EMBELLISHMENT to determine camera distance for all slots
    primary_embellishment = None
    camera_distance = None
    for layer in schema.get("layers", []):
        for slot in layer.get("slots", []):
            if slot.get("slot_id") == "theme_embellishment_primary":
                # Need to pass ensemble prefs to get theme-appropriate embellishment
                ensemble_prefs = {}
                if selected_ensemble_atom:
                    # Load ensemble preferences
                    for def_file in os.listdir(os.path.join(os.path.dirname(__file__), DEFINITIONS_DIR)):
                        if def_file == "dress_ensembles.json":
                            with open(os.path.join(os.path.dirname(__file__), DEFINITIONS_DIR, def_file)) as f:
                                ensemble_data = json.load(f)
                                for key, val in ensemble_data.items():
                                    if key == selected_ensemble_atom.key:
                                        ensemble_prefs = val
                                        break
                
                # Load camera atoms for validation
                camera_atoms = []
                for atom in all_atoms.values():
                    if atom.key.startswith("camera."):
                        camera_atoms.append(atom)
                
                # Select primary embellishment with camera validation
                max_attempts = 10  # Prevent infinite loop
                attempted_primaries = []
                
                # Pre-determine effective camera distance for filtering
                effective_distance = DEBUG_FORCE_CLOSE_CAMERA if DEBUG_FORCE_CLOSE_CAMERA else None
                distance_hierarchy = {'close': 0, 'medium': 1, 'full_body': 2}
                
                for attempt in range(max_attempts):
                    selected_atoms = select_atoms_for_slot(slot, all_atoms, ensemble_prefs, exclude_atoms=attempted_primaries)
                    if not selected_atoms:
                        print(f"   ⚠ No more primary embellishments available")
                        break
                    
                    candidate_primary = selected_atoms[0]
                    candidate_distance = getattr(candidate_primary, 'min_visible_distance', 'medium')
                    placement = getattr(candidate_primary, 'placement', None)
                    
                    # PRE-FILTER: Skip primaries that won't be visible at effective camera distance
                    if effective_distance:
                        eff_level = distance_hierarchy.get(effective_distance, 1)
                        cand_level = distance_hierarchy.get(candidate_distance, 1)
                        
                        # If candidate requires farther distance than we're locked to, skip
                        if cand_level > eff_level:
                            print(f"   ❌ {candidate_primary.key} - requires {candidate_distance} (locked to {effective_distance})")
                            attempted_primaries.append(candidate_primary)
                            continue
                        
                        # If placement is 'back' and we're doing front shots, skip
                        if placement == 'back':
                            print(f"   ❌ {candidate_primary.key} - back placement (front camera)")
                            attempted_primaries.append(candidate_primary)
                            continue
                    
                    camera_distance = candidate_distance
                    
                    # Validate cameras exist for this primary
                    suitable_cameras = coordinate_camera_with_embellishment(candidate_primary, camera_atoms)
                    
                    if len(suitable_cameras) == 0:
                        # No suitable cameras for this primary
                        reason = ""
                        if placement == 'back':
                            reason = "requires back cameras (not available)"
                        elif getattr(candidate_primary, 'group', '') == 'D1_Hair_Architectural':
                            if DEBUG_FORCE_CLOSE_CAMERA == 'medium':
                                reason = "requires close cameras (debug locked to medium)"
                            else:
                                reason = "requires close cameras (none suitable)"
                        else:
                            reason = f"no suitable cameras for {placement} placement at {camera_distance} distance"
                        
                        print(f"   ❌ {candidate_primary.key} - {reason}")
                        attempted_primaries.append(candidate_primary)
                        continue
                    
                    # Found valid primary with suitable cameras
                    primary_embellishment = candidate_primary
                    print(f"🎯 Primary embellishment selected: {primary_embellishment.key}")
                    if hasattr(primary_embellishment, 'placement'):
                        print(f"   Placement: {primary_embellishment.placement}")
                    print(f"   Requires camera distance: {camera_distance}")
                    print(f"   ✓ {len(suitable_cameras)} suitable cameras available")
                    break
                
                if not primary_embellishment:
                    # No valid primary found - use fallback with warning
                    if attempted_primaries:
                        primary_embellishment = attempted_primaries[0]  # Use first attempted
                        camera_distance = getattr(primary_embellishment, 'min_visible_distance', 'medium')
                        print(f"🎯 Primary embellishment FALLBACK: {primary_embellishment.key}")
                        print(f"   ⚠ Using despite no suitable cameras - expect issues")
                    else:
                        print(f"   ❌ CRITICAL: No primary embellishments available at all")
                
                # DEBUG OVERRIDE: Force specific camera distance if debug flag is set
                if DEBUG_FORCE_CLOSE_CAMERA and primary_embellishment:
                    if isinstance(DEBUG_FORCE_CLOSE_CAMERA, str):
                        camera_distance = DEBUG_FORCE_CLOSE_CAMERA
                        print(f"   🔒 DEBUG: Camera locked to {camera_distance.upper()} for debugging")
                    else:
                        camera_distance = "close"
                        print(f"   🔒 DEBUG: Camera locked to CLOSE-UP for debugging")
                    
                    print(f"   Distance-aware filtering active for ALL slots")
                    print()
                break
        if primary_embellishment:
            break
    
    # Pass selected ensemble atom, camera distance, AND primary embellishment to prompt builder
    prompt = build_prompt(all_atoms, schema, selected_ensemble_atom, camera_distance, primary_embellishment)
    
    # CHECKPOINT REPORTING
    print("═══ MANDATE CHECKPOINT REPORT ═══")
    if hasattr(build_prompt, 'checkpoint_data'):
        checkpoints = build_prompt.checkpoint_data
        
        print(f"✓ Age Safety (Early): {len(checkpoints['age_safety_early'])} atoms")
        if checkpoints['age_safety_early']:
            for atom_key in checkpoints['age_safety_early']:
                print(f"  • {atom_key}")
        
        print(f"✓ Age Safety (Late): {len(checkpoints['age_safety_late'])} atoms")
        if checkpoints['age_safety_late']:
            for atom_key in checkpoints['age_safety_late']:
                print(f"  • {atom_key}")
        
        print(f"✓ Dissonance: {len(checkpoints['dissonance'])} atoms")
        if checkpoints['dissonance']:
            for atom_key in checkpoints['dissonance']:
                print(f"  • {atom_key}")
        
        print(f"✓ Style Foundation: {len(checkpoints['style_foundation'])} atoms")
        if checkpoints['style_foundation']:
            for atom_key in checkpoints['style_foundation']:
                print(f"  • {atom_key}")
        
        # Pass/fail assessment
        print()
        all_checks_pass = (
            len(checkpoints['age_safety_early']) >= 2 and
            len(checkpoints['age_safety_late']) >= 1 and
            len(checkpoints['dissonance']) >= 1 and
            len(checkpoints['style_foundation']) >= 1
        )
        if all_checks_pass:
            print("✅ MANDATE CHECKPOINT: PASS - All critical atoms present")
        else:
            print("⚠️  MANDATE CHECKPOINT: PARTIAL - Review selected atoms above")
    else:
        print("⚠️  Checkpoint tracking unavailable")
    
    # DUPLICATE DETECTION REPORT
    if hasattr(build_prompt, 'duplicate_data') and build_prompt.duplicate_data:
        print()
        print("🚨 DUPLICATE ATOM DETECTION")
        print("────────────────────────────────────────────────────────────")
        for atom_key, slots in build_prompt.duplicate_data.items():
            print(f"  ⚠️  {atom_key}")
            print(f"      Appears in: {', '.join(slots)}")
        print()
        print("  FIX GUIDANCE:")
        print("  ─────────────")
        print("  1. Check atom's 'group' field in definitions/*.json")
        print("     - D0_Core atoms → should ONLY appear in 'dress.embellishments'")
        print("     - D1_Architectural atoms → should ONLY appear in 'theme_embellishment_primary'")
        print("  2. If group is correct, check camera.py filtering logic:")
        print("     - Lines ~150-175: Group filters for each slot")
        print("     - Verify slot_id matching is exact")
        print("  3. Check layer_slot_schema.json for slot configuration")
        print("     - Verify include_prefixes don't overlap")
        print("  4. Run: python development_protocols.py for deeper analysis")
        print("────────────────────────────────────────────────────────────")
    
    print()
    
    tokens = count_tokens(prompt)
    print(f"Generated prompt: {tokens} tokens (target: {TOKEN_TARGET})")
    
    # Save
    output_path = os.path.join(os.path.dirname(__file__), OUTPUT_FILE)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(prompt)
    
    print(f"✓ Saved to {OUTPUT_FILE}")
    
    # Show stats
    if tokens > TOKEN_TARGET * 1.1:
        print(f"⚠ Over budget by {tokens - TOKEN_TARGET} tokens")
    elif tokens < TOKEN_TARGET * 0.9:
        print(f"⚠ Under budget by {TOKEN_TARGET - tokens} tokens")
    else:
        print("✓ Within target range")
    
    # Run analytics
    print()
    print("╔════════════════════════════════════════════════════════════╗")
    print("║          Running Integrated Analytics                      ║")
    print("╚════════════════════════════════════════════════════════════╝")
    print()
    if run_analytics:
        try:
            run_analytics(prompt, TOKEN_TARGET)
        except Exception as e:
            print(f"⚠ Analytics error: {e}")
    else:
        print("⚠ Analytics module unavailable")
    print()
    
    # Run violation analysis
    if ViolationAnalyzer:
        print("╔════════════════════════════════════════════════════════════╗")
        print("║          Running Violation Analysis                        ║")
        print("╚════════════════════════════════════════════════════════════╝")
        print()
        try:
            analyzer = ViolationAnalyzer()
            report = analyzer.analyze_all()
            
            # Show summary
            total_violations = (
                len(report.get("narrative_violations", [])) +
                len(report.get("filter_risk_violations", [])) +
                len(report.get("character_limit_violations", []))
            )
            
            if total_violations > 0:
                print(f"⚠️  Found {total_violations} violations:")
                print(f"  • Narrative language: {len(report.get('narrative_violations', []))}")
                print(f"  • Filter-risk language: {len(report.get('filter_risk_violations', []))}")
                print(f"  • Character limit: {len(report.get('character_limit_violations', []))}")
                analyzer.save_report(report)
            else:
                print("✅ No violations detected!")
            print()
        except Exception as e:
            print(f"⚠ Violation analysis error: {e}")
            print()
    
    # ═══════════════════════════════════════════════════════════════
    # GENERATION ANALYTICS TRACKING
    # ═══════════════════════════════════════════════════════════════
    if track_generation:
        try:
            # Extract colors from prompt text
            import re
            dress_color_match = re.search(r'Dress Color:\s*(\w+)', prompt)
            accent_color_match = re.search(r'Accent Color:\s*(\w+)', prompt)
            
            # Get violation counts
            violations_by_type = {}
            total_violations = 0
            if ViolationAnalyzer:
                try:
                    analyzer = ViolationAnalyzer()
                    report = analyzer.analyze_all()
                    violations_by_type = {
                        "narrative": len(report.get("narrative_violations", [])),
                        "filter_risk": len(report.get("filter_risk_violations", [])),
                        "character_limit": len(report.get("character_limit_violations", []))
                    }
                    total_violations = sum(violations_by_type.values())
                except Exception as e:
                    # Violation analysis failed, continue without it
                    print(f"Warning: Violation analysis failed: {e}")
                    pass
            
            # Get checkpoint data
            checkpoints = {}
            if hasattr(build_prompt, 'checkpoint_data'):
                checkpoints = build_prompt.checkpoint_data
            
            # Get duplicate data
            duplicates = {}
            if hasattr(build_prompt, 'duplicate_data'):
                duplicates = build_prompt.duplicate_data
            
            # Build selected atoms dict (simplified - just track what we have)
            selected_atoms_summary = {}
            if checkpoints:
                for slot_name, atoms in checkpoints.items():
                    selected_atoms_summary[slot_name] = atoms
            
            track_generation(
                prompt_tokens=tokens,
                token_target=TOKEN_TARGET,
                camera_distance=camera_distance if 'camera_distance' in dir() else 'medium',
                ensemble_theme=ensemble_name if 'ensemble_name' in dir() else 'Unknown',
                ensemble_atom_key=selected_ensemble_atom.key if 'selected_ensemble_atom' in dir() and selected_ensemble_atom else '',
                primary_embellishment_key=primary_embellishment.key if 'primary_embellishment' in dir() and primary_embellishment else None,
                primary_placement=getattr(primary_embellishment, 'placement', None) if 'primary_embellishment' in dir() and primary_embellishment else None,
                dress_color=dress_color_match.group(1) if dress_color_match else None,
                accent_color=accent_color_match.group(1) if accent_color_match else None,
                selected_atoms=selected_atoms_summary,
                violation_count=total_violations,
                violations_by_type=violations_by_type,
                mandate_checkpoints=checkpoints,
                duplicate_atoms=duplicates
            )
            print("📊 Generation tracked to analytics")
        except Exception as e:
            print(f"⚠ Analytics tracking error: {e}")
    
    # Open the file
    print(f"\nOpening {OUTPUT_FILE}...")
    try:
        if sys.platform == "win32":
            try:
                os.startfile(output_path)
            except (AttributeError, OSError):
                # startfile not available or failed, try notepad
                subprocess.Popen(['notepad.exe', output_path])
        elif sys.platform == "darwin":
            subprocess.run(["open", output_path])
        else:
            # subprocess.run(["xdg-open", output_path])  # Disabled for testing
            pass
    except Exception as e:
        print(f"Note: Could not auto-open file ({e})")
        print(f"Please manually open: {output_path}")


if __name__ == "__main__":
    main()

