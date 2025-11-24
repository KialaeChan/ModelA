#!/usr/bin/env python3
"""
ModelA Generation Analytics - Comprehensive Data Tracking
Tracks EVERYTHING about each generation for analysis and optimization.
Data is gold!
"""

import json
import os
from datetime import datetime
from typing import Dict, List, Any, Optional
from pathlib import Path

# Analytics data file
ANALYTICS_FILE = "generation_history.json"
ANALYTICS_SUMMARY_FILE = "analytics_summary.json"

def load_history() -> List[Dict]:
    """Load existing generation history"""
    if os.path.exists(ANALYTICS_FILE):
        try:
            with open(ANALYTICS_FILE, 'r') as f:
                return json.load(f)
        except (json.JSONDecodeError, PermissionError) as e:
            # Return empty list if file is corrupted or unreadable
            print(f"Warning: Could not load history file: {e}")
            return []
    return []

def save_history(history: List[Dict]) -> None:
    """Save generation history"""
    with open(ANALYTICS_FILE, 'w') as f:
        json.dump(history, f, indent=2, default=str)

def track_generation(
    # Core generation data
    prompt_tokens: int,
    token_target: int,
    camera_distance: str,
    
    # Theme/ensemble data
    ensemble_theme: str,
    ensemble_atom_key: str,
    
    # Primary embellishment
    primary_embellishment_key: Optional[str],
    primary_placement: Optional[str],
    
    # Colors
    dress_color: Optional[str],
    accent_color: Optional[str],
    
    # Selected atoms by slot
    selected_atoms: Dict[str, List[str]],
    
    # Violations
    violation_count: int,
    violations_by_type: Dict[str, int],
    
    # Checkpoints
    mandate_checkpoints: Dict[str, List[str]],
    
    # Duplicates detected
    duplicate_atoms: Dict[str, List[str]],
    
    # Additional metadata
    metadata: Optional[Dict] = None
) -> Dict:
    """
    Track a single generation with all its data.
    Returns the tracked record.
    """
    
    record = {
        # Timestamp
        "timestamp": datetime.now().isoformat(),
        "generation_id": datetime.now().strftime("%Y%m%d_%H%M%S_%f"),
        
        # Token metrics
        "tokens": {
            "prompt": prompt_tokens,
            "target": token_target,
            "delta": prompt_tokens - token_target,
            "utilization_pct": round((prompt_tokens / token_target) * 100, 1) if token_target > 0 else 0,
            "over_budget": prompt_tokens > token_target
        },
        
        # Camera
        "camera": {
            "distance": camera_distance
        },
        
        # Theme/Ensemble
        "theme": {
            "name": ensemble_theme,
            "atom_key": ensemble_atom_key
        },
        
        # Primary embellishment
        "primary_embellishment": {
            "key": primary_embellishment_key,
            "placement": primary_placement
        },
        
        # Colors
        "colors": {
            "dress": dress_color,
            "accent": accent_color
        },
        
        # Atom selection
        "atoms_selected": selected_atoms,
        "total_atoms_selected": sum(len(v) for v in selected_atoms.values()),
        
        # Violations
        "violations": {
            "total": violation_count,
            "by_type": violations_by_type
        },
        
        # Mandate checkpoints
        "checkpoints": mandate_checkpoints,
        
        # Duplicates
        "duplicates": {
            "count": len(duplicate_atoms),
            "atoms": duplicate_atoms
        },
        
        # Custom metadata
        "metadata": metadata or {}
    }
    
    # Load, append, save
    history = load_history()
    history.append(record)
    save_history(history)
    
    # Update summary stats
    update_summary_stats(history)
    
    return record


