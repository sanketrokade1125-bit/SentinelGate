from fastapi import FastAPI

from backend.app.config import settings
from backend.app.database import init_db
from backend.app.api.assets import router as assets_router
from backend.app.api.vulnerabilities import router as vulnerabilities_router
from backend.app.api.security_events import router as security_events_router
from backend.app.api.incidents import router as incidents_router


app = FastAPI(
    title=settings.app_name,
    version="0.1.0",
    description="AI-powered cyber risk intelligence platform.",
)


@app.on_event("startup")
def startup_event():
    init_db()


app.include_router(assets_router)
app.include_router(vulnerabilities_router)
app.include_router(security_events_router)
app.include_router(incidents_router)

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