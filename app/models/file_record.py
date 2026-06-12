import enum
import uuid
from sqlalchemy import String, BigInteger, Boolean, Enum, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.base import Base


class FileStatus(str, enum.Enum):
    PENDING = "pending"
    ACTIVE  = "active"
    DELETED = "deleted"


class FileRecord(Base):
    __tablename__ = "file_records"

    user_id:         Mapped[uuid.UUID]   = mapped_column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    connection_id:   Mapped[uuid.UUID]   = mapped_column(UUID(as_uuid=True), ForeignKey("cloud_connections.id"), nullable=False)
    object_key:      Mapped[str]         = mapped_column(String(1024), nullable=False)
    original_name:   Mapped[str]         = mapped_column(String(512), nullable=False)
    size_bytes:      Mapped[int]         = mapped_column(BigInteger, default=0)
    mime_type:       Mapped[str | None]  = mapped_column(String(127), nullable=True)
    checksum_sha256: Mapped[str | None]  = mapped_column(String(64), nullable=True)
    status:          Mapped[FileStatus]  = mapped_column(Enum(FileStatus), default=FileStatus.PENDING)
    is_chunked:      Mapped[bool]        = mapped_column(Boolean, default=False)

    user:       Mapped["User"]            = relationship(back_populates="file_records")
    connection: Mapped["CloudConnection"] = relationship(back_populates="file_records")