def update_summary_stats(history: List[Dict]) -> Dict:
    """Calculate aggregate statistics from history"""
    
    if not history:
        return {}
    
    summary = {
        "last_updated": datetime.now().isoformat(),
        "total_generations": len(history),
        
        # Token stats
        "tokens": {
            "avg_prompt": round(sum(h["tokens"]["prompt"] for h in history) / len(history), 1),
            "min_prompt": min(h["tokens"]["prompt"] for h in history),
            "max_prompt": max(h["tokens"]["prompt"] for h in history),
            "over_budget_count": sum(1 for h in history if h["tokens"]["over_budget"]),
            "over_budget_pct": round(sum(1 for h in history if h["tokens"]["over_budget"]) / len(history) * 100, 1)
        },
        
        # Camera distance distribution
        "camera_distribution": {},
        
        # Theme distribution
        "theme_distribution": {},
        
        # Color distribution
        "dress_color_distribution": {},
        "accent_color_distribution": {},
        
        # Primary embellishment distribution
        "primary_embellishment_distribution": {},
        "primary_placement_distribution": {},
        
        # Violation trends
        "violations": {
            "avg_per_generation": round(sum(h["violations"]["total"] for h in history) / len(history), 1),
            "zero_violation_count": sum(1 for h in history if h["violations"]["total"] == 0),
            "by_type_totals": {}
        },
        
        # Top atoms (most frequently selected)
        "top_atoms": {},
        
        # Duplicate frequency
        "duplicate_frequency": round(sum(h["duplicates"]["count"] for h in history) / len(history), 2)
    }
    
    # Calculate distributions
    for h in history:
        # Camera
        cam = h["camera"]["distance"]
        summary["camera_distribution"][cam] = summary["camera_distribution"].get(cam, 0) + 1
        
        # Theme
        theme = h["theme"]["name"]
        summary["theme_distribution"][theme] = summary["theme_distribution"].get(theme, 0) + 1
        
        # Colors
        if h["colors"]["dress"]:
            dc = h["colors"]["dress"]
            summary["dress_color_distribution"][dc] = summary["dress_color_distribution"].get(dc, 0) + 1
        if h["colors"]["accent"]:
            ac = h["colors"]["accent"]
            summary["accent_color_distribution"][ac] = summary["accent_color_distribution"].get(ac, 0) + 1
        
        # Primary embellishment
        if h["primary_embellishment"]["key"]:
            pe = h["primary_embellishment"]["key"]
            summary["primary_embellishment_distribution"][pe] = summary["primary_embellishment_distribution"].get(pe, 0) + 1
        if h["primary_embellishment"]["placement"]:
            pp = h["primary_embellishment"]["placement"]
            summary["primary_placement_distribution"][pp] = summary["primary_placement_distribution"].get(pp, 0) + 1
        
        # Violations by type
        for vtype, vcount in h["violations"]["by_type"].items():
            summary["violations"]["by_type_totals"][vtype] = summary["violations"]["by_type_totals"].get(vtype, 0) + vcount
    
    # Calculate atom frequency across all generations
    atom_counts = {}
    for h in history:
        for slot, atoms in h.get("atoms_selected", {}).items():
            for atom in atoms:
                atom_counts[atom] = atom_counts.get(atom, 0) + 1
    
    # Top 20 most selected atoms
    sorted_atoms = sorted(atom_counts.items(), key=lambda x: x[1], reverse=True)[:20]
    summary["top_atoms"] = {k: v for k, v in sorted_atoms}
    
    # Sort distributions by frequency
    summary["camera_distribution"] = dict(sorted(summary["camera_distribution"].items(), key=lambda x: x[1], reverse=True))
    summary["theme_distribution"] = dict(sorted(summary["theme_distribution"].items(), key=lambda x: x[1], reverse=True))
    summary["dress_color_distribution"] = dict(sorted(summary["dress_color_distribution"].items(), key=lambda x: x[1], reverse=True))
    summary["primary_embellishment_distribution"] = dict(sorted(summary["primary_embellishment_distribution"].items(), key=lambda x: x[1], reverse=True)[:10])
    
    # Save summary
    with open(ANALYTICS_SUMMARY_FILE, 'w') as f:
        json.dump(summary, f, indent=2)
    
    return summary


