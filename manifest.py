import os

OUTPUT_FILENAME = "project_context.md"

SOURCE_DIRS = ['.', 'definitions']

IGNORE_DIRS = {
    '__pycache__', '.git', 'venv', 'archive', 'docs', 
    'reports', 'camera_work', '.idea', '.vscode'
}

IGNORE_FILES = {
    'project_tree.txt', 'json_manifest.txt', 'analytics_output.txt', 
    'analytics_run.txt', 'test_output.txt', 'generation_history.json',
    'prompt.txt', 'make_snapshot.py', 'packer.py', 'get_tree.py', 
    'pack_jsons.py', 'project_context.md'
}

INCLUDE_EXTS = {'.py', '.json', '.md', '.txt'}

def generate_snapshot():
    print(f"📸 Taking snapshot of project...")
    
    all_content = []
    file_list = []
    
    for source_dir in SOURCE_DIRS:
        if not os.path.exists(source_dir):
            continue
            
        for root, dirs, files in os.walk(source_dir):
            dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]
            
            files.sort()
            
            for file in files:
                if file in IGNORE_FILES or file == OUTPUT_FILENAME:
                    continue
                
                ext = os.path.splitext(file)[1]
                if ext not in INCLUDE_EXTS:
                    continue
                
                filepath = os.path.join(root, file)
                relpath = os.path.relpath(filepath, '.')
                
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read()
                        
                    lang = ext.lstrip('.')
                    header = f"\n## FILE: {relpath}\n```{lang}\n"
                    footer = "\n```\n"
                    
                    all_content.append(header + content + footer)
                    file_list.append(relpath)
                    print(f"  + Packed: {relpath}")
                    
                except Exception as e:
                    print(f"  - Skipping {relpath}: {e}")

    full_text = "".join(all_content)
    total_chars = len(full_text)
    
    if total_chars == 0:
        print("\n❌ No files found! Check your settings.")
        return

    print(f"\n📦 Total content: {total_chars:,} characters")
    
    manifest = "# MANIFEST OF INCLUDED FILES:\n" + "\n".join([f"- {f}" for f in file_list]) + "\n\n"
    final_output = manifest + full_text
    
    with open(OUTPUT_FILENAME, 'w', encoding='utf-8') as f:
        f.write(final_output)
            
    print(f"  -> Created: {OUTPUT_FILENAME}")

    print(f"\n✅ Done! Full project context saved to {OUTPUT_FILENAME}.")

if __name__ == "__main__":
    generate_snapshot()