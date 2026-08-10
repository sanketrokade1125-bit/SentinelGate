from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.app.database import get_db
from backend.app.models.vulnerability import Vulnerability
from backend.app.schemas.vulnerability import VulnerabilityResponse


router = APIRouter(
    prefix="/api/vulnerabilities",
    tags=["Vulnerabilities"],
)


@router.get("/", response_model=list[VulnerabilityResponse])
def get_vulnerabilities(db: Session = Depends(get_db)):
    vulnerabilities = db.query(Vulnerability).all()
    return vulnerabilities


@router.get(
    "/{vulnerability_id}",
    response_model=VulnerabilityResponse,
)
def get_vulnerability(
    vulnerability_id: int,
    db: Session = Depends(get_db),
):
    vulnerability = (
        db.query(Vulnerability)
        .filter(Vulnerability.id == vulnerability_id)
        .first()
    )

    if vulnerability is None:
        raise HTTPException(
            status_code=404,
            detail="Vulnerability not found",
        )

    return vulnerability