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

    def sort_by_color(self):
        self.flowers.sort(key=lambda flower: flower.color)

    def sort_by_price(self):
        self.flowers.sort(key=lambda flower: flower.price)

    def sor_by_stem_length(self):
        self.flowers.sort(key=lambda flower: flower.stem_length)

    def find_flowers_by_price(self, value):
        return [flower for flower in self.flowers if flower.price == value]

    def find_flowers_by_life_time(self, value):
        return [flower for flower in self.flowers if flower.life_time == value]

    def find_flowers_by_stem_length(self, value):
        return [flower for flower in self.flowers if flower.stem_length == value]

    def find_flowers_by_color(self, value):
        return [flower for flower in self.flowers if flower.color == value]

    def __str__(self):
        return '\n'.join(str(flower) for flower in self.flowers)

    def __repr__(self):
        return '\n'.join(str(flower) for flower in self.flowers)
