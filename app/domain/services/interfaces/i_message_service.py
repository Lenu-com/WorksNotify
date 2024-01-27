from abc import ABC, abstractmethod
from typing import Dict
from app.domain.objects.message import Message


class IMessageService(ABC):
    @abstractmethod
    def create_message_data(self, message: Message) -> Dict[str, str]:
        raise NotImplementedError()
