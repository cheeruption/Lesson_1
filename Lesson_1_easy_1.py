import random

number = (random.randint(-999999999999999, 999999999999999))
print('Произвольное число: ', number)

if number < 0:
    number = number * -1

#метод будет хранить заданное число и каждый цикл отсекать
#ненужную часть арифметическими действиями (деление и вычитание)

if number <= 9:
    print(number)
else:
    delit = 10
    print('\nСписок символов из числа:')
    while number / delit >= 0.1:
        number1 = ((number % delit) - (number % (0.1 * delit))) / (0.1 * delit)
        print(int(number1))
        delit = delit * 10

#Вывод цифр через цикл for

print('\nCписок полученный циклом for:')
number = str(number)

for x in number:
    print(x)
