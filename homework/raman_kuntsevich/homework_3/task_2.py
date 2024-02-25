def input_numeric_value(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Input is not a valid numeric value. Please enter a number.")


def print_result(prompt, result):
    print(f'{prompt} {result}')


x = input_numeric_value('Enter the numeric value of x:')
y = input_numeric_value('Enter the numeric value of y:')
formula_result = x - y / 1 + x * y

print_result('Formula x - y / 1 + x * y result:', formula_result)
