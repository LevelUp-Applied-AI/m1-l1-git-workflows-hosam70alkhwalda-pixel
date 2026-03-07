# AGENTS.md — [FILL IN: Project Name] AI Agent Governance

> This file defines the rules, constraints, and boundaries for AI agents (Claude, Copilot, Cursor, etc.)
> working in this repository. Any agent reading this file must follow the rules below before taking action.
>
> Last updated: [FILL IN: YYYY-MM-DD]

---

## Scope

[FILL IN: Describe what AI agents are authorized to do in this repo. Be specific:
- Which files may an agent read, modify, or create?
- Which directories are in scope?
- What kinds of tasks can an agent perform autonomously?]

**Example format:**
> Agents may read any file in this repository. Agents may modify `requirements.txt`, `setup.sh`,
> and files in `src/`. Agents may suggest changes to `README.md` but must not modify `AGENTS.md`
> or `.github/` without explicit instruction from a human.

---

## Constraints

[FILL IN: List the rules and limitations agents must follow. Consider:
- Code style and formatting requirements
- Package management rules
- Commit and branch conventions
- Environment and configuration assumptions
- Anything that would break the project if an agent got it wrong]

**Example format:**
> - Do not add packages to `requirements.txt` without verifying they are in the course stack plan.
> - All code changes must be compatible with Python 3.11.
> - Never commit secrets, credentials, or `.env` files.
> - Follow the branch naming convention: `feature/description` or `fix/description`.

---

## Testing Requirements

[FILL IN: What must an agent verify before proposing or completing a change? Be specific:
- What test or verification commands must pass?
- What does "done" look like for this project?
- What is the minimum bar before an agent should consider a task complete?]

**Example format:**
> Before proposing any change as complete, an agent must:
> 1. Run `bash setup.sh` — must exit 0.
> 2. Run `pytest tests/ -v` — all tests must pass.
> 3. Confirm no `.venv/`, `.env`, or `__pycache__/` files are staged for commit.

---

## Boundaries

[FILL IN: What is explicitly off-limits? Describe decisions that require human judgment and actions
that should never be taken autonomously. Consider:
- Sensitive files (credentials, environment files)
- External system actions (pushing to remote, opening PRs, sending messages)
- Files that must not be modified without explicit instruction
- Decisions with grading, scoring, or high-stakes consequences]

**Example format:**
> - Never read, write, or modify `.env` files or any file containing credentials.
> - Never push to remote branches or open pull requests without explicit human instruction.
> - Never modify `AGENTS.md`, `CHANGELOG.md`, or grading rubrics autonomously.
> - If a task requires deleting tracked files, stop and ask for confirmation.
