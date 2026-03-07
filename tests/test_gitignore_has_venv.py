"""
Autograder — lab-1-git-workflows
Check: .gitignore excludes the .venv/ directory.
"""

from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent


def test_gitignore_excludes_venv():
    gitignore = REPO_ROOT / ".gitignore"
    assert gitignore.exists(), ".gitignore is missing from the repo root"

    contents = gitignore.read_text(encoding="utf-8")

    assert ".venv" in contents, (
        "'.venv' or '.venv/' not found in .gitignore. "
        "Add '.venv/' on its own line to prevent committing your virtual environment. "
        "This is the most critical .gitignore entry for this lab."
    )


def test_venv_directory_not_tracked():
    """
    Confirm the .venv directory itself was not committed.
    If .venv/ exists in the repo, it was committed before .gitignore excluded it.
    """
    venv_dir = REPO_ROOT / ".venv"
    if venv_dir.exists():
        # It exists on disk, but is it tracked by git?
        # In CI (GitHub Actions), the checkout only includes tracked files.
        # If .venv/ appears here in CI, it was committed.
        import subprocess
        result = subprocess.run(
            ["git", "ls-files", ".venv"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
        )
        tracked_venv_files = result.stdout.strip()
        assert not tracked_venv_files, (
            "The .venv directory appears to be tracked by Git. "
            "Run: git rm -r --cached .venv/ && git commit -m 'Remove .venv from tracking'"
        )
