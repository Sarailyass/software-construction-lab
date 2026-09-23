
from src.hello import greet


def test_greet_world() -> None:
    assert greet("World") == "Hello, World!"