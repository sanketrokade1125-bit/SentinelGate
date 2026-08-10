from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.app.database import get_db
from backend.app.services.vulnerability_risk_service import (
    calculate_vulnerability_risk,
)


router = APIRouter(
    prefix="/api/risk",
    tags=["Risk Analysis"],
)


@router.get(
    "/vulnerability/{vulnerability_id}",
)
def get_vulnerability_risk(
    vulnerability_id: int,
    db: Session = Depends(get_db),
):
    return calculate_vulnerability_risk(
        vulnerability_id=vulnerability_id,
        db=db,
    )