"""
Autograder — lab-1-git-workflows
Check: required files present and README is non-empty.
"""

from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent


def test_requirements_txt_present():
    f = REPO_ROOT / "requirements.txt"
    assert f.exists(), "requirements.txt is missing from the repo root"
    assert f.stat().st_size > 0, "requirements.txt is empty"


def test_readme_present():
    f = REPO_ROOT / "README.md"
    assert f.exists(), "README.md is missing from the repo root"


def test_readme_nonempty():
    f = REPO_ROOT / "README.md"
    assert f.exists(), "README.md is missing"
    content = f.read_text(encoding="utf-8")
    assert len(content) > 50, (
        f"README.md is too short ({len(content)} bytes) — "
        "it appears to be just a title line. Add a brief project description."
    )


def test_gitignore_present():
    f = REPO_ROOT / ".gitignore"
    assert f.exists(), ".gitignore is missing from the repo root"


def test_test_environment_py_present():
    f = REPO_ROOT / "test_environment.py"
    assert f.exists(), (
        "test_environment.py is missing. "
        "This file is provided in the starter repo — do not delete it."
    )
