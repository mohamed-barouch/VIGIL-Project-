# Vigil

An AI-assisted backend monitoring platform. It watches the activity of a backend, detects abnormal or suspicious behavior, investigates the cause, and alerts developers with evidence.

> Status: early development (phase 0). The project is being built in public, step by step.

## Planned features
- Collect request events from any backend through a small middleware
- Store events and show them in a live dashboard
- Detect anomalies (error spikes, latency drift, failed-login bursts)
- Draft an explanation of the likely cause with an LLM
- Send alerts to Telegram or email

## Current state
- FastAPI app with two endpoints: `GET /health` and `GET /products` (sample data)

## Run it locally
```bash
cd backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1   # Windows PowerShell
pip install -r requirements.txt
fastapi dev main.py
```
Then open http://127.0.0.1:8000/docs

## Tech stack (planned)
Python, FastAPI, PostgreSQL, Redis, React, Docker, GitHub Actions