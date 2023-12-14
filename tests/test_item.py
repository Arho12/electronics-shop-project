"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item


def test_calculate_total_price():
    assert Item("Смартфон", 10000, 20).calculate_total_price() == 200000


def test_apply_discount():
    item = Item("Смартфон", 10000, 20)
    item.pay_rate = 0.5
    item.apply_discount()
    assert item.price == 5000


def test_instantiate_from_csv():
    Item.instantiate_from_csv('src/items.csv')
    assert len(Item.all) == 5


def test_string_to_number():
    assert Item.string_to_number('10') == 10
    assert Item.string_to_number('7.0') == 7
    assert Item.string_to_number('5.5') == 5

def test_repr():
    item1 = Item("Смартфон", 10001, 240)
    assert repr(item1) == "Item('Смартфон', 10001, 240)"

def test_str():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 10000, 20)
    assert str(item1) == 'Смартфон'
    assert str(item2) == 'Ноутбук'