#!/usr/bin/env python3
"""
Token Analysis Tool for ModelA (Offline Version)
Provides detailed breakdown of token usage across definition files and atoms
"""

import json
import os
from pathlib import Path
from collections import defaultdict
import re

def estimate_tokens(text):
    """Estimate tokens using character-based heuristic (offline version)
    Based on: ~1.3 tokens per word for English descriptive text"""
    if not text:
        return 0
    
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    
    # Approximate: 1.3 tokens per word
    word_count = len(text.split())
    estimated_tokens = int(word_count * 1.3)
    
    return max(estimated_tokens, 1)

def count_tokens(text):
    """Count tokens using offline estimation"""
    return estimate_tokens(text)

def analyze_atoms():
    """Analyze all atoms in definition files"""
    definitions_dir = Path("definitions")
    
    file_stats = {}
    bloated_atoms = []
    total_tokens = 0
    priority_distribution = defaultdict(int)
    
    # Analyze each definition file
    for json_file in sorted(definitions_dir.glob("*.json")):
        with open(json_file, 'r', encoding='utf-8') as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError as e:
                print(f"ERROR parsing {json_file.name}: {e}")
                continue
        
        file_tokens = 0
        atom_count = 0
        file_atoms = []
        
        # Process atoms - they're stored as dict keys with content inside
        for atom_id, atom_data in data.items():
            if isinstance(atom_data, dict):
                # Get content - could be in 'contents' or 'text'
                atom_text = atom_data.get("contents", atom_data.get("text", ""))
                priority = atom_data.get("priority", "P2")
                
                # Normalize priority format
                if "P0" in priority:
                    priority = "P0"
                elif "P1" in priority:
                    priority = "P1"
                else:
                    priority = "P2"
            else:
                atom_text = str(atom_data)
                priority = "P2"
            
            atom_tokens = count_tokens(atom_text)
            file_tokens += atom_tokens
            total_tokens += atom_tokens
            atom_count += 1
            
            priority_distribution[priority] += atom_tokens
            
            file_atoms.append({
                'id': atom_id,
                'tokens': atom_tokens,
                'priority': priority,
                'preview': atom_text[:60] + "..." if len(atom_text) > 60 else atom_text
            })
            
            # Track bloated atoms (>50 tokens)
            if atom_tokens > 50:
                bloated_atoms.append({
                    'file': json_file.name,
                    'id': atom_id,
                    'tokens': atom_tokens,
                    'priority': priority,
                    'text': atom_text
                })
        
        # Store file statistics
        file_stats[json_file.name] = {
            'tokens': file_tokens,
            'atom_count': atom_count,
            'avg_tokens': file_tokens / atom_count if atom_count > 0 else 0,
            'atoms': file_atoms
        }
    
    return file_stats, bloated_atoms, total_tokens, priority_distribution

def analyze_preamble():
    """Analyze preamble/configuration tokens"""
    config_tokens = 0
    
    # Check config.json
    try:
        with open("config.json", 'r', encoding='utf-8') as f:
            config = json.load(f)
            config_tokens += count_tokens(json.dumps(config))
    except:
        pass
    
    # Check for preamble in layer_slot_schema
    try:
        with open("layer_slot_schema.json", 'r', encoding='utf-8') as f:
            schema = json.load(f)
            if "preamble" in schema:
                config_tokens += count_tokens(schema["preamble"])
            # Also count any instructions
            if "instructions" in schema:
                config_tokens += count_tokens(str(schema["instructions"]))
    except:
        pass
    
    return config_tokens

