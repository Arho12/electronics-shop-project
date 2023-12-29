import csv
import os.path


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f'{self.name}'

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        new_name = ""
        if len(name) > 10:
            new_name += name[0:9]
        elif len(name) <= 10:
            new_name += name
        self.__name = new_name

    @classmethod
    def instantiate_from_csv(cls, file_path='../src/items.csv'):
        file_path = os.path.join(os.path.dirname(__file__), "..", file_path)
        try:
            cls.all.clear()
            with open(file_path, 'r', encoding="windows-1251") as file:
                reader = csv.DictReader(file)
                items = list(reader)
                for item in items:
                    Item(name=item["name"], price=float(item["price"]), quantity=int(item["quantity"]))
        except KeyError:
            raise InstantiateCSVError("Файл item.csv поврежден")
        except FileNotFoundError:
            return f"Отсутствует файл item.csv"

    @staticmethod
    def string_to_number(namber):
        return int(float(namber))

    def __add__(self, other):
        if issubclass(other.__class__, self.__class__):
            return self.quantity + other.quantity
        return None


class InstantiateCSVError(Exception):
    def __init__(self):
        pass

    def __str__(self):
        return 'Файл item.csv поврежден'
