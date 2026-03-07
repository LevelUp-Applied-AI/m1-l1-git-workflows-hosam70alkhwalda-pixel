"""
Autograder — integration-1-dev-environment
Structural checks: required files present and non-empty.
This integration task is rubric-graded; these checks confirm deliverables exist.
"""

from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent


def test_readme_present_and_substantial():
    readme = REPO_ROOT / "README.md"
    assert readme.exists(), (
        "README.md is missing. "
        "Replace the starter README.md with your completed 7-section version."
    )
    content = readme.read_text(encoding="utf-8")
    assert len(content) >= 300, (
        f"README.md is present but very short ({len(content)} bytes). "
        "A complete 7-section README should be substantially longer. "
        "Confirm you replaced the template content with your actual project documentation."
    )


def test_gitignore_present_and_has_venv():
    gitignore = REPO_ROOT / ".gitignore"
    assert gitignore.exists(), ".gitignore is missing from the repo root."
    contents = gitignore.read_text(encoding="utf-8")
    assert ".venv" in contents, (
        "'.venv' not found in .gitignore. "
        "This is required — add '.venv/' to prevent committing your virtual environment."
    )


def test_setup_sh_present():
    setup = REPO_ROOT / "setup.sh"
    assert setup.exists(), (
        "setup.sh is missing. "
        "Rename setup.sh.template to setup.sh and fill in the required content."
    )
    content = setup.read_text(encoding="utf-8")
    assert "set -euo pipefail" in content, (
        "'set -euo pipefail' not found in setup.sh. "
        "This line is required — it makes the script exit immediately on any error."
    )


def test_agents_md_present_and_has_sections():
    agents = REPO_ROOT / "AGENTS.md"
    assert agents.exists(), (
        "AGENTS.md is missing. "
        "Rename AGENTS.md.template to AGENTS.md and fill in all four required sections."
    )
    contents = agents.read_text(encoding="utf-8")
    assert len(contents) >= 200, (
        f"AGENTS.md is present but very short ({len(contents)} bytes). "
        "All four sections (Scope, Constraints, Testing Requirements, Boundaries) "
        "must contain substantive content — not just the template placeholder text."
    )


def test_changelog_md_present():
    changelog = REPO_ROOT / "CHANGELOG.md"
    assert changelog.exists(), (
        "CHANGELOG.md is missing. "
        "Create CHANGELOG.md with at least one initial entry documenting this project setup."
    )
    content = changelog.read_text(encoding="utf-8")
    assert len(content) >= 50, (
        "CHANGELOG.md is present but nearly empty. "
        "Add at least one dated entry describing what you set up."
    )


def test_requirements_txt_present():
    req = REPO_ROOT / "requirements.txt"
    assert req.exists(), (
        "requirements.txt is missing from the repo root. "
        "Add a requirements.txt listing your project dependencies."
    )
