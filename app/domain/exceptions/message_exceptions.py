class MessageTextNoneError(Exception):
    def __init__(self):
        super().__init__('message_text is None.')


class MessageTextEmptyError(Exception):
    def __init__(self):
        super().__init__('message_text is empty.')
