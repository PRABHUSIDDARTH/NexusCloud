# Import all models here so Alembic and SQLAlchemy detect them.
# This file is imported ONLY by alembic/env.py and app/main.py
# — never by the models themselves.

from app.models.user import User                   # noqa: F401
from app.models.connection import CloudConnection  # noqa: F401
from app.models.quota import QuotaSnapshot         # noqa: F401
from app.models.file_record import FileRecord      # noqa: F401
from app.models.audit import AuditLog              # noqa: F401
