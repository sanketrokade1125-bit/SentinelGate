from datetime import datetime

from pydantic import BaseModel, ConfigDict


class SecurityEventResponse(BaseModel):
    id: int
    timestamp: datetime
    event_type: str
    source_ip: str | None = None
    destination_ip: str | None = None
    severity: str
    description: str | None = None
    asset_id: int

    model_config = ConfigDict(from_attributes=True)