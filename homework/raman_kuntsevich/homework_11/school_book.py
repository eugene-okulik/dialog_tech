from homework.raman_kuntsevich.homework_11.book import Book


class SchoolBook(Book):

    def __init__(self, title: str, author: str, page_count: int, isbn: str, subject: str, grade: int, tasks: bool):
        super().__init__(title, author, page_count, isbn)
        self.subject = subject
        self.grade = grade
        self.tasks = tasks

    def print_book_info(self):
        book_info = (f'Название: {self.title}, '
                     f'Автор: {self.author}, '
                     f'страниц: {self.page_count}, '
                     f'предмет: {self.subject}, '
                     f'класс: {self.grade}')
        book_info = book_info + ', зарезервирована' if self.reserved else book_info
        print(book_info)
