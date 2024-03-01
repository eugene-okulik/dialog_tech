result_1 = 'результат операции: 42'
result_2 = 'результат операции: 54'
result_3 = 'результат работы программы: 209'
result_4 = 'результат: 2'


def format_result(result):
    result_text = result.split(': ')
    result_number = int(result_text[1])
    return result_number + 10


print(format_result(result_1))
print(format_result(result_2))
print(format_result(result_3))
print(format_result(result_4))
