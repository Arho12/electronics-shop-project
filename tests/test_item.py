"""Здесь надо написать тесты с использованием pytest для модуля item."""
import csv

import pytest

from src.item import Item
from src.phone import Phone


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

def test_add():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    item1 = Item("Смартфон", 10000, 20)
    assert item1 + phone1 == 25
    assert phone1 + phone1 == 10
    assert item1 + item1 == 40

def test_instantiate_from_csv():
    with open('items.csv') as file:
        read = csv.DictReader(file)
        assert read is not None
        for x in read:
            assert "name" in x
            assert "price" in x
            assert "quantity" in x

def test_instantiate_from_csv_file_not():
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv('juguig.csv')