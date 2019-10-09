import re
s = input('Введите слагаемые и знаки через пробел: ')
znak = re.compile('\s.\s')
znaki = znak.findall(s) #соберем знаки в список
print('Знаки в выражении:',znaki)


#удалить элемент 0 ограниченный пробелами со знаками '\D\s[0]\s\D'

elements = znak.split(s) #слагаемые представим как элементы списка
print('Cлагаемые: ', elements)
znam_glob = [] #сюда пишем список знаменателей
b = [] #сюда запишем список числителей

pattern1 = re.compile('\-\d{1,}\s\d{1,}\/\d{1,}') #шаблог на соответствие формату -nnn nnn/nnn
pattern2 = re.compile('\d{1,}\s\d{1,}\/\d{1,}') #шаблон на соответствие формату nnn nnn/nnn
pattern3 = re.compile('^\-\d{1,}$') #шаблон на соответствие формату -nnn
pattern4 = re.compile('^\d{1,}$') #шаблон на соответствие формату nnn
pattern5 = re.compile('\-\d{1,}\/\d{1,}') #шаблон -n/n
pattern6 = re.compile('^\d{1,}\/\d{1,}') #шаблон n/n

def convert_big(x):
    '''
    Функция принимает строку со слагаемым в любом виде (целые/дроби). Например: 3
    Выводит числитель и знаменатель полной дроби соответственно. Например: [9,3]
    '''
    a = [] #переменная функции для записи числителя
    znam = 1 #переменная для записи знаменателя

    if pattern1.match(x) != None:  # проверка на соответствие формату -nnn nnn/nnn
        a.append(str(int(re.search('\-\d{1,}', x).group(0)) * int(re.search('\d{1,}$', x).group(0)) - int(
            re.search('\s\d{1,}', x).group(0))))
        #a.append('/')
        znam = re.search('\d{1,}$', x).group(0)
        #a.append(re.search('\d{1,}$', x).group(0))
        a = ''.join(a)
    elif pattern2.match(x) != None:  # проверка на соответствие формату nnn nnn/nnn
        a.append(str(int(re.search('\d{1,}', x).group(0)) * int(re.search('\d{1,}$', x).group(0)) + int(
            re.search('\s\d{1,}', x).group(0))))
        #a.append('/')
        znam = re.search('\d{1,}$', x).group(0)
        #a.append(re.search('\d{1,}$', x).group(0))
        a = ''.join(a)
    elif pattern3.match(x) != None:  # проверка на соответствие формату -nnn
        a.append(str(int(re.search('\-\d{1,}', x).group(0)) ** 2 * (-1)))
        #a.append('/')
        #a.append(re.search('\d{1,}$', x).group(0))
        znam =  re.search('\d{1,}$', x).group(0)
        a = ''.join(a)
    elif pattern4.match(x) != None:  # проверка на соответствие формату nnn
        a.append(str(int(re.search('^\d{1,}', x).group(0)) ** 2))
        #a.append('/')
        #a.append(re.search('^\d{1,}', x).group(0))
        znam = re.search('\d{1,}$', x).group(0)
        a = ''.join(a)
    elif pattern5.match(x) != None:  # проверка -n/n
        a = re.search('^\-\d{1,}', x).group(0)
        znam = re.search('\d{1,}$', x).group(0)
    elif pattern6.match(x) != None:  # проверка n/n
        a = re.search('^\d+', x).group(0)
        znam = re.search('\d{1,}$', x).group(0)
    return a,znam

for i in range(len(elements)): #заполняем список числителей и знаменателей
    b.append(convert_big(elements[i])[0])
    znam_glob.append(int(convert_big(elements[i])[1]))
print('Числители:',b,'\nЗнаменатели:',znam_glob)

#зададим начальные значения числителя и знаменателя
chislit = int(str(b[0]))*int(znam_glob[1])
print(chislit)
znamen = int(znam_glob[0])
print(znamen)

for i in range(len(znaki)):
    znamen *= int(znam_glob[i+1]) #знаменатель растет с каждым слагаемым
    if '-' in znaki[i]: #вычитать или прибавлять?
        chislit -= int(b[i+1])*int(znam_glob[i])
    else:
        chislit += int(b[i + 1]) * int(znam_glob[i])
if chislit%znamen != 0:
    if chislit < 0:
        '''
        вот тут у меня огромный вопрос почему результат деления нацело 
        разный в зависимости отрицательное и положительное число делим
        '''
        print('-',abs(chislit)//znamen,''.join([str(abs(chislit)%znamen),'/', str(znamen)]))
    else:
        print(abs(chislit) // znamen, ''.join([str(abs(chislit) % znamen), '/', str(znamen)]))
else:
    print(chislit // znamen)
