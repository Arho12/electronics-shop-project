from src.phone import Phone

def test_repr():
    phone1 = Phone("Смартфон", 10001, 240, 2)
    assert repr(phone1) == "Phone('Смартфон', 10001, 240, 2)"

def test_str():
    phone1 = Phone("Смартфон", 10000, 20, 2)
    assert str(phone1) == 'Смартфон'


