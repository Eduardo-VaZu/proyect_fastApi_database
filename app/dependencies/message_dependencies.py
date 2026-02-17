from ..repository.impl.messageImpl_repository import MessageRepositoryImpl
from ..services.impl.messageImpl_service import MessageServiceImpl
from ..config.db_config import SessionLocal

from functools import lru_cache


@lru_cache()
def get_message_service():
    repository = MessageRepositoryImpl()
    return MessageServiceImpl(repository)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
