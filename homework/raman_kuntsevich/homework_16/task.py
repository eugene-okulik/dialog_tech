import csv
import os
import dotenv
from homework.raman_kuntsevich.homework_15.database_manager import DatabaseManager

file_path = os.path.join(
    os.path.dirname(
        os.path.dirname(
            os.path.dirname(__file__))),
    'eugene_okulik', 'Lesson_16', 'hw_data')
file_name = 'data.csv'
dotenv.load_dotenv()

query = '''
SELECT
s.name, 
s.second_name, 
g.title as group_title,
b.title as book_title,
s2.title as subject_title,
l.title  as lesson_title,
m.value  as mark_value
FROM 
students s
JOIN `groups` g ON s.group_id = g.id
JOIN books b ON b.taken_by_student_id = s.id
JOIN marks m ON m.student_id = s.id
JOIN lessons l ON m.lesson_id = l.id
JOIN subjets s2 ON l.subject_id = s2.id
WHERE s.name = %s
and s.second_name = %s
and g.title = %s
and b.title = %s
and s2.title = %s
and l.title = %s
and m.value = %s
'''

db = DatabaseManager(
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASSW'),
    database=os.getenv('DB_NAME')
)

with open(os.path.join(file_path, file_name), newline='') as csv_file:
    file_data = csv.DictReader(csv_file)
    for raw in file_data:
        if not db.execute_select_query(query, tuple(raw.values())):
            print(raw)

db.close_connection()
