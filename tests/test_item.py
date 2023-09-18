"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


@pytest.fixture()
def item():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)
    return item1, item2


def test_calculate_total_price(item):
    a, b = item
    assert a.calculate_total_price() == 200000
    assert b.calculate_total_price() == 100000


def test_apply_discount(item):
    a, b = item
    Item.pay_rate = 0.5
    a.apply_discount()
    b.apply_discount()
    assert a.price == 5000
    assert b.price == 10000


def test_string_to_number():
    assert Item.string_to_number('2') == 2


def test_instantiate_from_csv():
    Item.instantiate_from_csv('../src/items.csv')
    assert len(Item.all) == 5


def test_repr(item):
    a, b = item
    assert repr(a) == "Item('Смартфон', 10000, 20)"
    assert repr(b) == "Item('Ноутбук', 20000, 5)"


def test_str(item):
    a, b = item
    assert str(a) == 'Смартфон'
    assert str(b) == 'Ноутбук'
