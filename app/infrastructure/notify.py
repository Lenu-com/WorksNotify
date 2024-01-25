import os
import requests
from typing import Final
from app.domain.objects.interfaces.i_message import IMessage
from app.infrastructure.interfaces.i_http_client import IHttpClient

class Notify:
    _line_notify_api: Final[str] = 'https://notify-api.line.me/api/notify'
    
    def __init__(self, http_client: IHttpClient, line_notify_token=os.getenv('LINE_NOTIFY_TOKEN')) -> None:
        if line_notify_token is None:
            raise Exception('LINE_NOTIFY_TOKEN is not set.')
        if http_client is None:
            raise Exception('http_client is None.')
        self._line_notify_token = line_notify_token
        self._http_client = http_client
        
    
    def send_message(self, message: IMessage) -> None:
        self._http_client.post(
            url = self._line_notify_api,
            headers = {'Authorization': f'Bearer {self._line_notify_token}'},
            data = message.to_request()
        )

