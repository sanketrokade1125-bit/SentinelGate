from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.app.database import Base


class SecurityEvent(Base):
    __tablename__ = "security_events"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )

    timestamp: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        default=datetime.utcnow
    )

    event_type: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    source_ip: Mapped[str | None] = mapped_column(
        String(45),
        nullable=True
    )

    destination_ip: Mapped[str | None] = mapped_column(
        String(45),
        nullable=True
    )

    severity: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
        default="LOW"
    )

    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )

    asset_id: Mapped[int] = mapped_column(
        ForeignKey("assets.id"),
        nullable=False
    )

    asset = relationship(
        "Asset",
        back_populates="security_events"
    )