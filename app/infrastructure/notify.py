from typing import Final
from app.infrastructure.interfaces.i_http_client import IHttpClient
from app.domain.services.interfaces.i_message_service import IMessageService
from app.domain.objects.message import Message


class Notify:
    _line_notify_api: Final[str] = 'https://notify-api.line.me/api/notify'
    
    def __init__(self, http_client: IHttpClient, message_service: IMessageService, line_notify_token:str) -> None:
        if http_client is None:
            raise Exception('http_client is None.')
        if message_service is None:
            raise Exception('message_service is None.')
        if line_notify_token is None:
            raise Exception('LINE_NOTIFY_TOKEN is not set.')
        self._line_notify_token = line_notify_token
        self._http_client = http_client
        self._message_service = message_service
        
    
    def send_message(self, message: Message) -> None:
        self._http_client.post(
            url = self._line_notify_api,
            headers = {'Authorization': f'Bearer {self._line_notify_token}'},
            data = self._message_service.create_message_data(message)
        )

