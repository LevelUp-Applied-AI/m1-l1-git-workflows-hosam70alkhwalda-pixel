# AGENTS.md

## Testing Requirements

All changes must pass `python test_environment.py` before committing.

Any code added to `src/` must include tests that pass with:

pytest tests/ -v


## Secrets Policy

Do not include API keys, passwords, database credentials, or
any sensitive information in prompts or commits.

Never commit:
- .env
- *.key
- *.pem
- any file containing credentials


## Scope Boundaries

Agents may edit:

- src/
- notebooks/
- tests/

Agents must NOT modify:

- requirements.txt without human review
- setup.sh without testing locally
- .gitignore unless verifying it will not ignore source files


## Reproducibility Standard

All AI-assisted changes must be executed locally before committing.

The code must run successfully and produce the expected output.

"The AI generated it" is not a valid reason to commit code that has not been tested.