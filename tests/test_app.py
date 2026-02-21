import pytest
from src.app import add, greet


def test_greet_returns_correct_message():
    result = greet("Alice")
    assert result == "Hello, Alice! Welcome to the CI/CD Pipeline."


def test_greet_raises_on_empty_name():
    with pytest.raises(ValueError):
        greet("")


def test_add_two_numbers():
    assert add(2, 3) == 5


def test_add_negative_numbers():
    assert add(-1, -1) == -2
