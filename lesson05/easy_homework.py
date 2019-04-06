# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os

'''print('Путь к текущей директории', os.getcwd())
files = os.listdir(path=os.getcwd())
print('Файлы в текущей директории', files)

# Создаем новую директорию

for i in range(1, 10):
    dir_path = os.path.join(os.getcwd(), f'dir_{i}')
    print(dir_path)
    try:
        os.mkdir(dir_path)
    except FileExistsError:
        print('Такая директория уже существует')

# Проверка создались ли директории
files = os.listdir(path=os.getcwd())
print('Файлы в текущей директории', files)

# Удаление директорий
for i in range(1, 10):
    try:
        os.rmdir(f'dir_{i}')
    except FileExistsError:
        print('Такая директория уже не существует')

# Проверка удалились ли директории
files = os.listdir(path=os.getcwd())
print('Файлы в текущей директории', files)


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

files = [i for i in os.listdir(path=os.getcwd()) if os.path.isdir(i)]
print('Папки в текущей директории', files)

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.'''

import shutil
import sys

file_path = sys.argv[0]
name = file_path.split("/")[-1]
name = file_path.split(".")[0]
print(name)
shutil.copyfile(file_path, f'{name}.copy.py')

# Проверка создалась ли копия в текущей директории
files = [i for i in os.listdir(path=os.getcwd()) if os.path.isfile(i)]
print('Файлы в текущей директории', files)





