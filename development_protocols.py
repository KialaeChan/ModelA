#!/usr/bin/env python3
"""Development testing protocols for ModelA project"""

import json
import subprocess
import re
from collections import defaultdict

def capture_current_state():
    """Capture system state before any changes"""
    result = subprocess.run(['python', 'camera.py'], capture_output=True, text=True)
    
    # Extract token count
    token_match = re.search(r'Generated prompt: (\d+) tokens', result.stdout)
    tokens = int(token_match.group(1)) if token_match else 0
    
    # Count atoms by group and priority
    with open('definitions/shiny_embellishments.json', 'r') as f:
        embellishments = json.load(f)
    
    groups = defaultdict(int)
    priorities = defaultdict(int)
    
    for atom in embellishments.values():
        groups[atom.get('group', 'none')] += 1
        priorities[atom.get('priority', 'none')] += 1
    
    return {
        'tokens': tokens,
        'groups': dict(groups),
        'priorities': dict(priorities),
        'total_atoms': len(embellishments)
    }

def check_slot_contamination():
    """Check if atoms appear in multiple slots"""
    
    # Run camera.py and check for duplicate detection output
    result = subprocess.run(['python', 'camera.py'], capture_output=True, text=True)
    
    # Check if camera.py detected duplicates
    if "DUPLICATE ATOM DETECTION" in result.stdout:
        # Extract the duplicate info
        lines = result.stdout.split('\n')
        duplicates = []
        current_atom = None
        for line in lines:
            if "⚠️" in line and "DUPLICATE" not in line:
                current_atom = line.strip().replace("⚠️", "").strip()
            elif "Appears in:" in line and current_atom:
                slots = line.split("Appears in:")[1].strip()
                duplicates.append(f"{current_atom} -> {slots}")
                current_atom = None
        
        if duplicates:
            return False, f"DUPLICATES DETECTED:\n" + "\n".join(f"  - {d}" for d in duplicates)
    
    # Also do the original theme/shiny check
    with open('prompt.txt', 'r') as f:
        prompt = f.read()
    
    # Extract embellishments
    theme_match = re.search(r'Theme Embellishment \(Primary\): (.+?)(?:\n|$)', prompt)
    shiny_match = re.search(r'Shiny Embellishments: (.+?)(?:\n|$)', prompt)
    
    theme_emb = theme_match.group(1) if theme_match else ""
    shiny_emb = shiny_match.group(1) if shiny_match else ""
    
    # Check for duplication
    if theme_emb and shiny_emb:
        # Check if first sentence of theme appears in shiny
        theme_first = theme_emb.split('.')[0]
        if theme_first in shiny_emb:
            return False, f"CONTAMINATION: Same atom in both slots!\nTheme: {theme_emb[:80]}\nShiny: {shiny_emb[:80]}"
    
    return True, "No contamination detected"

def verify_group_assignments():
    """Verify atoms are in correct groups for their slots"""
    
    with open('definitions/shiny_embellishments.json', 'r') as f:
        embellishments = json.load(f)
    
    issues = []
    
    # Check all atoms have groups
    for key, atom in embellishments.items():
        if 'group' not in atom:
            issues.append(f"{key} missing group!")
        elif atom['group'] not in ['D0_Core', 'D1_Architectural']:
            issues.append(f"{key} has invalid group: {atom['group']}")
    
    # Count groups
    d0_count = sum(1 for a in embellishments.values() if a.get('group') == 'D0_Core')
    d1_count = sum(1 for a in embellishments.values() if a.get('group') == 'D1_Architectural')
    
    print(f"D0_Core (complementary): {d0_count}")
    print(f"D1_Architectural (signature): {d1_count}")
    
    if d0_count < 10:
        issues.append(f"Only {d0_count} D0_Core atoms - need more variety!")
    
    if d1_count < 8:
        issues.append(f"Only {d1_count} D1_Architectural atoms - need more signatures!")
    
    return len(issues) == 0, issues

