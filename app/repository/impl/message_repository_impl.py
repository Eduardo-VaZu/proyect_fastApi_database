from app.repository.message_repository import MessageRepository
from app.entities.message_entities import MessageEntity
from app.models.message_model import CreateMessage

from sqlalchemy.orm import Session
from typing import List, Optional


class MessageRepositoryImpl(MessageRepository):
    def get_all_messages(self, db: Session) -> List[MessageEntity]:
        query = db.query(MessageEntity)
        return query.all()

    def get_message_by_id(self, db: Session, id: int) -> Optional[MessageEntity]:
        return db.query(MessageEntity).filter(MessageEntity.id == id).first()

    def create_message(self, db: Session, message: MessageEntity) -> MessageEntity:
        db.add(message)
        db.commit()
        db.refresh(message)
        return message

    def update_message(
        self, db: Session, message_id: int, message_data: CreateMessage
    ) -> Optional[MessageEntity]:
        db_item = self.get_message_by_id(db, message_id)
        if db_item:
            db_item.message = message_data.message
            db_item.author_email = message_data.author_email
            db_item.priority = message_data.priority
            db.commit()
            db.refresh(db_item)
        return db_item

    def delete_message(self, db: Session, id: int) -> bool:
        db_item = self.get_message_by_id(db, id)
        if db_item:
            db.delete(db_item)
            db.commit()
            return True
        return False
