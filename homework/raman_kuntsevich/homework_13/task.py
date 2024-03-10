import os
import datetime

file_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'eugene_okulik', 'hw_13')
file_name = 'data.txt'


def read_file(path, file):
    with open(os.path.join(path, file), 'r') as file:
        for line in file.readlines():
            yield line


def parse_date_from_line(line):
    text_date = f'{line[1]}T{line[2]}'
    return datetime.datetime.strptime(text_date, '%Y-%m-%dT%H:%M:%S.%f')


for file_line in read_file(file_path, file_name):
    line_data = file_line.split(' ')
    line_data[0] = line_data[0].replace('.', '')
    if line_data[0] == '1':
        date = parse_date_from_line(line_data)
        print(date + datetime.timedelta(days=7))
        continue
    elif line_data[0] == '2':
        date = parse_date_from_line(line_data)
        print(datetime.datetime.strftime(date, '%A'))
        continue
    elif line_data[0] == '3':
        now = datetime.datetime.now()
        date = parse_date_from_line(line_data)
        print((now - date).days)
        continue
