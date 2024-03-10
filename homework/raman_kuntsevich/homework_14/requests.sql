-- Добавляем студента
insert into students (name, second_name)
values ('Raman', 'Kuntsevich')

-- Получаем ID добавленного студента
SELECT s.id
FROM students s
WHERE s.name = 'Raman'
and s.second_name = 'Kuntsevich'
order by s.id DESC
limit 1

-- Добавляем книги
insert into books (title, taken_by_student_id)
values
('Lord Of The Rings', 455),
('Harry Potter', 455),
('Game of Thrones', 455)

-- Добавляем группу
INSERT into `groups` (title, start_date, end_date)
values ('AQA python', 'feb 2024', 'apr 2024')

-- Получаем id добавленной группы
select g.id
from `groups` g
where g.title = 'AQA python'
order by g.id DESC
limit 1

-- Обновляем студента назначая группу
update students s
set s.group_id = 418
where s.id = 455

-- Добавляем предметы
insert into subjets (title)
values
('Защита от тменых исскуств'),
('Зельеварение'),
('Полеты на метле')

-- Получаем id добавленных предметов
select s.id, s.title
from subjets s
where s.title = 'Защита от тменых исскуств'
or s.title = 'Зельеварение'
or s.title = 'Полеты на метле'
order by s.id DESC
limit 3

-- Добавляем занятия
insert into lessons (title, subject_id)
values
('Экспелиармус', 526),
('Экспекто Патронум', 526),
('Феликс Филицис', 527),
('Оборотное зелье', 527),
('Первый полет', 528),
('Правила квиддича', 528)


-- Получаем id добавленных занятий
select l.id, l.title
from lessons l
where l.title = 'Экспелиармус'
or l.title = 'Экспекто Патронум'
or l.title = 'Феликс Филицис'
or l.title = 'Оборотное зелье'
or l.title = 'Первый полет'
or l.title = 'Правила квиддича'
order by l.id DESC
limit 6

-- Добавляем оценки
insert into marks (value, lesson_id, student_id)
values
('Normal', 577, 455),
('Not bad', 578, 455),
('Great', 579, 455),
('Bad', 580, 455),
('Excellent!', 581, 455),
('Perfect', 582, 455)

-- Получаем оценки для нашего студента
select s.name, s.second_name, l.title, m.value
from marks m, students s, lessons l
where s.id = 455
and s.id = m.student_id
and m.lesson_id = l.id

-- Получаем все книги взятые студентом
select b.title
from books b, students s
where s.id = 455
and s.id = b.taken_by_student_id

--Получаем всю информацию из бд по нашему студенту
SELECT *
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
where s.id = 455

