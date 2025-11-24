#!/usr/bin/env python3
"""
Theme Signature Elements Audit
Analyzes what signature elements each theme currently has
"""

import json
import os

def load_json(filepath):
    """Load a JSON file"""
    with open(filepath, 'r') as f:
        return json.load(f)

def analyze_theme_signatures():
    """Analyze signature elements for each theme"""
    
    print("=" * 60)
    print("THEME SIGNATURE ELEMENTS AUDIT")
    print("=" * 60)
    
    # Load all relevant data
    ensembles = load_json('definitions/dress_ensembles.json')
    embellishments = load_json('definitions/shiny_embellishments.json')
    patterns = load_json('definitions/dress_patterns.json')
    fabrics = load_json('definitions/dress_fabrics.json')
    colors = load_json('definitions/dress_colors.json')
    
    # Analyze each ensemble
    for key, ensemble in ensembles.items():
        if not key.startswith('ensemble.'):
            continue
            
        print(f"\n{'='*60}")
        print(f"📦 {key}")
        print(f"   Theme: {ensemble.get('theme', 'NO THEME')}")
        print(f"   Vision: {ensemble.get('description', 'No description')}")
        print(f"{'='*60}")
        
        # Count signature elements
        signature_count = 0
        
        # 1. PRIMARY EMBELLISHMENTS (Architectural signature)
        emb_pool = ensemble.get('embellishment_pool', [])
        print(f"\n1. PRIMARY EMBELLISHMENTS ({len(emb_pool)} items):")
        for emb in emb_pool[:3]:  # Show first 3
            emb_key = emb.replace('embellish.', '')
            if f"embellish.{emb_key}" in embellishments:
                atom = embellishments[f"embellish.{emb_key}"]
                print(f"   - {emb_key}: {atom.get('description', 'No desc')[:50]}...")
        if emb_pool:
            signature_count += 1
            
        # 2. PATTERNS
        pattern_pool = ensemble.get('pattern_pool', [])
        print(f"\n2. PATTERNS ({len(pattern_pool)} items):")
        for pat in pattern_pool[:3]:
            pat_key = pat.replace('dress.pattern.', '')
            print(f"   - {pat_key}")
        if pattern_pool:
            signature_count += 1
            
        # 3. FABRICS/MATERIALS
        fabric_pool = ensemble.get('fabric_pool', [])
        print(f"\n3. FABRICS ({len(fabric_pool)} items):")
        for fab in fabric_pool[:3]:
            fab_key = fab.replace('fabric.', '')
            print(f"   - {fab_key}")
        if fabric_pool:
            signature_count += 1
            
        # 4. SECONDARY DETAILS (Tailoring/Construction)
        tailoring_pool = ensemble.get('tailoring_pool', [])
        print(f"\n4. SECONDARY DETAILS ({len(tailoring_pool)} items):")
        for tail in tailoring_pool[:3]:
            tail_key = tail.replace('tailoring.', '')
            print(f"   - {tail_key}")
        if tailoring_pool:
            signature_count += 1
            
        # 5. ACCESSORIES (Hair accessories, hosiery)
        hair_acc = ensemble.get('hair_accessory_pool', [])
        hosiery = ensemble.get('hosiery_pool', [])
        print(f"\n5. ACCESSORIES:")
        print(f"   Hair: {len(hair_acc)} items")
        if hair_acc:
            print(f"      - {hair_acc[0].replace('hair.accessory.', '')}")
        print(f"   Hosiery: {len(hosiery)} items")
        if hosiery:
            print(f"      - {hosiery[0].replace('hosiery.', '')}")
        if hair_acc or hosiery:
            signature_count += 1
            
        # Summary
        print(f"\n📊 SIGNATURE ELEMENTS: {signature_count}/5")
        
        # Identify what's missing
        missing = []
        if not emb_pool:
            missing.append("Primary embellishments")
        if not pattern_pool:
            missing.append("Patterns")
        if not fabric_pool:
            missing.append("Fabrics")
        if not tailoring_pool:
            missing.append("Secondary details")
        if not hair_acc and not hosiery:
            missing.append("Accessories")
            
        if missing:
            print(f"⚠️  MISSING: {', '.join(missing)}")
        else:
            print(f"✅ All 5 signature categories present")
            
        # Theme cohesion check
        print(f"\n🎨 THEME COHESION:")
        focus_keywords = ensemble.get('embellishment_focus', [])
        print(f"   Focus keywords: {focus_keywords}")
        
        # Check if elements match theme
        theme_name = ensemble.get('theme', '').lower()
        cohesive_elements = []
        
        # Check patterns for theme words
        for pat in pattern_pool:
            if any(word in pat.lower() for word in focus_keywords):
                cohesive_elements.append(f"Pattern: {pat}")
                
        # Check embellishments for theme
        for emb in emb_pool:
            if any(word in emb.lower() for word in focus_keywords):
                cohesive_elements.append(f"Embellishment: {emb}")
                
        if cohesive_elements:
            print(f"   ✅ Cohesive elements found:")
            for elem in cohesive_elements[:3]:
                print(f"      - {elem}")
        else:
            print(f"   ⚠️ No elements match theme keywords")
    
    print("\n" + "="*60)
    print("RECOMMENDATIONS")
    print("="*60)
    print("""
For each theme to have 5 strong signature elements:

1. PRIMARY ARCHITECTURAL SIGNATURE
   - Distinctive silhouette-breaking embellishment
   - Should match theme name/vision

2. SECONDARY DECORATIVE MOTIFS  
   - Supporting D0_Core embellishments
   - Reinforce theme without competing

3. COLOR/PATTERN COORDINATION
   - Patterns that echo theme
   - Color palette that supports vision

4. MATERIAL/TEXTURE CHOICES
   - Fabrics that embody theme aesthetic
   - Textures that enhance theme

5. UNIQUE DISTINGUISHING FEATURES
   - Accessories, trims, special details
   - Elements that make theme instantly recognizable
""")

if __name__ == "__main__":
    analyze_theme_signatures()
