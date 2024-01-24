import os
import requests
from typing import Final
from app.domain.objects.interfaces.i_message import IMessage


class Notify:
    _line_notify_api: Final[str] = 'https://notify-api.line.me/api/notify'
    
    def __init__(self, line_notify_token=os.getenv('LINE_NOTIFY_TOKEN')) -> None:
        if line_notify_token is None:
            raise Exception('LINE_NOTIFY_TOKEN is not set.')
        self._line_notify_token = line_notify_token
        
    
    def send_message(self, message: IMessage) -> None:
        headers = {'Authorization': f'Bearer {self._line_notify_token}'}
        data = message.to_dict()
        requests.post(self._line_notify_api, headers = headers, data = data)


