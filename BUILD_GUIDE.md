# Building AI Projects HTML from Markdown

This guide explains how to use the `build_projects.py` script to generate `ai-projects.html` from your `projects.md` file.

## Overview

Instead of manually editing HTML, you can now:
1. Edit `projects.md` with your project entries
2. Run `build_projects.py` to generate a static HTML file
3. Commit both files to GitHub

## Quick Start

### Prerequisites
- Python 3.6 or higher (no external libraries required!)

### Step 1: Edit Your Projects
Open `projects.md` and add your projects in markdown format:

```markdown
## Your Project Title
**Date:** 2024 - 2025

Your project description goes here. Include 2-3 sentences about 
the impact and key achievements.

**Technologies:** Tech1, Tech2, Category1, Category2

**Links:** [GitHub](https://github.com/repo), [Demo](https://demo.com)

---
```

### Step 2: Run the Build Script
```bash
python build_projects.py
```

### Step 3: Check the Output
The script will:
- ✅ Read all projects from `projects.md`
- ✅ Generate beautiful HTML cards
- ✅ Create a static `ai-projects.html` file
- ✅ Print a summary of all projects found

### Step 4: Commit and Push
```bash
git add projects.md ai-projects.html
git commit -m "Update AI projects portfolio"
git push origin main
```

## Script Features

### Markdown Format Support
The script parses this markdown structure:
- **Title**: `## Project Title`
- **Date**: `**Date:** YYYY - YYYY`
- **Description**: Regular paragraph text
- **Technologies**: `**Technologies:** Tech1, Tech2, Category1`
- **Links**: `**Links:** [Text](URL), [Another](URL)`
- **Separator**: `---` (separates projects)

### Automatic Features
- ✅ Converts markdown links to HTML
- ✅ Categorizes technologies (single-word = blue, multi-word = green)
- ✅ Escapes HTML special characters for security
- ✅ Generates responsive project cards with hover effects
- ✅ Maintains consistent styling

### No Dependencies Required!
The script uses only Python standard library:
- `re` for regex (markdown parsing)
- `os` for file operations
- `pathlib` for path handling

## File Structure

```
resume/
├── projects.md              (Your project entries - EDIT THIS)
├── build_projects.py        (Build script - RUN THIS)
├── ai-projects.html         (Generated output - AUTO-GENERATED)
└── index.html               (Main resume)
```

## Example Workflow

### 1. Start with template projects
`projects.md` comes with 3 example projects - keep or replace them

### 2. Add your projects
```markdown
## Project 4: Your New Project
**Date:** 2024

Your description here.

**Technologies:** Python, PyTorch, Machine Learning

**Links:** [GitHub](url)

---
```

### 3. Generate HTML
```bash
python build_projects.py
```

Output:
```
🚀 Building AI Projects HTML from Markdown...
📖 Reading projects.md...
✅ Found 4 projects
🎨 Generating project HTML...
📝 Building ai-projects.html...
✅ Success! Generated ai-projects.html

📊 Project Summary:
  1. Agentic AI Framework for CAE Automation (2024 - 2025)
  2. LLM-Powered Engineering Design Advisor (2024)
  3. Surrogate Model for Design Optimization (2023)
  4. Your New Project (2024)
```

### 4. Commit changes
```bash
git add projects.md ai-projects.html
git commit -m "Add new AI project: Your New Project"
git push
```

## Advantages of This Approach

| Aspect | Before (JavaScript) | After (Python Build) |
|--------|-------------------|----------------------|
| **Editing** | Edit HTML + markdown | Edit markdown only ✅ |
| **Parsing** | Client-side (slower) | Build-time (instant) ✅ |
| **Caching** | Recalculates on load | Pre-computed ✅ |
| **SEO** | Dynamic content | Static HTML ✅ |
| **Dependencies** | html2pdf library | None (stdlib only) ✅ |
| **Build time** | 0 (none) | < 1 second ✅ |

## Troubleshooting

### Issue: "projects.md not found"
**Solution**: Ensure `projects.md` is in the same directory as `build_projects.py`

### Issue: Script runs but no HTML generated
**Solution**: Check that `projects.md` has valid markdown format with `---` separators

### Issue: Projects not appearing in HTML
**Solution**: 
- Check project format (## Title, **Date:**, **Technologies:**, **Links:**)
- Ensure proper separator `---` between projects
- Run script again

### Issue: "Permission denied" on macOS/Linux
**Solution**:
```bash
chmod +x build_projects.py
python3 build_projects.py
```

## Advanced Usage

### Automated Builds (Git Hooks)

Create `.git/hooks/pre-commit`:
```bash
#!/bin/bash
python build_projects.py && git add ai-projects.html
```

This automatically rebuilds HTML when you commit changes to `projects.md`

### GitHub Actions (Optional)

Create `.github/workflows/build-projects.yml`:
```yaml
name: Build Projects
on:
  push:
    paths:
      - 'projects.md'
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - run: python build_projects.py
      - uses: stefanzweifel/git-auto-commit-action@v4
        with:
          commit_message: 'Auto-build: Update ai-projects.html'
          file_pattern: ai-projects.html
```

## Markdown Syntax Tips

### Technology Tags
- Single word: Blue tag (standard technology)
- Multi-word: Green tag (category/domain)

Good examples:
```
**Technologies:** PyTorch, TensorFlow, Python, Agentic AI, Multi-Agent
```

### Links Format
```markdown
**Links:** [GitHub](https://github.com/repo), [Paper](https://arxiv.org), [Demo](https://demo.com)
```

### Dates
Flexible formats supported:
- `2024`
- `2024 - 2025`
- `Jan 2024 - Dec 2025`
- `2024 - Present`

## Questions?

Refer to `projects.md` for the complete markdown format examples. The file includes:
- 3 working example projects
- Template for new projects
- Guidelines for formatting
- Technology tag recommendations

---

**Last Updated:** October 2026
