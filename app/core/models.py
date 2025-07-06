from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import JSON

from app.core.database import Base


class HistoryORM(Base):
    __tablename__ = "history"

    id: Mapped[int] = mapped_column(primary_key=True)
    city: Mapped[str]
    data: Mapped[JSON] = mapped_column(type_=JSON)
    created_at: Mapped[datetime] = mapped_column(default=datetime.now)
