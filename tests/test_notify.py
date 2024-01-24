from unittest.mock import patch
from app.infrastructure.notify import Notify


@patch('requests.post')
def test_send_line_notify(mock_post):
    test_message = "Test message"
    test_token = "test_token"
    
    notify = Notify()
    notify.line_notify_token = test_token
    notify.send_line_notify(test_message)

    mock_post.assert_called_once_with(
        'https://notify-api.line.me/api/notify',
        headers={'Authorization': f'Bearer ' + test_token},
        data={'message': test_message}
    )