from app.config.db_config import Base

from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column


class MessageEntity(Base):
    __tablename__ = "messages"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)

    message: Mapped[str] = mapped_column(String(255), nullable=False, index=True)

    author_email: Mapped[str] = mapped_column(String(255), nullable=True, index=True)

    priority: Mapped[int] = mapped_column(
        Integer, nullable=False, default=1, index=True
    )
