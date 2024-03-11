from homework.raman_kuntsevich.homework_15.student_manager import StudentManager

db_students = StudentManager(
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    user='st-onl',
    password='AVNS_tegPDkI5BlB2lW5eASC',
    database='st-onl'
)

student_id = db_students.add_students(('Raman', 'Kuntsevich'))[0]
books_ids = db_students.add_books(
    ('Lord Of The Rings', student_id),
    ('Harry Potter', student_id),
    ('Game of Thrones', student_id)
)
group_id = db_students.add_groups(('Hogwarts 1st grade', 'sept 2024', 'may 2024'))[0]
updated_student = db_students.update_student_group(student_id, group_id)
subject_ids = db_students.add_subjects(
    'Защита от тменых исскуств',
    'Зельеварение',
    'Полеты на метле'
)
lesson_ids = db_students.add_lessons(
    ('Экспелиармус', subject_ids[0]),
    ('Экспекто Патронум', subject_ids[0]),
    ('Феликс Филицис', subject_ids[1]),
    ('Оборотное зелье', subject_ids[1]),
    ('Первый полет', subject_ids[2]),
    ('Правила квиддича', subject_ids[2])
)

mark_ids = db_students.add_marks(
    ('Normal', lesson_ids[0], student_id),
    ('Not bad', lesson_ids[1], student_id),
    ('Great', lesson_ids[2], student_id),
    ('Bad', lesson_ids[3], student_id),
    ('Excellent!', lesson_ids[4], student_id),
    ('Perfect', lesson_ids[5], student_id)
)

student_marks = db_students.get_student_marks(student_id)
student_books = db_students.get_student_books(student_id)
student_data = db_students.get_all_student_data(student_id)


def print_select_data(data, keys):
    if data:
        print("\n".join([", ".join([f"{key}: {entry[key]}" for key in keys]) for entry in data]))
    else:
        print(f"No {keys[0].lower()} found for the specified student.")


print_select_data(student_marks, ['Name', 'SecondName', 'Lesson', 'Mark'])
print_select_data(student_books, ['title'])
print_select_data(student_data, ['Name', 'SecondName', 'Group', 'Lesson', 'Mark', 'Book'])
