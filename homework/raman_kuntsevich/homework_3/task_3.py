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
mean_result = (x + y) / 2
geometric_mean_result = (x * y) ** 0.5

print_result('Mean x and y result:', mean_result)
print_result('Geometric mean x and y result:', geometric_mean_result)
