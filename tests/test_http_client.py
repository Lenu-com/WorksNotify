from unittest.mock import patch
from app.infrastructure.http_client import HttpClient


@patch('requests.post')
def test_post(mock_post):
    http_client = HttpClient()
    url = 'http://test.com'
    headers = {'Content-Type': 'application/json'}
    data = {'key': 'value'}

    http_client.post(url, headers, data)
    mock_post.assert_called_once_with(url=url, headers=headers, data=data)
