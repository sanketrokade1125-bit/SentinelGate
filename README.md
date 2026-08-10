# SentinelGate
AI-Powered Cyber Risk Intelligence and Threat Prioritization Platform.

## Phase 1
Development environment, project structure, configuration, database foundation, and minimal FastAPI backend.

## Run
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r backend\requirements.txt
uvicorn backend.app.main:app --reload
```

Open http://127.0.0.1:8000 and http://127.0.0.1:8000/docs
