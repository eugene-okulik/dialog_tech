class Flower:
    def __init__(self, name, color, price, life_time, stem_length):
        self.__name = name
        self.color = color
        self.__price = price
        self.__life_time = life_time
        self.__stem_length = stem_length

    @property
    def name(self):
        return self.__name

    @property
    def stem_length(self):
        return self.__stem_length

    @property
    def life_time(self):
        return self.__life_time

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        self.__price = value

    def __str__(self):
        return (f'{self.color} '
                f'{self.__name}, '
                f'stem length: {self.__stem_length}, '
                f'life time: {self.__life_time}, '
                f'price: {self.__price}$')

    def __repr__(self):
        return (f'{self.color} '
                f'{self.__name}, '
                f'stem length: {self.__stem_length}, '
                f'life time: {self.__life_time}, '
                f'price: {self.__price}$')
