# [FILL IN: Project Title — a short, descriptive name for your project]

> [FILL IN: One-sentence description — what does this project do, for whom, and in what context?]

---

## Project Purpose

[FILL IN: 2–4 sentences. What problem does this project address? Why is a reproducible environment important for this specific project? Who would use this repo and why?]

---

## Tech Stack

| Tool / Package | Version | Purpose |
|---|---|---|
| Python | 3.11.x | Primary language |
| [FILL IN: Package 1] | [FILL IN: e.g. 2.1.x] | [FILL IN: what it does in this project] |
| [FILL IN: Package 2] | [FILL IN: e.g. 3.8.x] | [FILL IN: what it does in this project] |

*Add a row for each package in your `requirements.txt`. Remove this italicized line when done.*

---

## Environment Setup

```bash
# Clone the repo
git clone [FILL IN: your repo URL]
cd [FILL IN: repo name]

# Create and activate venv
python -m venv .venv
source .venv/bin/activate        # Mac/Linux / Git Bash
# .venv\Scripts\activate.bat    # Windows CMD
# .venv\Scripts\Activate.ps1    # Windows PowerShell

# Install dependencies
pip install -r requirements.txt

# Verify setup
bash setup.sh
```

---

## Usage

[FILL IN: How does a teammate (or AI agent) run this project? Be specific:
- What command do they run first?
- What output should they see?
- What do they do if setup fails?]

---

## Repo Structure

```
[FILL IN: your-repo-name]/
├── README.md               ← This file
├── requirements.txt        ← Python dependencies
├── setup.sh                ← Reproducibility and verification script
├── .gitignore              ← Files excluded from version tracking
├── AGENTS.md               ← AI agent governance rules
└── CHANGELOG.md            ← Record of significant changes
```

*Add rows for any additional files or directories your project uses. Remove this italicized line when done.*

---

## AI Assistance Disclosure

[FILL IN: Describe how you used AI tools in this project. Be specific:
- Which tools did you use (e.g., Claude, GitHub Copilot, Cursor)?
- For what tasks did you use them?
- What output did you accept, what did you modify, and what did you reject?
- If you did not use any AI tools, state that explicitly.]

---

## Change History

See [CHANGELOG.md](CHANGELOG.md) for a record of significant changes to this project.
