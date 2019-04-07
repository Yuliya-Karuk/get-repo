# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py


import os
import sys
import shutil


def menu():
    print("""
        Меню - выберите нужное действие,
        При выборе пунктов 1, 3, 4 нужно будет ввести название папки
        1. Перейти в папку
        2. Просмотреть содержимое текущей папки
        3. Удалить папку
        4. Создать папку
        """)


def move_dir():
    name = (input('Введите желаемое название папки - '))
    path = os.path.join(os.getcwd(), f'{name}')
    try:
        os.chdir(path)
    except (NameError, FileNotFoundError):
        print("Переход невозможен, папка не найдена")
    else:
        print(f"Переход совершен в папку {name}")


def content_dir():
    files = os.listdir(path=os.getcwd())
    print('Файлы в текущей директории', files)


def make_dir():
    name = input('Введите желаемое название папки - ')
    dir_path = os.path.join(os.getcwd(), name)
    try:
        os.mkdir(dir_path)
    except FileExistsError:
        print('Такая директория уже существует')
    else:
        print('Директория успешно создана')


def del_dir():
    name = input('Введите название папки, которую хотите удалить - ')
    try:
        shutil.rmtree(f'{name}')
    except (FileExistsError, FileNotFoundError):
        print('Такой директории не существует')
    else:
        print('Директория успешно удалена')

while True:
    menu()
    command = int(input('Введите номер желаемого действия, для выхода нажмите 5 - '))
    if command == 1:
        move_dir()
    elif command == 2:
        content_dir()
    elif command == 3:
        del_dir()
    elif command == 4:
        make_dir()
    elif command == 5:
        print('Выход из программы')
        break
    else:
        print('Команда не может быть обработана')



