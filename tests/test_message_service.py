from app.domain.objects.message import Message
from app.domain.services.message_service import MessageService


def test_message_data_creation() -> None:
    message = Message("Test message")
    message_data = MessageService.create_message_data(message)
    assert message_data == {'message': message.text}

