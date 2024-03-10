class Bouquet:
    def __init__(self):
        self.flowers = []

    def add_flower(self, flower):
        self.flowers.append(flower)

    def add_flowers(self, flower, count):
        self.flowers.extend([flower] * count)

    def calculate_cost(self):
        total_cost = sum(flower.price for flower in self.flowers)
        return f'Bouquet price: {total_cost}$'

    def bouquet_life_time(self):
        sum_life_time = sum(flower.life_time for flower in self.flowers)
        average_life_time = round(sum_life_time / len(self.flowers))
        return f'Average bouquet life time is {average_life_time} days.'

    def sort_by(self, key):
        self.flowers.sort(key=lambda flower: getattr(flower, key))

    def find_flowers(self, key, value):
        return [flower for flower in self.flowers if getattr(flower, key) == value]

    def __str__(self):
        return '\n'.join(str(flower) for flower in self.flowers)

    def __repr__(self):
        return '\n'.join(str(flower) for flower in self.flowers)
