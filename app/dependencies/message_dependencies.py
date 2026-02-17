from app.repository.impl.message_repository_impl import MessageRepositoryImpl
from app.services.impl.message_service_impl import MessageServiceImpl
from app.config.db_config import SessionLocal

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
