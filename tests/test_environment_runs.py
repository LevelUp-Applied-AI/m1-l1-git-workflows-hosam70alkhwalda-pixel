"""
Autograder — lab-1-git-workflows
Check: test_environment.py runs successfully and prints "Environment OK".
"""

import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent


def test_test_environment_script_passes():
    """
    Run test_environment.py using the current Python interpreter.
    In CI, this is the venv Python after 'pip install -r requirements.txt'.
    Expects: exit code 0 and "Environment OK" in stdout.
    """
    script = REPO_ROOT / "test_environment.py"
    assert script.exists(), (
        "test_environment.py is missing. "
        "This file is provided in the starter repo — do not delete it."
    )

    result = subprocess.run(
        [sys.executable, str(script)],
        capture_output=True,
        text=True,
        cwd=REPO_ROOT,
    )

    assert result.returncode == 0, (
        f"test_environment.py exited with code {result.returncode}.\n"
        f"stderr: {result.stderr.strip()}\n"
        f"stdout: {result.stdout.strip()}\n\n"
        "Confirm your requirements.txt contains 'pandas' and 'matplotlib', "
        "and that they installed without errors."
    )

    assert "Environment OK" in result.stdout, (
        f"'Environment OK' not found in test_environment.py output.\n"
        f"stdout: {result.stdout.strip()}\n"
        "The script ran but did not print the expected confirmation message."
    )
