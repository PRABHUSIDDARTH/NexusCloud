import enum
from sqlalchemy import String, Boolean, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.base import Base


class Plan(str, enum.Enum):
    FREE    = "free"
    STARTER = "starter"
    PRO     = "pro"
    TEAM    = "team"


class User(Base):
    __tablename__ = "users"

    email:         Mapped[str]  = mapped_column(String(255), unique=True, nullable=False, index=True)
    password_hash: Mapped[str]  = mapped_column(String(255), nullable=False)
    is_active:     Mapped[bool] = mapped_column(Boolean, default=True)
    plan:          Mapped[Plan] = mapped_column(Enum(Plan), default=Plan.FREE)

    connections:  Mapped[list["CloudConnection"]] = relationship(back_populates="user", cascade="all, delete-orphan")
    file_records: Mapped[list["FileRecord"]]       = relationship(back_populates="user", cascade="all, delete-orphan")
    audit_logs:   Mapped[list["AuditLog"]]         = relationship(back_populates="user", cascade="all, delete-orphan")
