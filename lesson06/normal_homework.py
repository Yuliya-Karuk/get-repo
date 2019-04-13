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


class People:
    def __init__(self, full_name, class_rooms):
        self.full_name = full_name
        self.class_rooms = class_rooms


# Сами классы наследуем
class Pupil(People):
    def __init__(self, full_name, parents, class_rooms):
        # Явно вызываем конструктор родительского класса
        People.__init__(self, full_name, class_rooms)
        # Добавляем уникальные атрибуты
        self.parents = parents

    @property
    def info_parents(self):
        return f'Родители ученика {self.full_name} - {self.parents}'


class Teacher(People):
    def __init__(self, full_name, subject, class_rooms):
        People.__init__(self, full_name, class_rooms)
        self.subject = subject

def all_classes(lst):
    # функция выводит список всех классов
    classes = []
    for i in lst:
        classes.append(i.class_rooms)
    classes = list(set(classes))
    return classes

def pupil_in_class(lst):
    # функция выводит список всех учеников определенного класса
    answer = input('Учеников какого класса вы хотите посмотреть - ')
    pup = []
    for i in lst:
        if answer == i.class_rooms:
            pup.append(i.full_name)
    if len(pup) == 0:
        return 'Такого класса нет в школе'
    return pup

def class_of_pupil(lst1, name):
    # всомогательная функция возвращает класс определенного ученика
    for i in lst1:
        if name == i.full_name:
            pupil_class = i.class_rooms
            return pupil_class
    return 'Такого ученика нет в школе'

def pupil_subject(lst1, lst2):
    # функция выводит список предметов определенного ученика
    answer = input('Предметы какого ученика вы хотите посмотреть, \n'
                   'введите в формате Фаммили И.О. - ')
    room = class_of_pupil(lst1, answer)
    sub = []
    if len(room) > 3:
        return room
    else:
        for i in lst2:
            for j in i.class_rooms:
                if room == j:
                    sub.append(i.subject)
    return sub

def pupil_parents(lst1):
    answer = input('Родителей какого ученика вы хотите посмотреть, \n'
                   'введите в формате Фамилия И.О. - ')
    for i in lst1:
        if answer == i.full_name:
            return i.info_parents
    return 'Такого ученика нет в нашей школе'

def class_subject(lst1):
    # функция выводит список предметов определенного класса
    answer = input('Предметы какого класса вы хотите посмотреть - ')
    sub = []
    for i in lst1:
        for j in i.class_rooms:
            if answer == j:
                sub.append(i.full_name)
    if len(sub) == 0:
        return 'Такого класса нет в школе'
    return sub


teachers = [Teacher("Сельханович И. И.", "География", ["4 А", "7 А"]),
            Teacher("Струпинский В. Ч.", "Труд", ["5 Б", "9 А"]),
            Teacher("Рудковская И. И.", "Русский язык", ["8 А", "7 А"]),
            Teacher("Карук Ж. И.", "Химия", ["5 А", "7 А"]),
            Teacher("Бекиш И. И.", "Математика", ["5 Б", "9 А"]),
            Teacher("Иванова М. И.", "Физика", ["8 А", "7 А"])]


pupils = [Pupil("Гейдель О. С.", ["Гейдель С. И.", "Гейдель Н. К."], "4 А"),
          Pupil("Кралько О. Т.", ["Кралько С. Н.", "Кралько Л. К."], "5 А"),
          Pupil("Богдан Д. И.", ["Богдан А. В.", "Богдан В. С."], "7 А"),
          Pupil("Черняк Д. И.", ["Черняк Н В.", "Черняк О. С."], "5 В"),
          Pupil("Руденко Д. И.", ["Руденко Н В.", "Руденко О. С."], "5 В"),
          Pupil("Подмаско В. К.", ["Подмаско В. Ю.", "Подмаско Е. С."], "9 А")]


while True:
    try:
        item = int(input(""" Чтобы получить информацию введите номер запроса:
                  1. Получить полный список всех классов школы
                  2. Получить список всех учеников в указанном классе
                  3. Получить список всех предметов указанного ученика
                  4. Узнать ФИО родителей указанного ученика
                  5. Получить список всех Учителей, преподающих в указанном классе
                  Для выхода введите 0\n"""))
    except ValueError:
        print('Вы введи неправильное число')
    else:
        if item == 1:
            print(all_classes(pupils))
        elif item == 2:
            print(pupil_in_class(pupils))
        elif item == 3:
            print(pupil_subject(pupils, teachers))
        elif item == 4:
            print(pupil_parents(pupils))
        elif item == 5:
            print(class_subject(teachers))
        elif item == 0:
            break
        else:
            print('Вы ввели неправильную команду')

