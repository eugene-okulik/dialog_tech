text_template = 'Students {0} study these subjects: {1}'
students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']

print(text_template.format(', '.join(students), ', '.join(subjects)))

text_template2 = f'Students {', '.join(students)} study these subjects: {', '.join(subjects)}'

print(text_template2)
