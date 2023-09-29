import pytest
from src.keyboard import Keyboard


@pytest.fixture()
def keyboard():
    item1 = Keyboard('Dark Project KD87A', 10000, 20)
    item2 = Keyboard('Light Project KD1A', 666, 25)
    return item1, item2


def test_repr(keyboard):
    a, b = keyboard
    a.change_lang()
    assert str(a.language) == "RU"
    assert str(b.language) == "EN"
    assert repr(a) == "Keyboard('Dark Project KD87A', 10000, 20)"
    assert repr(b) == "Keyboard('Light Project KD1A', 666, 25)"
