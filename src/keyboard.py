from src.item import Item


class KeyboardLanguage:
    lang = "EN"

    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
        self.__language = self.lang

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        if self.__language == 'EN':
            self.__language = 'RU'
        else:
            self.__language = 'EN'


class Keyboard(KeyboardLanguage, Item):
    pass


