from rose import Rose
from sunflower import Sunflower
from tulip import Tulip
from bouquet import Bouquet

red_rose = Rose('Red')
sunflower = Sunflower('Yellow')
blue_tulip = Tulip('Blue')
bouquet = Bouquet()

bouquet.add_flower(red_rose)
bouquet.add_flower(sunflower)
bouquet.add_flower(blue_tulip)
bouquet.add_flowers(red_rose, 1)
bouquet.add_flowers(sunflower, 2)
bouquet.add_flowers(blue_tulip, 3)

print(bouquet.calculate_cost())
print(bouquet.bouquet_life_time())
print(bouquet)
print()
bouquet.sort_by_color()
print(bouquet)
print()
bouquet.sort_by_price()
print(bouquet)
print()
bouquet.sor_by_stem_length()
print(bouquet)

print(bouquet.find_flowers_by_price(3))


