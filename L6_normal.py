# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать 
# в неограниченном кол-ве классов свой определенный предмет. 
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика 
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе


class Teacher:
    def __init__(self, surname, course):
        self.surname = surname
        self.course = course


class Classroom:
    def __init__(self, number, teachers):
        self.number = number
        self.teachers = teachers


class Student:
    def __init__(self, name, surname, mom, dad, class_room):
        self.name = name
        self.surname = surname
        self.mom = mom
        self.dad = dad
        self.class_room = class_room


teachers = {
    'Шишкин': Teacher('Шишкин', 'Математика'),
    'Пупкин': Teacher('Пупкин', 'География'),
    'Серов': Teacher('Серов', 'Физика'),
    'Скриптов': Teacher('Скриптов', 'Информатика'),
    'Мухова': Teacher('Мухова', 'Литература'),
    'Филатов': Teacher('Филатов', 'ОБЖ')
}

classes = {
    '10А': Classroom('10А', ['Серов', 'Филатов', 'Мухова']),
    '3Б': Classroom('3Б', ['Пупкин', 'Шишкин']),
    '7Б': Classroom('7Б', ['Серов']),
    '10В': Classroom('10В', ['Скриптов', 'Филатов'])
}

students = {
    'Егор Летов': Student('Егор', 'Летов', 'Летова И.П.', 'Летов Е.М.', '10А'),
    'Рома Жёлудь': Student('Рома', 'Жёлудь', 'Жёлудь О.В.', 'Жёлудь Е.Б.', '3Б'),
    'Александр Васильев': Student('Александр', 'Васильев', 'Васильева Н.К.', 'Васильев Е.В.', '7Б'),
    'Джон Леннон': Student('Джон', 'Леннон', 'Леннон Й.О.', 'Леннон В.В.', '10В')
}

print('\nСписок всех классов:')
for each in classes:
    print(each)

class_room = '3Б'
print('\nСпиок учеников в классе {}:'.format(class_room))
for each in students.values():
    if each.class_room == class_room:
        print(each.name, each.surname)

search_courses = 'Джон Леннон'
print('\nУроки, которые посещает {}:'.format(search_courses))
if search_courses in students:
    class_room = students[search_courses].class_room
    if class_room in classes:
        for surname in classes[class_room].teachers:
            if surname in teachers:
                print(teachers[surname].course)

search_parents = 'Егор Летов'
print('\nРодители ученика - {}:'.format(search_parents))
if search_parents in students:
    print('Мать: ', students[search_parents].mom)
    print('Отец: ', students[search_parents].dad)

class_room = '10В'
print('\nПреподаватели в {}:'.format(class_room))
if class_room in classes:
    print(classes[class_room].teachers)