from datetime import datetime

from pydantic import BaseModel, ConfigDict


class IncidentResponse(BaseModel):
    id: int
    title: str
    attack_type: str
    severity: str
    risk_score: float | None = None
    status: str
    description: str | None = None
    asset_id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)