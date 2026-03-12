# AGENTS.md

## Testing Requirements

All changes must pass `python test_environment.py` before committing.

Any new code added to `src/` must include tests inside `tests/`
and pass the command:

pytest tests/ -v

## Secrets Policy

Never include API keys, database credentials, private data,
or environment secrets in prompts or commits.

Files that must never be committed:

.env  
*.key  
*.pem  

Data files such as raw hospital datasets must also remain
outside version control.

## Scope Boundaries

AI agents may edit the following directories:

src/  
notebooks/  

Agents must NOT modify:

requirements.txt without human approval  
setup.sh without testing locally  
.gitignore without verifying it does not exclude source code

## Reproducibility Standard

All AI-assisted changes must run locally before committing.

The project must successfully run:

python test_environment.py

before any commit is pushed.

AI-generated code must always be tested locally before
being committed to the repository.