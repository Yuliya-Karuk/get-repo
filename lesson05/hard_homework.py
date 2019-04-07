# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.

import os
import sys
import shutil
print('sys.argv = ', sys.argv)


def print_help():
    print("""
        help - получение справки
        mkdir <dir_name> - создание директории
        cp <file_name> - создает копию указанного файла
        rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
        cd <full_path or relative_path> - меняет текущую директорию на указанную
        ls - отображение полного пути текущей директории
        ping - тестовый ключ""")


def make_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir_name))
    except FileExistsError:
        print('директория {} уже существует'.format(dir_name))


def ping():
    print("pong")

def copy_file():
    if not file_name:
        print("Необходимо указать имя файла вторым параметром")
        return
    file_path = os.path.join(os.getcwd(), file_name)
    try:
        shutil.copyfile(file_path, f'{file_name}_copy.py')
    except FileExistsError:
        print('Копия файла {} уже существует'.format(file_name))
    else:
        print('Копия файла {} создана'.format(file_name))


def del_file():
    if not file_name:
        print("Необходимо указать имя файла вторым параметром")
        return
    try:
        answer = input('Вы уверены, что хотите удалить файл (Y/N)?')
        if answer == 'Y':
            file_path = os.path.join(os.getcwd(), file_name)
            os.remove(file_path)
        else:
            print('Команда отменена')
            return
    except FileExistsError:
        print('Файла {} не существует'.format(file_name))
    else:
        print('Файл {} успешно удален'.format(file_name))

def move_dir():
    abspath = os.path.join(os.getcwd(), path)
    try:
        os.chdir(abspath)
    except FileExistsError:
        print("Переход невозможен, папка не найдена")
    else:
        print(f"Переход в папку совершен")


def abspath_file():
    print('Отображение полного пути текущей директории - ', os.getcwd())


do = {
    "help": print_help,
    "mkdir": make_dir,
    "cp": copy_file,
    "rm": del_file,
    "cd": move_dir,
    "ls": abspath_file,
    "ping": ping
}

try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None

try:
    file_name = sys.argv[2]
except IndexError:
    file_name = None

try:
    path = sys.argv[2]
except IndexError:
    path = None

try:
    key = sys.argv[1]
except IndexError:
    key = None


if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")
