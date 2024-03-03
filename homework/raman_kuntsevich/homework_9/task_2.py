temperatures = [
    20, 15, 32, 34, 21, 19, 25, 27, 30, 32,
    34, 30, 29, 25, 27, 22, 22, 23, 25, 29,
    29, 31, 33, 31, 30, 32, 30, 28, 24, 23
]
hot_days = list(filter(lambda day: day > 28, temperatures))

print(f'Hot days: {hot_days}')
print(f'Max temperature: {max(hot_days)}')
print(f'Min temperature: {min(hot_days)}')
print(f'Average temperature: {round(sum(hot_days) / len(hot_days))}')
