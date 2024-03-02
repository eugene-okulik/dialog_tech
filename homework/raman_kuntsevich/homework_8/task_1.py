import random


def get_salary():
    while True:
        try:
            return int(input("Enter your salary in integer:"))
        except ValueError:
            print("Input is not a valid integer value. Please enter an integer.")


# Сделал бонус не совсем случайным, а 10% - 50% от зарплаты
def get_result_salary(salary_value):
    bonus = random.choice([True, False])
    random_bonus_value = salary_value * random.uniform(0.1, 0.5) if bonus else 0
    result_salary = salary_value + random_bonus_value
    print(f'{salary_value}, {bonus} - ${result_salary}')


salary = get_salary()
get_result_salary(salary)
