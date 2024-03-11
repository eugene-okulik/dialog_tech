from homework.raman_kuntsevich.homework_15.database_manager import DatabaseManager


class StudentManager(DatabaseManager):

    def __init__(self, host, port, user, password, database):
        super().__init__(host, port, user, password, database)

    def add_students(self, *args):
        """
        Add students to the database.

        :param args: Each student is represented by a tuple ('name', 'surname').
        :return: List of identifiers for the added students.
        """

        query = '''
        insert into students (name, second_name)
        values (%s, %s)
        '''
        params = [*args]
        return self.execute_insert_query(query, params)

    def add_books(self, *args):
        """
        Add books to the database.

        :param args: Each book is represented by a tuple ('title', 'taken_by_student_id').
        :return: List of identifiers for the added books.
        """

        query = '''
        insert into books (title, taken_by_student_id)
        values (%s, %s)
        '''
        params = [*args]
        return self.execute_insert_query(query, params)

    def add_groups(self, *args):
        """
        Add groups to the database.

        :param args: Each group is represented by a tuple ('title', 'start_date', 'end_date').
        :return: List of identifiers for the added groups.
        """

        query = '''
        INSERT into `groups` (title, start_date, end_date)
        values (%s, %s, %s)
        '''
        params = [*args]
        return self.execute_insert_query(query, params)

    def update_student_group(self, student_id, group_id):
        """
        Update student group.

        :param student_id: Updated student id
        :param group_id: Added group id
        :return: None
        """

        query = '''
        update students s
        set s.group_id = %s
        where s.id = %s
        '''
        params = (group_id, student_id)
        return self.execute_update_query(query, params)

    def add_subjects(self, *args):
        """
        Add subjects to the database.

        :param args: Each subject is represented by a tuple ('title').
        :return: List of identifiers for the added subjects.
        """

        query = '''
        insert into subjets (title)
        values (%s)
        '''
        params = [(title,) for title in args]
        return self.execute_insert_query(query, params)

    def add_lessons(self, *args):
        """
        Add lessons to the database.

        :param args: Each lesson is represented by a tuple ('title', 'subject_id').
        :return: List of identifiers for the added lessons.
        """

        query = '''
        insert into lessons (title, subject_id)
        values (%s, %s)
        '''
        params = [*args]
        return self.execute_insert_query(query, params)

    def add_marks(self, *args):
        """
        Add marks to the database.

        :param args: Each mark is represented by a tuple ('value', 'lesson_id', 'student_id').
        :return: List of identifiers for the added marks.
        """

        query = '''
        insert into marks (value, lesson_id, student_id)
        values (%s, %s, %s)
        '''
        params = [*args]
        return self.execute_insert_query(query, params)

    def get_student_marks(self, student_id):
        """
        Get student marks from database

        :param student_id: student id in database.
        :return: List of student marks by lessons.
        """

        query = '''
        select
        s.name as Name,
        s.second_name as SecondName,
        l.title as Lesson,
        m.value as Mark
        from marks m, students s, lessons l
        where s.id = %s
        and s.id = m.student_id
        and m.lesson_id = l.id
        '''
        return self.execute_select_query(query, (student_id,))

    def get_student_books(self, student_id):
        """
        Get student books from database

        :param student_id: student id in database.
        :return: List of student books.
        """

        query = '''
        select b.title
        from books b, students s
        where s.id = %s
        and s.id = b.taken_by_student_id
        '''
        return self.execute_select_query(query, (student_id,))

    def get_all_student_data(self, student_id):
        """
        Get student all data from database

        :param student_id: student id in database.
        :return: All student data.
        """

        query = '''
        SELECT
        s.name as Name,
        s.second_name as SecondName,
        g.title as `Group`,
        b.title as Book,
        s2.title as Subject,
        l.title as Lesson,
        m.value as Mark
        from students s
        join `groups` g
        on s.group_id  = g.id
        join books b
        on b.taken_by_student_id  = s.id
        join marks m
        on m.student_id = s.id
        join lessons l
        on l.id = m.lesson_id
        join subjets s2
        on s2.id = l.subject_id
        where s.id = %s
        '''
        return self.execute_select_query(query, (student_id,))
