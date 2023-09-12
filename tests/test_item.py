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
