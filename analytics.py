#!/usr/bin/env python3
"""
ModelA Analytics Toolkit
Runs integrated analysis after every prompt generation via camera.py
Provides real-time insights into token usage, atom efficiency, and system health
"""

import json
import os
from typing import Dict, List, Tuple, Any
from pathlib import Path

# Try to import tiktoken for accurate token counting
TIKTOKEN_AVAILABLE = False
encoding = None

try:
    import tiktoken
    encoding = tiktoken.get_encoding("cl100k_base")
    TIKTOKEN_AVAILABLE = True
except:
    try:
        from tiktoken import get_encoding
        encoding = get_encoding("cl100k_base")
        TIKTOKEN_AVAILABLE = True
    except:
        pass


def count_tokens(text: str) -> int:
    """Count tokens in text using tiktoken if available, else estimate"""
    if TIKTOKEN_AVAILABLE and encoding:
        try:
            return len(encoding.encode(text))
        except:
            return len(text) // 4
    return len(text) // 4


def analyze_definitions(definitions_dir: str = "definitions") -> Dict[str, Any]:
    """
    Analyze all definition files for token efficiency and atom quality
    Returns detailed metrics per file and aggregate statistics
    """
    if not os.path.exists(definitions_dir):
        return {}
    
    analysis = {
        "files": {},
        "totals": {
            "total_atoms": 0,
            "total_tokens": 0,
            "avg_tokens_per_atom": 0,
        },
        "by_priority": {
            "P0: MANDATE": {"atoms": 0, "tokens": 0},
            "P1: CORE": {"atoms": 0, "tokens": 0},
            "P2: DETAIL": {"atoms": 0, "tokens": 0},
        },
        "violations": {
            "over_300_chars": [],
            "over_100_tokens": [],
            "narrative_language": [],
        },
        "efficiency": {
            "most_efficient_atoms": [],  # tokens per atom ratio
            "least_efficient_atoms": [],
            "dense_atoms": [],  # many tokens in few chars
        }
    }
    
    # Narrative language patterns
    narrative_patterns = [
        "shows", "creates", "demonstrates", "reads as", "appears",
        "seems", "suggests", "looks like", "could be", "reminds of",
        "applied with", "hand-sewn", "buffed", "layered", "stitched",
        "professional", "precise", "elaborate", "careful", "masterfully",
        "grim", "haunting", "poignant", "tragic", "beautiful", "precious"
    ]
    
    all_atoms = []
    
    # Process each definition file
    for filename in sorted(os.listdir(definitions_dir)):
        if not filename.endswith('.json'):
            continue
        
        filepath = os.path.join(definitions_dir, filename)
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                definitions = json.load(f)
        except:
            continue
        
        file_analysis = {
            "atoms": 0,
            "tokens": 0,
            "avg_tokens": 0,
            "atom_list": []
        }
        
        for atom_key, atom_data in definitions.items():
            if "contents" not in atom_data:
                continue
            
            contents = atom_data.get("contents", "")
            chars = len(contents)
            tokens = count_tokens(contents)
            priority = atom_data.get("priority", "P2: DETAIL")
            
            atom_info = {
                "key": atom_key,
                "chars": chars,
                "tokens": tokens,
                "priority": priority,
                "description": atom_data.get("description", ""),
                "contents": contents[:100] + "..." if len(contents) > 100 else contents,
            }
            
            file_analysis["atoms"] += 1
            file_analysis["tokens"] += tokens
            file_analysis["atom_list"].append(atom_info)
            analysis["totals"]["total_atoms"] += 1
            analysis["totals"]["total_tokens"] += tokens
            all_atoms.append(atom_info)
            
            # Priority tracking
            if priority in analysis["by_priority"]:
                analysis["by_priority"][priority]["atoms"] += 1
                analysis["by_priority"][priority]["tokens"] += tokens
            
            # Violation detection
            if chars > 300:
                analysis["violations"]["over_300_chars"].append({
                    "key": atom_key,
                    "chars": chars,
                    "tokens": tokens,
                    "file": filename
                })
            
            if tokens > 100:
                analysis["violations"]["over_100_tokens"].append({
                    "key": atom_key,
                    "chars": chars,
                    "tokens": tokens,
                    "file": filename
                })
            
            # Narrative language detection (use word boundaries to avoid false positives)
            import re
            lower_contents = contents.lower()
            found_patterns = [p for p in narrative_patterns if re.search(r'\b' + re.escape(p) + r'\b', lower_contents)]
            if found_patterns:
                analysis["violations"]["narrative_language"].append({
                    "key": atom_key,
                    "file": filename,
                    "patterns": found_patterns,
                })
        
        if file_analysis["atoms"] > 0:
            file_analysis["avg_tokens"] = file_analysis["tokens"] / file_analysis["atoms"]
            analysis["files"][filename] = file_analysis
    
    # Calculate efficiency metrics
    if all_atoms:
        # Filter out metadata entries with no real content (0 tokens or 0 chars)
        real_atoms = [a for a in all_atoms if a["tokens"] > 0 and a["chars"] > 0]
        
        # Sort by efficiency (tokens per character - higher = denser)
        all_atoms_with_efficiency = [
            {**a, "efficiency": a["tokens"] / max(a["chars"], 1)}
            for a in real_atoms
        ]
        
        all_atoms_with_efficiency.sort(key=lambda x: x["efficiency"], reverse=True)
        
        # Most efficient (dense - good)
        analysis["efficiency"]["dense_atoms"] = [
            {
                "key": a["key"],
                "tokens": a["tokens"],
                "chars": a["chars"],
                "ratio": f"{a['efficiency']:.3f}",
                "file": next((f for f, fa in analysis["files"].items() 
                            if a["key"] in [atom["key"] for atom in fa["atom_list"]]), "unknown")
            }
            for a in all_atoms_with_efficiency[:15]  # Top 15 densest
        ]
        
        # Least efficient (verbose - maybe trim)
        all_atoms_with_efficiency.sort(key=lambda x: x["efficiency"])
        analysis["efficiency"]["least_efficient_atoms"] = [
            {
                "key": a["key"],
                "tokens": a["tokens"],
                "chars": a["chars"],
                "ratio": f"{a['efficiency']:.3f}",
                "file": next((f for f, fa in analysis["files"].items() 
                            if a["key"] in [atom["key"] for atom in fa["atom_list"]]), "unknown")
            }
            for a in all_atoms_with_efficiency[:15]  # Bottom 15 least dense
        ]
    
    if analysis["totals"]["total_atoms"] > 0:
        analysis["totals"]["avg_tokens_per_atom"] = (
            analysis["totals"]["total_tokens"] / analysis["totals"]["total_atoms"]
        )
    
    return analysis


