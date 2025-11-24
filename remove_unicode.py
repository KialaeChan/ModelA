#!/usr/bin/env python3
import json
import os
import glob

# Unicode replacements
REPLACEMENTS = {
    'é': 'e', 'è': 'e', 'ê': 'e', 'ë': 'e',
    'à': 'a', 'â': 'a', 'ä': 'a',
    'ñ': 'n',
    'ü': 'u', 'û': 'u', 'ù': 'u',
    'ö': 'o', 'ô': 'o', 'ò': 'o',
    'ï': 'i', 'î': 'i', 'ì': 'i',
    ''': "'", ''': "'",
    '"': '"', '"': '"',
    '—': '-', '–': '-',
    'ç': 'c',
}

def remove_unicode(text):
    """Replace unicode characters with ASCII equivalents."""
    for unicode_char, ascii_char in REPLACEMENTS.items():
        text = text.replace(unicode_char, ascii_char)
    return text

def process_json_file(filepath):
    """Process a single JSON file to remove unicode."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_len = len(content)
    cleaned = remove_unicode(content)
    
    if cleaned != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(cleaned)
        print(f"✓ Cleaned {filepath} ({original_len - len(cleaned)} unicode chars removed)")
        return True
    return False

# Process all JSON files in definitions directory
definitions_dir = '/home/claude/ModelA/definitions'
json_files = glob.glob(os.path.join(definitions_dir, '*.json'))

cleaned_count = 0
for filepath in json_files:
    if process_json_file(filepath):
        cleaned_count += 1

print(f"\n{cleaned_count} files cleaned of unicode characters")
