import os
import requests
from typing import Final


class Notify:
    _line_notify_api: Final[str] = 'https://notify-api.line.me/api/notify'
    
    def __init__(self, line_notify_token=os.getenv('LINE_NOTIFY_TOKEN')):
        if line_notify_token is None:
            raise Exception('LINE_NOTIFY_TOKEN is not set.')
        self._line_notify_token = line_notify_token
        
    
    def send_line_notify(self, notifycation_message):
        headers = {'Authorization': f'Bearer {self._line_notify_token}'}
        data = {'message': notifycation_message}
        requests.post(self._line_notify_api, headers = headers, data = data)