def test_multiple_generations(n=10):
    """Test multiple generations for variety and contamination"""
    
    results = defaultdict(list)
    
    for i in range(n):
        subprocess.run(['python', 'camera.py'], capture_output=True, text=True)
        
        with open('prompt.txt', 'r') as f:
            prompt = f.read()
        
        # Extract what was selected
        theme_match = re.search(r'Theme Embellishment \(Primary\): (.+?)(?:\n|$)', prompt)
        shiny_match = re.search(r'Shiny Embellishments: (.+?)(?:\n|$)', prompt)
        
        if theme_match:
            theme = theme_match.group(1)[:50]
            results['theme_embellishments'].append(theme)
        
        if shiny_match:
            shiny = shiny_match.group(1)[:50]
            results['shiny_embellishments'].append(shiny)
            
            # Check for contamination
            if theme_match and theme_match.group(1) in shiny_match.group(1):
                results['contamination'].append(f"Generation {i+1}")
    
    # Report
    print(f"\nRan {n} generations:")
    print(f"Unique theme embellishments: {len(set(results['theme_embellishments']))}")
    print(f"Unique shiny embellishments: {len(set(results['shiny_embellishments']))}")
    
    if results['contamination']:
        print(f"⚠️  CONTAMINATION in: {', '.join(results['contamination'])}")
        return False
    else:
        print("✓ No contamination detected")
        return True

def check_atom_in_correct_slot(atom_key):
    """Verify a specific atom appears in the correct slot"""
    
    # Load atom to check its group
    with open('definitions/shiny_embellishments.json', 'r') as f:
        embellishments = json.load(f)
    
    if atom_key not in embellishments:
        return False, f"Atom {atom_key} not found!"
    
    atom = embellishments[atom_key]
    group = atom.get('group', 'none')
    
    # Run generation and check where it appears
    subprocess.run(['python', 'camera.py'], capture_output=True, text=True)
    
    with open('prompt.txt', 'r') as f:
        prompt = f.read()
    
    atom_content = atom.get('contents', '')[:50]
    
    in_theme = atom_content in prompt[prompt.find('Theme Embellishment'):prompt.find('Shiny Embellishments')] if 'Theme Embellishment' in prompt else False
    in_shiny = atom_content in prompt[prompt.find('Shiny Embellishments'):] if 'Shiny Embellishments' in prompt else False
    
    if group == 'D1_Architectural':
        if in_shiny:
            return False, f"D1_Architectural atom {atom_key} appearing in Shiny slot!"
        return True, f"D1_Architectural atom correctly in Theme slot only"
    elif group == 'D0_Core':
        if in_theme:
            return False, f"D0_Core atom {atom_key} appearing in Theme slot!"
        return True, f"D0_Core atom correctly in Shiny slot only"
    
    return False, f"Atom {atom_key} has invalid group: {group}"

def run_all_checks():
    """Run all verification checks"""
    
    print("="*60)
    print("RUNNING COMPREHENSIVE CHECKS")
    print("="*60)
    
    # Check 1: State
    print("\n1. CURRENT STATE:")
    state = capture_current_state()
    print(f"   Tokens: {state['tokens']}")
    print(f"   Groups: {state['groups']}")
    print(f"   Priorities: {state['priorities']}")
    
    # Check 2: Groups
    print("\n2. GROUP ASSIGNMENTS:")
    groups_ok, issues = verify_group_assignments()
    if not groups_ok:
        print("   ⚠️  Issues found:")
        for issue in issues:
            print(f"      - {issue}")
    else:
        print("   ✓ All groups correctly assigned")
    
    # Check 3: Contamination
    print("\n3. SLOT CONTAMINATION:")
    clean, message = check_slot_contamination()
    if not clean:
        print(f"   ⚠️  {message}")
    else:
        print("   ✓ No contamination")
    
    # Check 4: Multiple generations
    print("\n4. MULTIPLE GENERATION TEST:")
    variety_ok = test_multiple_generations(5)
    
    print("\n" + "="*60)
    
    # Final verdict
    all_ok = groups_ok and clean and variety_ok
    if all_ok:
        print("✅ ALL CHECKS PASSED")
    else:
        print("❌ CHECKS FAILED - FIX REQUIRED")
    
    return all_ok

if __name__ == "__main__":
    run_all_checks()
