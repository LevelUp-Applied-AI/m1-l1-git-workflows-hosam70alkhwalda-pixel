"""
Autograder — lab-1-git-workflows
Check: requirements.txt contains the required packages.
"""

from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
REQUIRED_PACKAGES = ["pandas", "matplotlib"]


def _read_requirements():
    req_file = REPO_ROOT / "requirements.txt"
    assert req_file.exists(), "requirements.txt is missing"
    return req_file.read_text(encoding="utf-8").lower()


def test_requirements_contains_pandas():
    contents = _read_requirements()
    assert "pandas" in contents, (
        "'pandas' not found in requirements.txt. "
        "Add 'pandas' on its own line (lowercase)."
    )


def test_requirements_contains_matplotlib():
    contents = _read_requirements()
    assert "matplotlib" in contents, (
        "'matplotlib' not found in requirements.txt. "
        "Add 'matplotlib' on its own line (lowercase)."
    )


def test_requirements_not_just_comments():
    contents = _read_requirements()
    non_comment_lines = [
        line.strip()
        for line in contents.splitlines()
        if line.strip() and not line.strip().startswith("#")
    ]
    assert len(non_comment_lines) >= 1, (
        "requirements.txt contains only comments. "
        "Add your required packages (e.g., 'pandas', 'matplotlib')."
    )
