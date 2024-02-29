words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}

for key, value in words.items():
    for _ in range(value):
        print(key, end='')
    print()
