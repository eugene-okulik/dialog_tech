class Book:
    page_material = 'Paper'
    presence_of_text = True

    def __init__(self, title: str, author: str, page_count: int, isbn: str, reserved: bool = False):
        self.title = title
        self.author = author
        self.page_count = page_count
        self.isbn = isbn
        self.reserved = reserved

    def print_book_info(self):
        book_info = (f'Название: {self.title}, '
                     f'Автор: {self.author}, '
                     f'страниц: {self.page_count}, '
                     f'материал: {self.page_material}')
        book_info = book_info + ', зарезервирована' if self.reserved else book_info
        print(book_info)
