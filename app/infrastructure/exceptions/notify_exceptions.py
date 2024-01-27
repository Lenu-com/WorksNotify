class HttpClientNoneException(Exception):
    def __init__(self):
        super().__init__('http_client is None.')


class MessageServiceNoneException(Exception):
    def __init__(self):
        super().__init__('message_service is None.')
        

class LineNotifyTokenNoneException(Exception):
    def __init__(self):
        super().__init__('LINE_NOTIFY_TOKEN is None.')
