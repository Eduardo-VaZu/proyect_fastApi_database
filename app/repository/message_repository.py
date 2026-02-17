from app.entities.message_entities import MessageEntity
from app.models.message_model import CreateMessage

from sqlalchemy.orm import Session
from abc import ABC, abstractmethod
from typing import List, Optional


class MessageRepository(ABC):
    @abstractmethod
    def get_all_messages(self, db: Session) -> List[MessageEntity]:
        pass

    @abstractmethod
    def get_message_by_id(
        self, db: Session, message_id: int
    ) -> Optional[MessageEntity]:
        pass

    @abstractmethod
    def create_message(self, db: Session, message: MessageEntity) -> MessageEntity:
        pass

    @abstractmethod
    def update_message(
        self, db: Session, message_id: int, message: CreateMessage
    ) -> Optional[MessageEntity]:
        pass

    @abstractmethod
    def delete_message(self, db: Session, message_id: int) -> bool:
        pass
