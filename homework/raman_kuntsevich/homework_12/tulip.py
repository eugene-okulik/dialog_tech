from flower import Flower


class Tulip(Flower):
    def __init__(self, color):
        super().__init__("Tulip", color, 4, 7, 5)
