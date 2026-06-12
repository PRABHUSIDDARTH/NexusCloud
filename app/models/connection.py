import enum
import uuid
from sqlalchemy import String, Boolean, Enum, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.base import Base


class Provider(str, enum.Enum):
    GCP    = "gcp"
    R2     = "r2"
    AWS    = "aws"
    AZURE  = "azure"
    B2     = "b2"
    ORACLE = "oracle"
    IBM    = "ibm"


class CloudConnection(Base):
    __tablename__ = "cloud_connections"

    user_id:         Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    provider:        Mapped[Provider]  = mapped_column(Enum(Provider), nullable=False)
    display_name:    Mapped[str]       = mapped_column(String(100), nullable=False)
    bucket_name:     Mapped[str]       = mapped_column(String(255), nullable=False)
    region:          Mapped[str | None]= mapped_column(String(100), nullable=True)
    encrypted_creds: Mapped[str]       = mapped_column(String(2048), nullable=False)
    is_active:       Mapped[bool]      = mapped_column(Boolean, default=True)

    user:            Mapped["User"]               = relationship(back_populates="connections")
    quota_snapshots: Mapped[list["QuotaSnapshot"]]= relationship(back_populates="connection", cascade="all, delete-orphan")
    file_records:    Mapped[list["FileRecord"]]   = relationship(back_populates="connection")
