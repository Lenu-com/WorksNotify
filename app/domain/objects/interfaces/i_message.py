from abc import ABC, abstractmethod
from typing import Dict

class IMessage(ABC):
    @abstractmethod
    def to_request(self) -> Dict[str, str]:
        raise NotImplementedError()
