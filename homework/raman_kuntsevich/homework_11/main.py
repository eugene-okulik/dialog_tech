from homework.raman_kuntsevich.homework_11.book import Book
from homework.raman_kuntsevich.homework_11.school_book import SchoolBook

hp_part_1 = Book(
    'Harry Potter and Philosopher\'s Stone',
    'Rowling J. K.',
    331,
    '9780545069670'
)

lotr_part_1 = Book(
    'Lord Of The Rings: The Fellowship of the Ring',
    'Tolkien J. R. R.',
    448,
    '9780007136599'
)

witcher_part_1 = Book(
    'The Witcher: Blood of Elves',
    'Sapkowski Andrzej',
    398,
    '9788842916659'
)

the_magician_wanderings_part_1 = Book(
    'Странствия Мага. Том 1',
    'Ник Перумов',
    352,
    '9785425032027'
)

game_of_thrones_part_1 = Book(
    'A Game of Thrones',
    'Martin George R. R.',
    864,
    '9788496208490'
)

algebra_first_grade = SchoolBook(
    'Алгебра',
    'Василий Пупкин',
    200,
    '24294924924',
    'Математика',
    1,
    True
)

biology_ten_grade = SchoolBook(
    'Флора и Фауна',
    'Генадий Дарвин',
    321,
    '24294235354',
    'Биология',
    10,
    False
)

history_eight_grade = SchoolBook(
    'История Европы',
    'Петр Наполеонович',
    1000,
    '22366224924',
    'История',
    8,
    True
)

lotr_part_1.reserved = True
history_eight_grade.reserved = True

hp_part_1.print_book_info()
lotr_part_1.print_book_info()
witcher_part_1.print_book_info()
the_magician_wanderings_part_1.print_book_info()
game_of_thrones_part_1.print_book_info()

algebra_first_grade.print_book_info()
biology_ten_grade.print_book_info()
history_eight_grade.print_book_info()
