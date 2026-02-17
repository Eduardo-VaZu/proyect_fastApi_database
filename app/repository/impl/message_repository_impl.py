from app.repository.message_repository import MessageRepository
from app.entities.message_entities import MessageEntity

from sqlalchemy.orm import Session
from typing import List, Optional


class MessageRepositoryImpl(MessageRepository):

    def find_all(self, db: Session) -> List[MessageEntity]:
        query = db.query(MessageEntity)
        return query.all()

    def find_by_id(self, db: Session, id: int) -> Optional[MessageEntity]:
        return db.query(MessageEntity).filter(MessageEntity.id == id).first()

    def save(self, db: Session, message: MessageEntity) -> MessageEntity:
        db.add(message)
        db.commit()
        db.refresh(message)
        return message

    def delete(self, db: Session, id: int) -> bool:
        db_item = self.find_by_id(db, id)
        if db_item:
            db.delete(db_item)
            db.commit()
            return True
        return False
