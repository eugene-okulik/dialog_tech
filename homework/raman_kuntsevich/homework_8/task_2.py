import sys

sys.set_int_max_str_digits(30000)


def fibonacci_generator():
    first_value = 0
    second_value = 1
    while True:
        yield first_value
        first_value, second_value = second_value, first_value + second_value


def get_fibonacci_value(value_index):
    fibonacci = fibonacci_generator()
    for _ in range(value_index - 1):
        next(fibonacci)
    print(next(fibonacci))


get_fibonacci_value(5)
get_fibonacci_value(200)
get_fibonacci_value(1000)
get_fibonacci_value(100000)
