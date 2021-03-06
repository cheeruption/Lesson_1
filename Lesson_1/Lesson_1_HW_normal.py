__author__ = 'Снегирев Виктор Сергеевич'

# Задача-1: Дано произвольное целое число, вывести самую большую цифру этого числа.
# Например, дается x = 58375.
# Нужно вывести максимальную цифру в данном числе, т.е. 8.
# Подразумевается, что мы не знаем это число заранее.
# Число приходит в виде целого беззнакового.
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании и понимании решите задачу с применением цикла for.

x = int(input('Введите целое число '))
max = 0
while x != 0:
    if x % 10 > max:
        max = int(x % 10)
    x = (x - x % 10)//10
print('Максимальная цифра ', max)

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.
# Подсказки:
# * постарайтесь сделать решение через действия над числами;
# * при желании и понимании воспользуйтесь синтаксисом кортежей Python.

a = float(input('Введите значение первой переменной '))
b = float(input('Введите значение второй переменной '))
a = a + b
b = a - b
a = a - b
print(a , b)

# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида
# ax² + bx + c = 0.
# Коэффициенты уравнения вводятся пользователем.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math:
# import math
# math.sqrt(4) - вычисляет корень числа 4

import math
print('Введите коэффициенты квадратного уравнения:\n')
a = float(input('a= '))
b = float(input('b= '))
c = float(input('c= '))
if a == 0:
    print('Единственное решение x =', -1*c/b)
else:
    D = b **2 - 4* a *c
    if D < 0:
        print('Корней нет')
    elif D == 0:
        print ('Только одно решение x= ', (- 1 *b ) /( 2 *a))
    else:
        print('Первое решение x1= ', (- 1 * b+ math.sqrt(D)) / (2 * a))
        print('Второе решение x2= ', (- 1 * b -math.sqrt(D)) / (2 * a))












