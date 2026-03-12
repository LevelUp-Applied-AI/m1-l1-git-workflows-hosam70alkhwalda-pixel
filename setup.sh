#!/usr/bin/env bash
set -euo pipefail

python -m venv .venv
source .venv/Scripts/activate # if in environment is activated in the same one this line will return an error.
pip install -r requirements.txt
python test_environment.py
echo "Setup complete."