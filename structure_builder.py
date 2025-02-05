import os
import argparse
import json
from pathlib import Path
from datetime import datetime

def create_structure(config_path: str, base_path: str, variables: dict, dry_run: bool = False) -> None:
    """
    Build folder/file structure based on configuration file
    """
    try:
        with open(config_path, 'r') as f:
            config = json.load(f)
    except FileNotFoundError:
        print(f"❌ Error: Config file '{config_path}' not found!")
        return
    except json.JSONDecodeError:
        print(f"❌ Error: Invalid JSON format in '{config_path}'!")
        return

    # Variable replacement
    def replace_vars(text: str, n: int) -> str:
        text = text.replace("{{n}}", str(n))
        text = text.replace("{{timestamp}}", datetime.now().strftime("%Y/%m/%d_%H:%M:%S"))
        for key, value in variables.items():
            text = text.replace(f"{{{{{key}}}}}", str(value))
        return text

    # Recursive structure builder
    def build_item(item, current_path, n):
        item_name = replace_vars(item['name'], n) if 'name' in item else ""
        item_path = Path(current_path) / item_name

        if dry_run:
            print(f"📂 [Dry Run] Folder: {item_path}")
        else:
            os.makedirs(item_path, exist_ok=True)
            print(f"📂 Folder created: {item_path}")

        if 'subfolders' in item:
            for subfolder in item['subfolders']:
                build_item(subfolder, item_path, n)

        if 'files' in item:
            for file in item['files']:
                file_name = replace_vars(file['name'], n)
                file_path = item_path / file_name
                content = replace_vars(file.get('content', ''), n)

                if dry_run:
                    print(f"📄 [Dry Run] File: {file_path}")
                else:
                    with open(file_path, 'w') as f:
                        f.write(content)
                    print(f"📄 File created: {file_path}")

    # Process structure with repetition
    for item in config['structure']:
        if 'repeat' in item:
            repeat_config = item['repeat']
            start = repeat_config.get('start', 1)
            end = repeat_config.get('end', 5)
            var_name = repeat_config.get('var', 'n')
            
            for n in range(start, end + 1):
                variables[var_name] = n
                build_item(item, base_path, n)
        else:
            build_item(item, base_path, variables.get('n', 1))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Dynamic Folder/File Structure Builder")
    parser.add_argument("--config", type=str, required=True, help="Path to config JSON file")
    parser.add_argument("--path", type=str, default=os.getcwd(), help="Base directory path")
    parser.add_argument("--var", nargs='*', help="Custom variables (e.g., --var project=MyProject)")
    parser.add_argument("--dry-run", action="store_true", help="Simulate without creating files")
    args = parser.parse_args()

    variables = {}
    if args.var:
        for var in args.var:
            key, value = var.split('=')
            variables[key] = value

    create_structure(
        config_path=args.config,
        base_path=args.path,
        variables=variables,
        dry_run=args.dry_run
    )