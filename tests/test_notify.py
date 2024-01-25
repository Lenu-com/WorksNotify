from unittest.mock import patch
from app.infrastructure.notify import Notify
from app.infrastructure.http_client import HttpClient
from app.domain.objects.Message import Message


@patch('requests.post')
def test_send(mock_post) -> None:
    test_message = "Test message"
    test_token = "test_token"
    
    http_client = HttpClient()
    notify = Notify(http_client, line_notify_token=test_token)
    notify.send_message(Message(test_message))

    mock_post.assert_called_once_with(
        url='https://notify-api.line.me/api/notify',
        headers={'Authorization': f'Bearer ' + test_token},
        data={'message': test_message}
    )
