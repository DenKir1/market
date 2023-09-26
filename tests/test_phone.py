import pytest
from src.phone import Phone


@pytest.fixture()
def phones():
    item1 = Phone("Смартфон", 10000, 20, 2)
    item2 = Phone("Франкенфон", 666, 25, 10)
    return item1, item2


def test_repr(phones):
    a, b = phones
    assert repr(a) == "Phone('Смартфон', 10000, 20, 2)"
    assert repr(b) == "Phone('Франкенфон', 666, 25, 10)"


def test_str(phones):
    a, b = phones
    assert str(a) == 'Смартфон'
    assert str(b) == 'Франкенфон'
