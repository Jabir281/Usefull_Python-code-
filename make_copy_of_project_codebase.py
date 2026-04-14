import os
from pathlib import Path

def export_project(root_dir=".", output_file="project_dump.txt"):
    ignore = {'.git', 'node_modules', 'dist', 'build', '__pycache__', '.next', 'venv'}
    extensions = {'.js', '.jsx', '.ts', '.tsx', '.json', '.css', '.html', '.env', '.md', '.prisma'}
    
    with open(output_file, 'w', encoding='utf-8') as out:
        # Write file tree first
        out.write("PROJECT STRUCTURE:\n")
        out.write("==================\n")
        for path in sorted(Path(root_dir).rglob('*')):
            if any(ig in path.parts for ig in ignore):
                continue
            depth = len(path.relative_to(root_dir).parts) - 1
            if path.is_dir():
                out.write(f"{'  ' * depth}📁 {path.name}/\n")
            else:
                out.write(f"{'  ' * depth}📄 {path.name}\n")
        
        # Write file contents
        out.write("\n\nFILE CONTENTS:\n")
        out.write("==============\n")
        
        for path in sorted(Path(root_dir).rglob('*')):
            if any(ig in path.parts for ig in ignore):
                continue
            if path.is_file() and path.suffix in extensions:
                relative_path = path.relative_to(root_dir)
                out.write(f"\n\n=== {relative_path} ===\n")
                try:
                    with open(path, 'r', encoding='utf-8') as f:
                        out.write(f.read())
                except Exception as e:
                    out.write(f"[Error reading file: {e}]")
    
    print(f"✅ Project exported to {output_file}")
    print(f"📋 Now copy the contents of {output_file} and paste it here!")

if __name__ == "__main__":
    export_project()
