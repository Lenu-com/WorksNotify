import os
import requests
from typing import Final


class Notify:
    line_notify_token: Final[str] = os.getenv('LINE_NOTIFY_TOKEN')
    line_notify_api: Final[str] = 'https://notify-api.line.me/api/notify'
    
    def __init__(self):
        if self.line_notify_token is None:
            raise Exception('LINE_NOTIFY_TOKEN is not set.')
    
    def send_line_notify(self, notifycation_message):
        headers = {'Authorization': f'Bearer {self.line_notify_token}'}
        data = {'message': notifycation_message}
        requests.post(self.line_notify_api, headers = headers, data = data)
