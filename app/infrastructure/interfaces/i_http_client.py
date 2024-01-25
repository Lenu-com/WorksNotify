from abc import ABC, abstractmethod


class IHttpClient(ABC):
    @abstractmethod
    def post(self, url, headers, data):
        raise NotImplementedError()
