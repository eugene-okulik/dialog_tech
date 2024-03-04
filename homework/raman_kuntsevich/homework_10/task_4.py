PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

price_dict = {raw.split()[0]: int(raw.split()[1][:-1]) for raw in PRICE_LIST.split('\n')}
print(price_dict)
