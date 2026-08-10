from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.app.database import get_db
from backend.app.models.security_event import SecurityEvent
from backend.app.schemas.security_event import SecurityEventResponse


router = APIRouter(
    prefix="/api/security-events",
    tags=["Security Events"],
)


@router.get(
    "/",
    response_model=list[SecurityEventResponse],
)
def get_security_events(db: Session = Depends(get_db)):
    events = (
        db.query(SecurityEvent)
        .order_by(SecurityEvent.timestamp.desc())
        .all()
    )

    return events


@router.get(
    "/{event_id}",
    response_model=SecurityEventResponse,
)
def get_security_event(
    event_id: int,
    db: Session = Depends(get_db),
):
    event = (
        db.query(SecurityEvent)
        .filter(SecurityEvent.id == event_id)
        .first()
    )

    if event is None:
        raise HTTPException(
            status_code=404,
            detail="Security event not found",
        )

    return event