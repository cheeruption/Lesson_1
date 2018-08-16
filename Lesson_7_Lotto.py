import random
import os
import re

def give_card():
    card = []
    for i in range(3):  # создадим список из 3 строк
        card.append([])
        for j in range(9):  # и 9 клеток на каждой строке
            card[i].append([])

    x = random.sample(range(1, 91), 15)  # список из 15 уникальных случайных чисел от 1 до 90
    x[0:5], x[5:9], x[10:15] = sorted(x[0:5]), sorted(x[5:9]), sorted(
        x[10:15])  # каждые 5 чисел сортируем по возрастанию
    for num, each in enumerate(x):  # форматируем этот список для подстановки в карточку в формате NN_ либо _N_
        if len(str(each)) != 2:
            x[num] = ' ' + str(each) + ' '
        else:
            x[num] = str(each) + ' '
    y = []
    for k in range(3):
        y.append(sorted(random.sample(range(0, 9), 5)))  # для каждой строки определим какие 5 клеток заняты
    x0 = 0
    for i0 in range(3):  # для каждой строки
        for y0 in range(5):
            card[i0][y[i0][y0]] = x[x0]  # из полученного выше списка берем номера клеток и заполняем их числами
            x0 += 1
    for i in range(3):
        for num, each in enumerate(card[i]):
            if not each:  # если элемент остался пустым после заполнения карточки
                card[i][num] = ' \u2022 '  # форматируем пустой элемент для корректного отображения
    return card #получилась карточка-массив 3х9

player = give_card()
AI = give_card()

pl1 = 0 # счетчики количества закрытых клеток
ai_check = 0

def print_card(card): # функцией можем вывести карточку
    if card is player:
        print('Карточка игрока:')
    else:
        print('Карточка компьютера:')
    print('-' * 26)
    print(''.join(card[0]))
    print(''.join(card[1]))
    print(''.join(card[2]))
    print('-' * 26)

def check_num(card_pl, card_AI, num, ans): # эта функция проверяет номер бочонка в обеих карточках
    global ai_check
    global end
    check = 0
    for i in range(3):
        for j in range(9):
            if re.findall('^\s?[0-9]{1,2}\s?$',card_pl[i][j]) != []:
                if int(card_pl[i][j]) == int(num):
                    card_pl[i][j] = ("\033[42;30m{}\033[m".format(card_pl[i][j]))
                    check = 1
            if re.findall('^\s?[0-9][0-9]\s?$',card_AI[i][j]) != [] and int(card_AI[i][j]) == int(num):
                card_AI[i][j] = ("\033[42;30m{}\033[m".format(card_AI[i][j]))  # и подсвечивает номер
                ai_check += 1
    if check == 0 and ans == 'y':
        print('Вы проиграли, такого числа нет на Вашей карточке')
        end = True
    if check == 1 and ans == 'n':
        print('Вы проиграли, У Вас есть это число')
        end = True
    return check


bochonok = random.sample(range(1,91),90) #замешаем 90 бочонков в случайную последовательность

end = False
while end != True:
    print_card(player)
    num_b = bochonok.pop(0)
    while True:
            answ = input('\033[49;31mУ Вас есть номер {}? y/n \n\n\n\n\n\033[m'.format(str(num_b)))
            if answ not in 'yn':
                print_card(player)
                print('Введите корректно ответ y/n\n')
            else:
                break
    pl1 += check_num(player,AI,num_b,answ)
    if pl1 == 15 or ai_check == 15:
        end = True
        if ai_check == 15:
            print('Комп выйграл')
            print_card(AI)
        else:
            print('Вы выйграли!!!')

