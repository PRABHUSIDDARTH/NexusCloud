import enum
import uuid
from sqlalchemy import String, Enum, ForeignKey
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.base import Base


class AuditAction(str, enum.Enum):
    UPLOAD            = "upload"
    DOWNLOAD          = "download"
    DELETE            = "delete"
    CONNECT           = "connect"
    DISCONNECT        = "disconnect"
    CREDENTIAL_ACCESS = "credential_access"
    LOGIN             = "login"
    REGISTER          = "register"


class AuditLog(Base):
    __tablename__ = "audit_logs"

    user_id:     Mapped[uuid.UUID]   = mapped_column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    action:      Mapped[AuditAction] = mapped_column(Enum(AuditAction), nullable=False)
    resource_id: Mapped[str | None]  = mapped_column(String(255), nullable=True)
    ip_address:  Mapped[str | None]  = mapped_column(String(45), nullable=True)
    user_agent:  Mapped[str | None]  = mapped_column(String(512), nullable=True)
    meta:        Mapped[dict | None] = mapped_column(JSONB, nullable=True)

    user: Mapped["User"] = relationship(back_populates="audit_logs")
