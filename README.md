# py-calc (CLI Calculator)

A simple CLI calculator built to practice:
- Git & GitHub workflow
- Python virtual environment
- Unit testing (pytest)
- Logging (LOG_LEVEL env var)
- Docker
---
## Run locally (Linux)
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install pytest
PYTHONPATH=src python3 src/calculator/cli.py
```
---
## Run tests
```bash
PYTHONPATH=src pytest -q
```
---
## Run with logs
```bash
LOG_LEVEL=DEBUG PYTHONPATH=src python3 src/calculator/cli.py
```
---
## Run with Docker
```bash
docker build -t py-calc:1.0 .
docker run -it --rm -e LOG_LEVEL=DEBUG py-calc:1.0
```
---

