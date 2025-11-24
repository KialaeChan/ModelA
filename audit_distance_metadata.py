#!/usr/bin/env python3
"""
Comprehensive distance metadata audit for ModelA atoms.
Identifies all atoms with measurements that need distance limits.
"""

import json
import os
import re

def has_measurements(content):
    """Check if content has specific measurements"""
    patterns = [
        r'\d+-\d+mm',  # 5-6mm
        r'\d+mm',       # 5mm
        r'\d+-\d+cm',   # 2-3cm
        r'\d+cm',       # 3cm
        r'\d+-\d+ ',    # 8-10 items
        r'multiple tiny',
        r'scattered',
        r'individual'
    ]
    
    for pattern in patterns:
        if re.search(pattern, content, re.IGNORECASE):
            return True
    return False

def audit_file(filepath):
    """Audit a single JSON file for distance issues"""
    filename = os.path.basename(filepath)
    
    with open(filepath, 'r') as f:
        data = json.load(f)
    
    issues = {
        'no_distance': [],
        'wrong_distance': [],
        'needs_variant': []
    }
    
    for key, atom in data.items():
        content = atom.get('contents', '')
        
        if not has_measurements(content):
            continue
            
        min_dist = atom.get('min_visible_distance')
        max_dist = atom.get('max_visible_distance')
        
        # Check for issues
        if not min_dist and not max_dist:
            issues['no_distance'].append(key)
        elif min_dist == 'medium' and 'mm' in content:
            issues['wrong_distance'].append(key)
        elif min_dist == 'close' and not key.endswith('_medium') and not key.endswith('_full'):
            # Might need distance variants
            issues['needs_variant'].append(key)
    
    return issues

def main():
    """Run comprehensive audit"""
    definitions_dir = 'definitions'
    
    print("=" * 60)
    print("COMPREHENSIVE DISTANCE METADATA AUDIT")
    print("=" * 60)
    print()
    
    total_issues = 0
    
    for filename in sorted(os.listdir(definitions_dir)):
        if not filename.endswith('.json'):
            continue
            
        filepath = os.path.join(definitions_dir, filename)
        issues = audit_file(filepath)
        
        # Skip if no issues
        if not any(issues.values()):
            continue
            
        print(f"\n📁 {filename}")
        print("-" * 40)
        
        if issues['no_distance']:
            print(f"❌ NO DISTANCE METADATA: {len(issues['no_distance'])} atoms")
            for atom in issues['no_distance'][:3]:
                print(f"   - {atom}")
            if len(issues['no_distance']) > 3:
                print(f"   ... and {len(issues['no_distance'])-3} more")
            total_issues += len(issues['no_distance'])
        
        if issues['wrong_distance']:
            print(f"⚠️  WRONG DISTANCE (mm at medium): {len(issues['wrong_distance'])} atoms")
            for atom in issues['wrong_distance'][:3]:
                print(f"   - {atom}")
            if len(issues['wrong_distance']) > 3:
                print(f"   ... and {len(issues['wrong_distance'])-3} more")
            total_issues += len(issues['wrong_distance'])
        
        if issues['needs_variant']:
            print(f"📝 MAY NEED VARIANTS: {len(issues['needs_variant'])} atoms")
            # Don't list all, just count
            total_issues += len(issues['needs_variant'])
    
    print()
    print("=" * 60)
    print(f"TOTAL ISSUES FOUND: {total_issues}")
    print("=" * 60)
    
    print("\nRECOMMENDATIONS:")
    print("1. Add distance metadata to all atoms with measurements")
    print("2. Set mm measurements to close-only")
    print("3. Create medium/full variants without measurements")
    print("4. Test token reduction after fixes")

if __name__ == "__main__":
    main()
