import pytest
from app.domain.objects.message import Message
from app.domain.exceptions.message_exceptions import MessageTextEmptyError, MessageTextNoneError


def test_message_creation() -> None:
    text = "Test message"
    message = Message(text)
    assert message.text == text


def test_message_creation_empty_text() -> None:
    with pytest.raises(MessageTextEmptyError):
        Message("")


def test_message_creation_none_text() -> None:
    with pytest.raises(MessageTextNoneError):
        Message(None)


def test_message_hash() -> None:
    text = "Test message"
    message1 = Message(text)
    message2 = Message(text)
    assert hash(message1) == hash(message2)
    
    
def test_message_hash_different() -> None:
    message1 = Message("Test message 1")
    message2 = Message("Test message 2")
    assert hash(message1) != hash(message2)
    
    
def test_message_equality() -> None:
    text = "Test message"
    message1 = Message(text)
    message2 = Message(text)
    assert message1 == message2


def test_message_inequality() -> None:
    message1 = Message("Test message 1")
    message2 = Message("Test message 2")
    assert message1 != message2
    

def test_message_equality_with_non_message() -> None:
    message = Message("Test message")
    assert message != "Test message"