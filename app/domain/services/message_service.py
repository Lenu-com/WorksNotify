from typing import Dict
from app.domain.services.interfaces.i_message_service import IMessageService
from app.domain.objects.message import Message


class MessageService(IMessageService):
    @classmethod
    def create_message_data(cls, message: Message) -> Dict[str, str]:
        return {'message': message.text}
