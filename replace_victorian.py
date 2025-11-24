#!/usr/bin/env python3
import json
import glob
import os

REPLACEMENTS = {
    # Victorian -> Fun special day
    'Victorian doll aesthetic': 'Fun special day aesthetic',
    'Victorian doll': 'special day',
    'Victorian formal': 'special occasion',
    'Victorian nature motif': 'fun nature decoration',
    'Victorian military-inspired': 'fancy dress-up',
    'Victorian hand-finishing': 'special handwork',
    'Victorian aesthetic': 'party dress style',
    'Victorian detail': 'special detail',
    'Victorian': 'special day',
    
    # Stuffy language -> Fun language
    'elegant': 'fun',
    'refined': 'special',
    'sophisticated': 'fancy',
    'formal doll': 'party dress',
    'recital aesthetic': 'special day fun',
    'vintage formal': 'party special',
}

def replace_in_text(text):
    """Replace Victorian/stuffy language with fun special day language."""
    for old, new in REPLACEMENTS.items():
        text = text.replace(old, new)
    return text

def process_json_file(filepath):
    """Process JSON file to replace language."""
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    modified = False
    for key, atom in data.items():
        if 'contents' in atom:
            original = atom['contents']
            updated = replace_in_text(original)
            if updated != original:
                atom['contents'] = updated
                modified = True
                print(f"{key}: Updated language")
        
        if 'description' in atom:
            original = atom['description']
            updated = replace_in_text(original)
            if updated != original:
                atom['description'] = updated
                modified = True
    
    if modified:
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"✓ Updated {filepath}")
        return True
    return False

# Process all JSON files
definitions_dir = '/home/claude/ModelA/definitions'
json_files = glob.glob(os.path.join(definitions_dir, '*.json'))

updated_count = 0
for filepath in json_files:
    if process_json_file(filepath):
        updated_count += 1

print(f"\n{updated_count} files updated with fun special day language")
