from app.repository.message_repository import MessageRepository
from app.services.message_service import MessageService
from app.entities.message_entities import MessageEntity
from app.models.message_model import SaveMessage

from sqlalchemy.orm import Session
from typing import List, Optional


class MessageServiceImpl(MessageService):
    def __init__(self, repository: MessageRepository):
        self.repository = repository

    def find_all_messages(self, db: Session) -> List[MessageEntity]:
        return self.repository.find_all(db)

    def find_message_by_id(
        self, db: Session, message_id: int
    ) -> Optional[MessageEntity]:
        return self.repository.find_by_id(db, message_id)

    def create_message(self, db: Session, message: SaveMessage) -> MessageEntity:
        new_message = MessageEntity(
            message=message.message,
            author_email=message.author_email,
            priority=message.priority,
        )
        return self.repository.save(db, new_message)

    def update_message(
        self, db: Session, message_id: int, message: SaveMessage
    ) -> Optional[MessageEntity]:
        db_item = self.repository.find_by_id(db, message_id)
        if db_item:
            db_item.message = message.message
            db_item.author_email = message.author_email
            db_item.priority = message.priority
            return self.repository.save(db, db_item)
        return None

    def delete_message(self, db: Session, message_id: int) -> bool:
        return self.repository.delete(db, message_id)
