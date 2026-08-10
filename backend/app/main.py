from fastapi import FastAPI
from backend.app.config import settings
from backend.app.database import init_db

app = FastAPI(
    title=settings.app_name,
    version="0.1.0",
    description="AI-powered cyber risk intelligence platform.",
)

@app.on_event("startup")
def startup_event():
    init_db()

@app.get("/")
def root():
    return {
        "project": settings.app_name,
        "version": "0.1.0",
        "status": "running",
        "phase": "Phase 1",
    }

@app.get("/health")
def health():
    return {"status": "healthy"}
