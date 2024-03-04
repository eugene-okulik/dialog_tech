def repeat_func(func):
    def wrapper(*args, **kwargs):
        count = kwargs.pop('count', 1)
        # for _ in range(count):
        #     func(*args, **kwargs)
        list(map(lambda _: func(*args, **kwargs), range(count)))

    return wrapper


@repeat_func
def print_func(text):
    print(text)


print_func("Hello!", count=3)
