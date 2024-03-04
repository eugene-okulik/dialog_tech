def choose_calc_operation(func):
    def wrapper(first, second):
        if first < 0 or second < 0:
            return func(first, second, '*')
        elif first > second:
            return func(first, second, '-')
        elif first < second:
            return func(first, second, '/')
        elif first == second:
            return func(first, second, '+')

    return wrapper


# return first / second if second != 0 else None - Не добавил это условие т.к. в текущей реализаци такого не может быть
@choose_calc_operation
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '/':
        return first / second
    elif operation == '*':
        return first * second


def get_numbers_from_user():
    try:
        first = float(input("Enter the first number: "))
        second = float(input("Enter the second number: "))
        return first, second
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        return get_numbers_from_user()


first_num, second_num = get_numbers_from_user()
result = calc(first_num, second_num)
print(f'Result: {result}')
