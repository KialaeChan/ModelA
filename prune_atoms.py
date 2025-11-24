#!/usr/bin/env python3
import json
import re
import sys

def prune_content(content):
    """Aggressively prune content following the atom writing standards."""
    
    # Remove forbidden phrases
    forbidden = [
        r"Realistic digital rendering of [^.]*\.",
        r"Shows? (\d+-?\d*\s+)?hours? of [^.]*\.",
        r"Shows? time investment[^.]*\.",
        r"Professional (salon |technique|placement)[^.]*\.",
        r"Requires? [^.]*time[^.]*\.",
        r"Applied with [^.]*brush[^.]*\.",
        r"Each layer (carefully|precisely|allowed to)[^.]*\.",
        r"Creates? dimensional [^.]*effect",
        r"Reads as special occasion[^.]*\.",
        r"Cannot hide [^.]*\.",
        r"Cannot disguise [^.]*\.",
        r"Despite [^.]*makeup[^.]*\.",
        r"Professional (technique|layering|grooming)[^.]*\.",
        r"Fabric has body and spring",
        r"with realistic [^.]*response",
    ]
    
    for pattern in forbidden:
        content = re.sub(pattern, "", content, flags=re.IGNORECASE)
    
    # Remove redundant words
    content = re.sub(r'\bfabric\b', '', content, count=5)  # Keep first instance only
    content = re.sub(r'\bcreating\b', '', content)
    content = re.sub(r'\bdimensional\s+', '', content, count=3)  # Reduce usage
    
    # Clean up spacing
    content = re.sub(r'\s+', ' ', content)
    content = re.sub(r'\s*\.\s*\.', '.', content)
    content = re.sub(r'\s*,\s*,', ',', content)
    content = re.sub(r'\s+\.', '.', content)
    content = content.strip()
    
    return content

def process_file(filepath):
    """Process a single JSON file."""
    with open(filepath, 'r') as f:
        data = json.load(f)
    
    modified = False
    for key, atom in data.items():
        if 'contents' in atom:
            original = atom['contents']
            pruned = prune_content(original)
            
            if len(pruned) != len(original):
                atom['contents'] = pruned
                modified = True
                print(f"{key}: {len(original)} -> {len(pruned)} chars ({100*(len(original)-len(pruned))//len(original)}% reduction)")
    
    if modified:
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"\n✓ Updated {filepath}")
        return True
    return False

if __name__ == "__main__":
    files = sys.argv[1:] if len(sys.argv) > 1 else []
    
    if not files:
        print("Usage: python3 prune_atoms.py file1.json file2.json ...")
        sys.exit(1)
    
    for filepath in files:
        print(f"\n=== Processing {filepath} ===")
        process_file(filepath)
