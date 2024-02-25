def input_numeric_value(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            else:
                print("Input must be a positive number. Please enter a positive value.")
        except ValueError:
            print("Input is not a valid numeric value. Please enter a number.")


def print_result(prompt, result):
    print(f'{prompt} {result}')


leg_a = input_numeric_value('Enter the numeric value of leg a:')
leg_b = input_numeric_value('Enter the numeric value of leg b:')
triangle_hypotenuse = (leg_a ** 2 + leg_b ** 2) ** 0.5
triangle_area = 0.5 * leg_a * leg_b

print_result('Triangle hypotenuse:', triangle_hypotenuse)
print_result('Triangle area:', triangle_area)
