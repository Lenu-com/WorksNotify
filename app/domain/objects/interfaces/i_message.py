from abc import ABC, abstractmethod
from typing import Dict

class IMessage(ABC):
    @abstractmethod
    def to_message_dict(self) -> Dict[str, str]:
        raise NotImplementedError()