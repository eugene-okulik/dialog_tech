from flower import Flower


class Rose(Flower):
    def __init__(self, color):
        super().__init__("Rose", color, 3, 5, 7)