def generate_analysis_report(
    prompt_text: str,
    analysis: Dict[str, Any],
    token_target: int = 3000
) -> str:
    """Generate a formatted analysis report"""
    
    prompt_tokens = count_tokens(prompt_text)
    budget_status = prompt_tokens - token_target
    
    report = []
    report.append("╔════════════════════════════════════════════════════════════╗")
    report.append("║           MODELА ANALYTICS REPORT                          ║")
    report.append("╚════════════════════════════════════════════════════════════╝")
    report.append("")
    
    # Token Overview
    report.append("📊 TOKEN OVERVIEW")
    report.append("─" * 60)
    report.append(f"  Prompt Tokens:        {prompt_tokens:,}")
    report.append(f"  Target:               {token_target:,}")
    report.append(f"  Budget Status:        {budget_status:+,} {'⚠️ OVER' if budget_status > 0 else '✓ UNDER'}")
    if token_target > 0:
        percent = (prompt_tokens / token_target) * 100
        report.append(f"  Utilization:          {percent:.1f}% of target")
    report.append("")
    
    # Atom Library Overview
    if analysis.get("totals"):
        totals = analysis["totals"]
        report.append("📚 ATOM LIBRARY")
        report.append("─" * 60)
        report.append(f"  Total Atoms:          {totals['total_atoms']:,}")
        report.append(f"  Total Atom Tokens:    {totals['total_tokens']:,}")
        report.append(f"  Avg per Atom:         {totals['avg_tokens_per_atom']:.1f} tokens")
        report.append("")
    
    # Priority Breakdown
    if analysis.get("by_priority"):
        report.append("🎯 PRIORITY BREAKDOWN")
        report.append("─" * 60)
        for priority, data in analysis["by_priority"].items():
            if data["atoms"] > 0:
                pct = (data["tokens"] / analysis["totals"]["total_tokens"] * 100) if analysis["totals"]["total_tokens"] > 0 else 0
                report.append(f"  {priority:15} {data['atoms']:3} atoms, {data['tokens']:5} tokens ({pct:5.1f}%)")
        report.append("")
    
    # Top Files by Token Weight
    if analysis.get("files"):
        report.append("🔝 HEAVIEST FILES")
        report.append("─" * 60)
        files_by_tokens = sorted(
            [(name, data) for name, data in analysis["files"].items()],
            key=lambda x: x[1]["tokens"],
            reverse=True
        )[:5]
        for filename, file_data in files_by_tokens:
            report.append(f"  {filename:40} {file_data['tokens']:5} tokens ({file_data['atoms']:2} atoms)")
        report.append("")
    
    # Violations Summary
    violations = analysis.get("violations", {})
    total_violations = sum(len(v) if isinstance(v, list) else 0 for v in violations.values())
    
    if total_violations > 0:
        report.append("⚠️  VIOLATIONS DETECTED")
        report.append("─" * 60)
        if violations.get("over_100_tokens"):
            report.append(f"  Atoms over 100 tokens:  {len(violations['over_100_tokens'])}")
            for v in violations["over_100_tokens"][:3]:
                report.append(f"    • {v['key']:40} {v['tokens']:3} tokens")
        if violations.get("over_300_chars"):
            report.append(f"  Atoms over 300 chars:   {len(violations['over_300_chars'])}")
        if violations.get("narrative_language"):
            report.append(f"  Narrative language:     {len(violations['narrative_language'])}")
        report.append("")
    else:
        report.append("✅ NO VIOLATIONS DETECTED")
        report.append("")
    
    # Efficiency Insights
    if analysis.get("efficiency"):
        report.append("⚡ EFFICIENCY INSIGHTS")
        report.append("─" * 60)
        
        if analysis["efficiency"].get("dense_atoms"):
            report.append(f"  Most token-dense atoms (good compression):")
            for atom in analysis["efficiency"]["dense_atoms"][:5]:
                report.append(f"    • {atom['key']:35} {atom['ratio']} tokens/char")
        
        if analysis["efficiency"].get("least_efficient_atoms"):
            report.append(f"\n  Least efficient atoms (consider trimming):")
            for atom in analysis["efficiency"]["least_efficient_atoms"][:5]:
                report.append(f"    • {atom['key']:35} {atom['ratio']} tokens/char - trim candidate")
        report.append("")
    
    report.append("═" * 60)
    report.append(f"Report generated. Tiktoken available: {TIKTOKEN_AVAILABLE}")
    report.append("")
    
    return "\n".join(report)


def run_analytics(prompt_text: str, token_target: int = 3000) -> None:
    """Main function to run analytics and print report"""
    analysis = analyze_definitions()
    report = generate_analysis_report(prompt_text, analysis, token_target)
    print(report)
    return analysis


if __name__ == "__main__":
    # For standalone testing
    if os.path.exists("prompt.txt"):
        with open("prompt.txt", 'r', encoding='utf-8') as f:
            prompt = f.read()
        run_analytics(prompt)
