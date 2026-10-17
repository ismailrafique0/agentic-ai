# Agentic AI Course

This repository contains small, separate student apps built for the Agentic AI course. Each app lives in its own subfolder (e.g., `week01/`) with its own `.venv` and `.env`.

## Structure

- `week01/` — Student Information System
- `.gitignore` — excludes `.venv/`, `.env`, caches

## Running an App

```bash
cd week01
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m src.student_app.main
pytest
```