#!/usr/bin/env python3
"""
Theme Coordination Diagnostic Tool
Identifies mismatches between ensemble themes and atom tags
"""

import json
import os
from collections import defaultdict

def load_json(filepath):
    """Load a JSON file"""
    with open(filepath, 'r') as f:
        return json.load(f)

def analyze_theme_coordination():
    """Analyze theme coordination between ensembles and atoms"""
    
    print("=" * 60)
    print("THEME COORDINATION DIAGNOSTIC")
    print("=" * 60)
    
    # Load ensembles
    ensembles = load_json('definitions/dress_ensembles.json')
    
    # Load all embellishment atoms
    embellishments = load_json('definitions/shiny_embellishments.json')
    
    # Analyze each ensemble
    issues = []
    
    for key, ensemble in ensembles.items():
        if not key.startswith('ensemble.'):
            continue
            
        print(f"\n📦 {key}")
        print(f"   Theme: {ensemble.get('theme', 'NO THEME')}")
        
        # Get embellishment focus keywords
        focus_keywords = ensemble.get('embellishment_focus', [])
        print(f"   Focus keywords: {focus_keywords}")
        
        # Check if any atoms match
        matching_atoms = []
        pool_atoms = ensemble.get('embellishment_pool', [])
        
        for atom_key, atom in embellishments.items():
            # Skip if not in pool
            if f"embellish.{atom_key.split('.')[-1]}" not in pool_atoms:
                continue
                
            theme_tags = atom.get('theme_tags', [])
            
            # Check for keyword matches
            matches = False
            for keyword in focus_keywords:
                # Check in atom key
                if keyword.lower() in atom_key.lower():
                    matches = True
                    break
                # Check in theme tags
                for tag in theme_tags:
                    if keyword.lower() in tag.lower():
                        matches = True
                        break
                        
            if matches:
                matching_atoms.append(atom_key)
        
        if matching_atoms:
            print(f"   ✅ Found {len(matching_atoms)} matching atoms")
        else:
            print(f"   ❌ NO MATCHING ATOMS!")
            issues.append({
                'ensemble': key,
                'keywords': focus_keywords,
                'pool': pool_atoms
            })
    
    # Report issues
    if issues:
        print("\n" + "=" * 60)
        print("⚠️  COORDINATION ISSUES FOUND")
        print("=" * 60)
        
        for issue in issues:
            print(f"\n{issue['ensemble']}:")
            print(f"  Keywords {issue['keywords']} don't match any atoms in pool")
            print(f"  Pool has {len(issue['pool'])} atoms but none have matching tags")
            print(f"  SOLUTION: Either:")
            print(f"    1. Add theme_tags to atoms in pool matching keywords")
            print(f"    2. Change embellishment_focus keywords to match existing tags")
            print(f"    3. Use compound tags like 'romantic_floral' in both places")
    
    # Check for atoms with missing theme_tags
    print("\n" + "=" * 60)
    print("ATOMS WITHOUT THEME TAGS")
    print("=" * 60)
    
    no_tags = []
    for atom_key, atom in embellishments.items():
        if not atom.get('theme_tags'):
            no_tags.append(atom_key)
    
    if no_tags:
        print(f"\n⚠️  {len(no_tags)} atoms have no theme_tags:")
        for atom in no_tags[:10]:  # Show first 10
            print(f"  - {atom}")
        if len(no_tags) > 10:
            print(f"  ... and {len(no_tags) - 10} more")
    else:
        print("\n✅ All atoms have theme_tags")
    
    print("\n" + "=" * 60)
    print("DIAGNOSTIC COMPLETE")
    print("=" * 60)

if __name__ == "__main__":
    analyze_theme_coordination()