def print_analytics_dashboard() -> None:
    """Print a formatted analytics dashboard"""
    
    if not os.path.exists(ANALYTICS_SUMMARY_FILE):
        print("No analytics data yet. Generate some prompts first!")
        return
    
    with open(ANALYTICS_SUMMARY_FILE, 'r') as f:
        summary = json.load(f)
    
    print()
    print("╔════════════════════════════════════════════════════════════╗")
    print("║           MODELА GENERATION ANALYTICS DASHBOARD            ║")
    print("╚════════════════════════════════════════════════════════════╝")
    print()
    
    print(f"📊 OVERVIEW ({summary['total_generations']} generations)")
    print("─" * 60)
    print(f"  Last updated: {summary['last_updated'][:19]}")
    print()
    
    # Token stats
    print("🔢 TOKEN STATISTICS")
    print("─" * 60)
    t = summary["tokens"]
    print(f"  Average:      {t['avg_prompt']:,.0f} tokens")
    print(f"  Range:        {t['min_prompt']:,} - {t['max_prompt']:,}")
    print(f"  Over budget:  {t['over_budget_count']}/{summary['total_generations']} ({t['over_budget_pct']}%)")
    print()
    
    # Camera distribution
    print("📷 CAMERA DISTANCE DISTRIBUTION")
    print("─" * 60)
    for dist, count in summary["camera_distribution"].items():
        pct = round(count / summary['total_generations'] * 100, 1)
        bar = "█" * int(pct / 5)
        print(f"  {dist:10} {count:3} ({pct:5.1f}%) {bar}")
    print()
    
    # Theme distribution
    print("🎀 THEME DISTRIBUTION")
    print("─" * 60)
    for theme, count in list(summary["theme_distribution"].items())[:8]:
        pct = round(count / summary['total_generations'] * 100, 1)
        bar = "█" * int(pct / 5)
        print(f"  {theme:25} {count:3} ({pct:5.1f}%) {bar}")
    print()
    
    # Color distribution
    print("🎨 TOP DRESS COLORS")
    print("─" * 60)
    for color, count in list(summary["dress_color_distribution"].items())[:5]:
        pct = round(count / summary['total_generations'] * 100, 1)
        print(f"  {color:15} {count:3} ({pct:5.1f}%)")
    print()
    
    # Primary embellishments
    print("✨ TOP PRIMARY EMBELLISHMENTS")
    print("─" * 60)
    for emb, count in list(summary["primary_embellishment_distribution"].items())[:5]:
        short_name = emb.split(".")[-1] if "." in emb else emb
        print(f"  {short_name:35} {count:3}")
    print()
    
    # Violations
    print("⚠️  VIOLATION TRENDS")
    print("─" * 60)
    v = summary["violations"]
    print(f"  Avg per generation: {v['avg_per_generation']}")
    print(f"  Zero violations:    {v['zero_violation_count']}/{summary['total_generations']}")
    if v["by_type_totals"]:
        print("  By type:")
        for vtype, vcount in v["by_type_totals"].items():
            print(f"    • {vtype}: {vcount}")
    print()
    
    # Top atoms
    print("🔝 MOST FREQUENTLY SELECTED ATOMS")
    print("─" * 60)
    for atom, count in list(summary["top_atoms"].items())[:10]:
        short_name = atom.split(".")[-1] if "." in atom else atom
        print(f"  {short_name:40} {count:3}")
    print()
    
    print("═" * 60)
    print()


def get_recent_generations(n: int = 10) -> List[Dict]:
    """Get the N most recent generations"""
    history = load_history()
    return history[-n:]


def export_to_csv(filename: str = "generation_export.csv") -> None:
    """Export generation history to CSV for external analysis"""
    import csv
    
    history = load_history()
    if not history:
        print("No data to export")
        return
    
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        
        # Header
        writer.writerow([
            "timestamp", "generation_id",
            "tokens_prompt", "tokens_target", "tokens_delta", "over_budget",
            "camera_distance",
            "theme_name", "theme_atom",
            "primary_embellishment", "primary_placement",
            "dress_color", "accent_color",
            "total_atoms", "violations_total", "duplicates_count"
        ])
        
        # Data rows
        for h in history:
            writer.writerow([
                h["timestamp"],
                h["generation_id"],
                h["tokens"]["prompt"],
                h["tokens"]["target"],
                h["tokens"]["delta"],
                h["tokens"]["over_budget"],
                h["camera"]["distance"],
                h["theme"]["name"],
                h["theme"]["atom_key"],
                h["primary_embellishment"]["key"],
                h["primary_embellishment"]["placement"],
                h["colors"]["dress"],
                h["colors"]["accent"],
                h["total_atoms_selected"],
                h["violations"]["total"],
                h["duplicates"]["count"]
            ])
    
    print(f"✓ Exported {len(history)} records to {filename}")


if __name__ == "__main__":
    print_analytics_dashboard()
