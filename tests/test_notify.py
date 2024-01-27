from unittest.mock import patch
from app.infrastructure.notify import Notify
from app.infrastructure.http_client import HttpClient
from app.domain.services.message_service import MessageService
from app.domain.objects.message import Message


@patch('requests.post')
def test_send(mock_post) -> None:
    test_message = "Test message"
    test_token = "test_token"
    
    http_client = HttpClient()
    message_service = MessageService()
    notify = Notify(http_client, message_service, line_notify_token=test_token)
    notify.send_message(Message(test_message))

    mock_post.assert_called_once_with(
        url='https://notify-api.line.me/api/notify',
        headers={'Authorization': f'Bearer ' + test_token},
        data=message_service.create_message_data(Message(test_message))
    )
