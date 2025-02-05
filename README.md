# 🗂 Dynamic Folder Structure Builder

A Python tool to generate complex folder structures with files using JSON configuration. Perfect for automating project setups!

![Folder Structure Example](screenshots/folder_structure.png)

## ✨ Features
- **Dynamic Variables** (e.g., `{{n}}`, `{{timestamp}}`)
- **Nested Subfolders** (Unlimited depth)
- **Batch Creation** (Number ranges: 1-30, etc.)
- **Auto File Creation** (Custom content/extensions)
- **Dry Run Mode** (Preview without changes)

## 🚀 Quick Start
```bash
# Clone repo
git clone https://github.com/yourusername/folder-structure-builder.git
cd folder-structure-builder

# Install requirements
pip install -r requirements.txt
```

## 🛠 Usage
### Basic Command
```bash
python structure_builder.py --config config.json
```

### Advanced Example
```bash
# Create 50 folders with dry run
python structure_builder.py \
  --config config.json \
  --path "C:/Projects" \
  --var client=Acme \
  --dry-run
```

## 📝 Sample Config (config.json)
```json
{
  "structure": [
    {
      "name": "Project_{{n}}",
      "subfolders": [
        {
          "name": "Assets",
          "subfolders": ["Raw", "Processed"]
        },
        {
          "name": "Docs",
          "files": [
            { "name": "Specs_{{n}}.md", "content": "# Project {{n}} Details" }
          ]
        }
      ],
      "repeat": {
        "var": "n",
        "start": 1,
        "end": 5
      }
    }
  ]
}
```

## 🔧 CLI Options
| Option | Description | Example |
|--------|-------------|---------|
| `--config` | Path to JSON config | `--config my_config.json` |
| `--path` | Base output path | `--path "D:/Projects"` |
| `--var` | Custom variables | `--var project=Demo` |
| `--dry-run` | Preview mode | `--dry-run` |

## 🤝 Contributing
1. Fork the repository
2. Create your feature branch:  
   `git checkout -b feature/amazing-feature`
3. Commit changes:  
   `git commit -m 'Add amazing feature'`
4. Push to branch:  
   `git push origin feature/amazing-feature`
5. Open a Pull Request

## 📜 License
© 2025 Sina Nozhati
