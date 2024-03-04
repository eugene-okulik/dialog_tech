def type_finished_after_func(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print('finished')
        return result
    return wrapper


@type_finished_after_func
def print_word():
    print("Hello")


@type_finished_after_func
def calc_x(x):
    print(x * 2)


@type_finished_after_func
def calc_sum(x, y):
    print(x + y)


print_word()
calc_x(10)
calc_sum(3, 9)
