import pytest
from app.domain.objects.message import Message


def test_message_creation() -> None:
    text = "Test message"
    message = Message(text)
    assert message.text == text


def test_message_creation_empty_text() -> None:
    with pytest.raises(ValueError):
        Message("")


def test_message_creation_none_text() -> None:
    with pytest.raises(ValueError):
        Message(None)