def print_report(file_stats, bloated_atoms, total_tokens, priority_distribution, preamble_tokens):
    """Generate and print analysis report"""
    
    print("\n" + "="*80)
    print("TOKEN ANALYSIS REPORT FOR MODELA")
    print("="*80)
    print("(Using offline token estimation: ~1.3 tokens per word)")
    
    # Summary
    print(f"\nTOTAL TOKEN COUNT: {total_tokens:,} tokens")
    print(f"Preamble/Config: ~{preamble_tokens:,} tokens")
    print(f"Atoms: {total_tokens:,} tokens")
    print(f"ESTIMATED TOTAL PROMPT: ~{total_tokens + preamble_tokens:,} tokens")
    
    tokens_to_cut = max(0, total_tokens + preamble_tokens - 3000)
    if tokens_to_cut > 0:
        print(f"\n⚠ OVER BUDGET: Need to reduce ~{tokens_to_cut} tokens (target: 3,000)")
    else:
        print(f"\n✓ WITHIN BUDGET: {total_tokens + preamble_tokens} / 3000 tokens")
    
    # Priority distribution
    print("\nPRIORITY DISTRIBUTION:")
    print("-" * 40)
    for priority in ['P0', 'P1', 'P2']:
        tokens = priority_distribution.get(priority, 0)
        pct = (tokens / total_tokens * 100) if total_tokens > 0 else 0
        print(f"  {priority}: {tokens:,} tokens ({pct:.1f}%)")
    
    # File breakdown
    print("\nFILE BREAKDOWN (by token consumption):")
    print("-" * 40)
    sorted_files = sorted(file_stats.items(), key=lambda x: x[1]['tokens'], reverse=True)
    
    for filename, stats in sorted_files:
        pct = (stats['tokens'] / total_tokens * 100) if total_tokens > 0 else 0
        print(f"  {filename:40s} {stats['tokens']:5d} tokens ({pct:5.1f}%) - {stats['atom_count']:3d} atoms")
    
    # Bloated atoms analysis
    print("\nBLOATED ATOMS (>50 tokens - candidates for splitting):")
    print("-" * 80)
    if bloated_atoms:
        sorted_bloated = sorted(bloated_atoms, key=lambda x: x['tokens'], reverse=True)
        for i, atom in enumerate(sorted_bloated[:20], 1):  # Show top 20
            print(f"\n  [{i}] {atom['file']}: {atom['id']}")
            print(f"      Priority: {atom['priority']} | Tokens: {atom['tokens']}")
            print(f"      Text: {atom['text'][:100]}...")
    else:
        print("  No atoms >50 tokens found - good structure!")
    
    # Recommendations
    print("\nOPTIMIZATION RECOMMENDATIONS:")
    print("-" * 80)
    
    if tokens_to_cut > 0:
        print(f"  Target reduction: ~{tokens_to_cut:,} tokens\n")
        print(f"  Strategy (in priority order):")
        
        bloated_count = len(bloated_atoms)
        if bloated_count > 0:
            saved = bloated_count * 20
            print(f"    1. Split {bloated_count} bloated atoms (est. {saved:,} tokens)")
        
        print(f"    2. Remove redundant synonyms in P2 atoms (est. 100-200 tokens)")
        print(f"    3. Move detailed descriptions to P2 only (est. 150-300 tokens)")
        print(f"    4. Consolidate similar concepts (est. 50-150 tokens)")
        
        if tokens_to_cut > 500:
            print(f"    5. Reduce P1 atom verbosity (est. 200-400 tokens)")
    else:
        print(f"  ✓ Within budget! Current: {total_tokens + preamble_tokens} / 3000")
    
    print("\n" + "="*80)

def main():
    print("Analyzing ModelA token usage (offline mode)...")
    
    file_stats, bloated_atoms, total_tokens, priority_distribution = analyze_atoms()
    preamble_tokens = analyze_preamble()
    
    print_report(file_stats, bloated_atoms, total_tokens, priority_distribution, preamble_tokens)
    
    # Save detailed report
    with open("token_analysis.json", 'w', encoding='utf-8') as f:
        json.dump({
            'total_tokens': total_tokens,
            'preamble_tokens': preamble_tokens,
            'estimated_total': total_tokens + preamble_tokens,
            'file_stats': {k: {
                'tokens': v['tokens'],
                'atom_count': v['atom_count'],
                'avg_tokens': round(v['avg_tokens'], 1)
            } for k, v in file_stats.items()},
            'priority_distribution': dict(priority_distribution),
            'bloated_atoms_count': len(bloated_atoms),
            'estimation_note': 'Using 1.3 tokens per word approximation'
        }, f, indent=2)
    
    print("\nDetailed report saved to: token_analysis.json")

if __name__ == "__main__":
    main()
