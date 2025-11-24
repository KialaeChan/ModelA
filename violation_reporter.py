#!/usr/bin/env python3
"""
ModelA Violation Detail Reporter
Provides detailed analysis of specific violations with suggested fixes
Integrates with analytics.py for deeper insights
"""

import json
import os
from typing import Dict, List, Any

# Import analytics utilities
try:
    from analytics import count_tokens, TIKTOKEN_AVAILABLE
except:
    # Fallback if analytics not available
    def count_tokens(text: str) -> int:
        return len(text) // 4
    TIKTOKEN_AVAILABLE = False


class ViolationAnalyzer:
    """Analyzes specific violations and provides remediation guidance"""
    
    NARRATIVE_PATTERNS = {
        "shows": "Use observable fact instead",
        "creates": "Use observable fact instead",
        "demonstrates": "Use observable fact instead",
        "reads as": "Use observable fact instead",
        "appears": "Use observable fact instead",
        "seems": "Use observable fact instead",
        "suggests": "Use observable fact instead",
        "looks like": "Use observable fact instead",
        "could be": "Remove speculation",
        "reminds of": "Remove interpretation",
        "applied with": "Remove process description",
        "hand-sewn": "Remove process description",
        "buffed": "Remove process description",
        "layered": "Remove process description",
        "stitched": "Remove process description",
        "professional": "Remove interpretive adjective",
        "precise": "Remove interpretive adjective",
        "elaborate": "Remove interpretive adjective",
        "careful": "Remove interpretive adjective",
        "masterfully": "Remove interpretive adjective",
        "grim": "Remove evocative language",
        "haunting": "Remove evocative language",
        "poignant": "Remove evocative language",
        "tragic": "Remove evocative language",
        "beautiful": "Remove evocative language",
        "precious": "Remove evocative language",
        "exhausted": "Replace with filter-safe alternative (fatigued)",
        "resigned": "Replace with filter-safe alternative (composed)",
        "withdrawn": "Replace with filter-safe alternative (reserved)",
        "vacant": "Replace with filter-safe alternative (unfocused)",
        "trained": "Replace with filter-safe alternative (practiced)",
        "broken": "Replace with filter-safe alternative (diminished)",
        "conditioned": "Replace with filter-safe alternative (prepared)",
        "obedient": "Replace with filter-safe alternative (cooperative)",
        "complying": "Replace with filter-safe alternative (obliging)",
    }
    
    def __init__(self, definitions_dir: str = "definitions"):
        self.definitions_dir = definitions_dir
        self.violations = {
            "narrative": [],
            "filter_risk": [],
            "over_limit": [],
            "redundancy": [],
        }
        self.all_atoms = {}
        self._load_definitions()
    
    def _load_definitions(self):
        """Load all definition files"""
        if not os.path.exists(self.definitions_dir):
            return
        
        for filename in sorted(os.listdir(self.definitions_dir)):
            if not filename.endswith('.json'):
                continue
            
            filepath = os.path.join(self.definitions_dir, filename)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    definitions = json.load(f)
                    for atom_key, atom_data in definitions.items():
                        self.all_atoms[atom_key] = {
                            "data": atom_data,
                            "file": filename,
                            "contents": atom_data.get("contents", ""),
                        }
            except:
                continue
    
    def analyze_all(self) -> Dict[str, Any]:
        """Run complete analysis on all atoms"""
        report = {
            "narrative_violations": [],
            "filter_risk_violations": [],
            "character_limit_violations": [],
            "token_heavy_atoms": [],
            "potential_redundancy": [],
        }
        
        for atom_key, atom_info in self.all_atoms.items():
            contents = atom_info["contents"]
            chars = len(contents)
            tokens = count_tokens(contents)
            
            # Check narrative language
            narrative_found = self._check_narrative(contents)
            if narrative_found:
                report["narrative_violations"].append({
                    "atom": atom_key,
                    "file": atom_info["file"],
                    "patterns": narrative_found,
                    "contents": contents[:80] + "...",
                    "chars": chars,
                    "tokens": tokens,
                })
            
            # Check filter-risk language
            filter_patterns = self._check_filter_risk(contents)
            if filter_patterns:
                report["filter_risk_violations"].append({
                    "atom": atom_key,
                    "file": atom_info["file"],
                    "patterns": filter_patterns,
                    "contents": contents[:80] + "...",
                    "chars": chars,
                    "tokens": tokens,
                })
            
            # Check character limits
            if chars > 300:
                report["character_limit_violations"].append({
                    "atom": atom_key,
                    "file": atom_info["file"],
                    "chars": chars,
                    "tokens": tokens,
                    "over_by": chars - 300,
                })
            
            # Identify token-heavy atoms
            if tokens > 80:
                report["token_heavy_atoms"].append({
                    "atom": atom_key,
                    "file": atom_info["file"],
                    "tokens": tokens,
                    "chars": chars,
                    "efficiency": tokens / max(chars, 1),
                })
        
        # Sort by severity
        report["narrative_violations"].sort(key=lambda x: len(x["patterns"]), reverse=True)
        report["filter_risk_violations"].sort(key=lambda x: len(x["patterns"]), reverse=True)
        report["character_limit_violations"].sort(key=lambda x: x["over_by"], reverse=True)
        report["token_heavy_atoms"].sort(key=lambda x: x["tokens"], reverse=True)
        
        return report
    
    def _check_narrative(self, contents: str) -> List[str]:
        """Find narrative language patterns (word boundaries to avoid false positives)"""
        import re
        found = []
        lower = contents.lower()
        for pattern in self.NARRATIVE_PATTERNS.keys():
            # Use word boundary to avoid matching substrings (e.g., "strained" shouldn't match "trained")
            if re.search(r'\b' + re.escape(pattern) + r'\b', lower):
                found.append(pattern)
        return found
    
    def _check_filter_risk(self, contents: str) -> List[str]:
        """Find filter-risk language that needs replacement (word boundaries)"""
        import re
        filter_risk = {
            "exhausted": "fatigued",
            "resigned": "composed",
            "withdrawn": "reserved",
            "vacant": "unfocused",
            "trained": "practiced",
            "broken": "diminished",
            "conditioned": "prepared",
            "obedient": "cooperative",
            "complying": "obliging",
        }
        found = []
        lower = contents.lower()
        for risky, replacement in filter_risk.items():
            # Use word boundary to avoid matching substrings (e.g., "strained" shouldn't match "trained")
            if re.search(r'\b' + re.escape(risky) + r'\b', lower):
                found.append(f"{risky} → {replacement}")
        return found
    
    def generate_report(self, report: Dict[str, Any]) -> str:
        """Generate formatted violation report"""
        lines = []
        lines.append("╔════════════════════════════════════════════════════════════╗")
        lines.append("║        VIOLATION DETAIL & REMEDIATION REPORT               ║")
        lines.append("╚════════════════════════════════════════════════════════════╝")
        lines.append("")
        
        # Narrative violations
        if report["narrative_violations"]:
            lines.append(f"⚠️  NARRATIVE LANGUAGE VIOLATIONS ({len(report['narrative_violations'])})")
            lines.append("─" * 60)
            for v in report["narrative_violations"][:10]:
                lines.append(f"  {v['atom']:<40} [{v['file']}]")
                lines.append(f"    Patterns: {', '.join(v['patterns'][:3])}")
                lines.append(f"    Fix: Replace with observable facts")
                lines.append(f"    Content: {v['contents']}")
                lines.append("")
        
        # Filter-risk violations
        if report["filter_risk_violations"]:
            lines.append(f"🚨 FILTER-RISK LANGUAGE ({len(report['filter_risk_violations'])})")
            lines.append("─" * 60)
            for v in report["filter_risk_violations"][:10]:
                lines.append(f"  {v['atom']:<40} [{v['file']}]")
                for replacement in v["patterns"]:
                    lines.append(f"    Apply: {replacement}")
                lines.append(f"    Content: {v['contents']}")
                lines.append("")
        
        # Character limit violations
        if report["character_limit_violations"]:
            lines.append(f"📏 CHARACTER LIMIT VIOLATIONS ({len(report['character_limit_violations'])})")
            lines.append("─" * 60)
            for v in report["character_limit_violations"]:
                lines.append(f"  {v['atom']:<40} {v['chars']} chars (over by {v['over_by']})")
                lines.append(f"    Tokens: {v['tokens']} | File: {v['file']}")
            lines.append("")
        
        # Token-heavy atoms (candidates for trim)
        if report["token_heavy_atoms"]:
            lines.append(f"💾 HEAVIEST ATOMS - TRIM CANDIDATES")
            lines.append("─" * 60)
            heaviest = report["token_heavy_atoms"][:15]
            for v in heaviest:
                lines.append(f"  {v['atom']:<40} {v['tokens']:3} tokens")
                lines.append(f"    File: {v['file']} | Efficiency: {v['efficiency']:.3f} tokens/char")
            lines.append("")
        
        lines.append("═" * 60)
        lines.append(f"Analysis complete. Tiktoken: {TIKTOKEN_AVAILABLE}")
        lines.append("")
        
        return "\n".join(lines)
    
    def save_report(self, report: Dict[str, Any], filename: str = "VIOLATION_DETAIL_REPORT.md"):
        """Save detailed report to file"""
        report_text = self.generate_report(report)
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(report_text)
        print(f"✓ Detailed report saved to {filename}")


def run_violation_analysis():
    """Main function to run violation analysis"""
    analyzer = ViolationAnalyzer()
    report = analyzer.analyze_all()
    report_text = analyzer.generate_report(report)
    print(report_text)
    analyzer.save_report(report)
    return report


if __name__ == "__main__":
    run_violation_analysis()
