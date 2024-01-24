from typing import Dict
from app.domain.objects.interfaces.i_message import IMessage


class Message(IMessage):
    def __init__(self, message_text: str) -> None:
        if message_text is None:
            raise Exception('message_text is None.')
        if len(message_text) < 1:
            raise Exception('message_text is empty.')
        self._message_text = message_text
        
    
    def __hash__(self) -> int:
        return hash(self._message_text)
    
    
    def __eq__(self, obj: object) -> bool:
        if not isinstance(obj, Message):
            return False
        return self._message_text == obj._message_text
    
    
    def to_message_dict(self) -> Dict[str, str]:
        return {'message': self._message_text}
