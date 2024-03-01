import random

random_number = random.randint(1, 10)


def first_example(number):
    while True:
        user_number = input('Guess the number from 1 to 10: ')
        if user_number.isnumeric():
            user_number = int(user_number)
        else:
            print("Input is not a valid int value. Please enter a number.")
            continue
        if user_number == number:
            print('YOU WON!')
            break
        print('Try again!')


# Вариант для практики
def second_example(number):
    while True:
        try:
            user_number = int(input('Guess the number from 1 to 10: '))
            if user_number == number:
                print('YOU WON!')
                break
            print('Try again!')
        except ValueError:
            print("Input is not a valid int value. Please enter a number.")


first_example(random_number)
