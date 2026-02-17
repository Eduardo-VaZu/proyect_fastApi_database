from app.models.message_model import SaveMessage
from app.entities.message_entities import MessageEntity

from sqlalchemy.orm import Session
from typing import List, Optional
from abc import ABC, abstractmethod


class MessageService(ABC):
    @abstractmethod
    def find_all_messages(self, db: Session) -> List[MessageEntity]:
        pass

    @abstractmethod
    def find_message_by_id(
        self, db: Session, message_id: int
    ) -> Optional[MessageEntity]:
        pass

    @abstractmethod
    def create_message(self, db: Session, message: SaveMessage) -> MessageEntity:
        pass

    @abstractmethod
    def update_message(
        self, db: Session, message_id: int, message: SaveMessage
    ) -> Optional[MessageEntity]:
        pass

    @abstractmethod
    def delete_message(self, db: Session, message_id: int) -> bool:
        pass
