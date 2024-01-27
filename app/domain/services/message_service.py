from typing import Dict
from app.domain.services.interfaces.i_message_service import IMessageService


class MessageService(IMessageService):
    @classmethod
    def create_message_data(cls, message) -> Dict[str, str]:
        return {'message': message.text}
