from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Float, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.app.database import Base


class Incident(Base):
    __tablename__ = "incidents"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )

    title: Mapped[str] = mapped_column(
        String(200),
        nullable=False
    )

    attack_type: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    severity: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
        default="LOW"
    )

    risk_score: Mapped[float | None] = mapped_column(
        Float,
        nullable=True
    )

    status: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
        default="OPEN"
    )

    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )

    asset_id: Mapped[int] = mapped_column(
        ForeignKey("assets.id"),
        nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        default=datetime.utcnow
    )

    asset = relationship(
        "Asset",
        back_populates="incidents"
    )