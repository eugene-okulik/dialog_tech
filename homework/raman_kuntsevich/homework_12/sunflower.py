from flower import Flower


class Sunflower(Flower):
    def __init__(self, color):
        super().__init__("Sunflower", color, 10, 4, 8)
