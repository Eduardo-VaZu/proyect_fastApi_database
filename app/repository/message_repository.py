from app.entities.message_entities import MessageEntity

from sqlalchemy.orm import Session
from abc import ABC, abstractmethod
from typing import List, Optional


class MessageRepository(ABC):

    @abstractmethod
    def find_all(self, db: Session) -> List[MessageEntity]:
        pass

    @abstractmethod
    def find_by_id(self, db: Session, message_id: int) -> Optional[MessageEntity]:
        pass

    @abstractmethod
    def save(self, db: Session, message: MessageEntity) -> MessageEntity:
        pass

    @abstractmethod
    def delete(self, db: Session, message_id: int) -> bool:
        pass
