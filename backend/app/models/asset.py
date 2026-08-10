from sqlalchemy import Boolean, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.app.database import Base


class Asset(Base):
    __tablename__ = "assets"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    asset_type: Mapped[str] = mapped_column(String(50), nullable=False)
    ip_address: Mapped[str | None] = mapped_column(String(45), nullable=True)
    criticality: Mapped[int] = mapped_column(Integer, default=3, nullable=False)
    internet_exposed: Mapped[bool] = mapped_column(
        Boolean, default=False, nullable=False
    )
    owner: Mapped[str | None] = mapped_column(String(100), nullable=True)

    vulnerabilities = relationship(
        "Vulnerability",
        back_populates="asset",
        cascade="all, delete-orphan",
    )

    security_events = relationship(
        "SecurityEvent",
        back_populates="asset",
        cascade="all, delete-orphan",
    )

    incidents = relationship(
        "Incident",
        back_populates="asset",
        cascade="all, delete-orphan",
    )