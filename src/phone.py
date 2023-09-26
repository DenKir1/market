from src.item import Item


class Phone(Item):

    def __init__(self, name, price, quantity, number_of_sim):
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim

    def __str__(self):
        return super().__str__()

    def __repr__(self):
        a = super().__repr__()
        return f"{a[:-1]}, {self.number_of_sim})"

    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, sim):
        if sim > 0 and isinstance(sim, int):
            self.__number_of_sim = sim
        else:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')
