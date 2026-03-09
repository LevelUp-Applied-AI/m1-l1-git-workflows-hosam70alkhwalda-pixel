[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/FdVrU54p)
#  Hospital Admission Records Analysis

> **Lab 1 starter repo** — Replace the heading above with your project title. Team member names are not part of the lab — they go in Section 2 of your completed README in the integration task.

---

## Project Overview

This lab focuses on setting up a reproducible Python project environment using Git and virtual environments.
The goal is to ensure that any team member can quickly recreate the development environment and run the project without configuration issues.

The setup includes creating a requirements.txt file for project dependencies, configuring .gitignore to exclude unnecessary files such as .venv, and verifying that the environment works correctly using test_environment.py.

By completing this setup, the project environment can be created with only a few commands, ensuring consistency across all team members.

---

## Setup Instructions

TODO: Complete these setup steps after creating your `requirements.txt`:

```bash
python -m venv .venv

# Activate — choose the command for your OS:
# Mac / Linux:      source .venv/bin/activate
# Windows Git Bash: source .venv/Scripts/activate
# Windows CMD:      .venv\Scripts\activate.bat
# Windows PowerShell: .venv\Scripts\Activate.ps1

pip install -r requirements.txt
python test_environment.py    # should print "Environment OK"
```

---

## Contributing

- Branch naming: `setup/`, `feature/`, `fix/`
- Open a PR to `main` for all changes
- Commit messages: imperative mood, ≤ 50 characters

---

*Starter file for Lab 1 — lab-1-git-workflows | aispire-14005*