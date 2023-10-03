import csv
import os

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
        self.all.append(self)


    def __str__(self):
        return f'{self.name}'


    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"


    def __add__(self, other):
        if issubclass(other.__class__, self.__class__):
            return self.quantity + other.quantity
        else:
            raise ValueError()

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        if len(name) > 10:
            print('Длина наименования товара превышает 10 символов')
            name = name[:10]
            self.__name = name
        else:
            self.__name = name

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

    @classmethod
    def instantiate_from_csv(cls, path):
        cls.all = []

        thing = None
        try:
            with open(path, newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    thing = Item(*row.values())
        except FileNotFoundError:
            print("FileNotFoundError: Отсутствует файл item.csv")
            raise FileNotFoundError('Отсутствует файл item.csv')
        except TypeError:
            print("InstantiateCSVError: Файл item.csv поврежден")
            raise InstantiateCSVError
        return thing

    @staticmethod
    def string_to_number(string):
        return round(float(string))


class InstantiateCSVError(Exception):
    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else 'Файл item.csv поврежден'

    def __str__(self):
        return self.message
