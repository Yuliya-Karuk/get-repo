# Задание-1: Решите задачу (дублированную ниже):

# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки они получают
# удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

# С использованием классов.
# Реализуйте классы сотрудников так, чтобы на вход функции-конструктора
# каждый работник получал строку из файла
import re


file_worker = open("workers.txt", "r")

# функция, чтобы посчитать количество строк в файле
def counter(X):
    count = 0
    for line in X:
        count += 1
    return count

row_worker = counter(file_worker)
file_worker.seek(0)                     #возврат на начало файла после подсчета строк
w_none = file_worker.readline()         #ненужная 1 строка


class worker:
    def __init__(self, stroke):
        self.stroke = stroke
        self.name = ''
        self.surname = ''
        self.hours = 0
        self.salary = 0
        self.needed_hours = 0
        self.position = ''
        self.worked_hours = 0

    def parseing(self):
    # разбили строку на нужные состовляющие
        self.name = re.split(r' +', self.stroke)[0]
        self.surname = re.split(r' +', self.stroke)[1]
        self.salary = re.split(r' +', self.stroke)[2]
        self.position = re.split(r' +', self.stroke)[3]
        self.needed_hour = re.split(r' +', self.stroke)[4]

    def appending_hours(self):
    # Функция, которая находит по фамилии количество отработанных часов
    # во втором файле и задает значение в переменную
        with open("hours_of.txt", 'r') as f:
            f.readline()
            for line in f.readlines():
                if re.split(r' +', line)[1] == self.surname:
                    self.worked_hours = re.split(r' +', line)[2]
                else:
                    continue


# код, который вычесляет зп из каждой строки с переменными month_salary, needed_hours, worked_hours
for i in range(0, row_worker-1):
    w = worker(file_worker.readline())
    w.parseing()
    w.appending_hours()
    if int(w.worked_hours) <= int(w.needed_hour):
        sal = int(int(w.salary) / int(w.needed_hour) * int(w.worked_hours))
    else:
        sal = int(int(w.salary) + int(w.salary) / int(w.needed_hour) * 2 * (int(w.worked_hours) - int(w.needed_hour)))
    print(f'Заработная плата {w.name} {w.surname} - {sal}')

file_worker.close()
