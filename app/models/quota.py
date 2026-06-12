import enum
import uuid
from datetime import datetime
from sqlalchemy import BigInteger, DateTime, Enum, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.base import Base


class TierType(str, enum.Enum):
    ALWAYS_FREE  = "always_free"
    TWELVE_MONTH = "twelve_month"
    PAID         = "paid"


class QuotaSnapshot(Base):
    __tablename__ = "quota_snapshots"

    connection_id: Mapped[uuid.UUID]       = mapped_column(UUID(as_uuid=True), ForeignKey("cloud_connections.id"), nullable=False)
    used_bytes:    Mapped[int]             = mapped_column(BigInteger, default=0)
    free_bytes:    Mapped[int]             = mapped_column(BigInteger, default=0)
    limit_bytes:   Mapped[int]             = mapped_column(BigInteger, default=0)
    tier_type:     Mapped[TierType]        = mapped_column(Enum(TierType), default=TierType.ALWAYS_FREE)
    expires_at:    Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    polled_at:     Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)

    connection: Mapped["CloudConnection"] = relationship(back_populates="quota_snapshots")
