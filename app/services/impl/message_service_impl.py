from app.repository.message_repository import MessageRepository
from app.services.message_service import MessageService
from app.entities.message_entities import MessageEntity
from app.models.message_model import CreateMessage, UpdateMessage

from sqlalchemy.orm import Session
from typing import List, Optional


class MessageServiceImpl(MessageService):
    def __init__(self, repository: MessageRepository):
        self.repository = repository

    def get_all_messages(self, db: Session) -> List[MessageEntity]:
        return self.repository.get_all_messages(db)

    def get_message_by_id(
        self, db: Session, message_id: int
    ) -> Optional[MessageEntity]:
        return self.repository.get_message_by_id(db, message_id)

    def create_message(self, db: Session, message: CreateMessage) -> MessageEntity:
        new_message = MessageEntity(
            message=message.message,
            author_email=message.author_email,
            priority=message.priority,
        )
        # Fixed: save_message -> create_message
        return self.repository.create_message(db, new_message)

    def update_message(
        self, db: Session, message_id: int, message: UpdateMessage
    ) -> Optional[MessageEntity]:
        entity_data = MessageEntity(
            message=message.message,
            author_email=message.author_email,
            priority=message.priority,
        )
        return self.repository.update_message(db, message_id, entity_data)

    def delete_message(self, db: Session, message_id: int) -> bool:
        return self.repository.delete_message(db, message_id)
