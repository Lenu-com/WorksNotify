from abc import ABC, abstractmethod
from typing import Dict


class IHttpClient(ABC):
    @abstractmethod
    def post(self, url: str, headers: Dict[str, str], data: Dict[str, str]) -> None:
        raise NotImplementedError()
