class Message:
    def __init__(self, message_text: str) -> None:
        if message_text is None:
            raise Exception('message_text is None.')
        if len(message_text) < 1:
            raise Exception('message_text is empty.')
        self._text = message_text
        
    
    def __hash__(self) -> int:
        return hash(self._text)
    
    
    def __eq__(self, obj: object) -> bool:
        if not isinstance(obj, Message):
            return False
        return self._text == obj._text
    
    
    @property
    def text(self) -> str:
        return self._text



