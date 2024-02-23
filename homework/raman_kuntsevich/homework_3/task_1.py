def input_numeric_value(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Input is not a valid numeric value. Please enter a number.")


def print_result(prompt, math_result):
    print(f'{prompt} {math_result}')


a = input_numeric_value('Enter the numeric value of a:')
b = input_numeric_value('Enter the numeric value of b:')
sum_result = a + b
diff_result = a - b
prod_result = a * b

print_result('Sum of numbers:', sum_result)
print_result('Difference of numbers:', diff_result)
print_result('Product of numbers:', prod_result)
