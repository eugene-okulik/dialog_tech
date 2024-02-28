result_1 = 'результат операции: 42'
result_2 = 'результат операции: 514'
result_3 = 'результат работы программы: 9'

# Первый вариант
result_1_index = result_1.index(':')
result_2_index = result_2.index(':')
result_3_index = result_3.index(':')

number_1 = int(result_1[result_1_index + 2:])
number_2 = int(result_2[result_2_index + 2:])
number_3 = int(result_3[result_3_index + 2:])

print(number_1 + 10)
print(number_2 + 10)
print(number_3 + 10)


# Второй вариант
def format_result(result):
    result_index = result.index(': ')
    result_text = result[result_index:].lstrip(': ')
    result_number = int(result_text)
    return result_number + 10


print(format_result(result_1))
print(format_result(result_2))
print(format_result(result_3))
