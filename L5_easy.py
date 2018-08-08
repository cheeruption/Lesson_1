
# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
import os
path = os.getcwd()
print(path)
for i in range(1,10):
    (os.mkdir(os.path.join(path, 'Dir_{0}'.format(i))))

input('Папки созданы. Нажмите Enter для удаления папок.')

for i in range(1,10):
    (os.rmdir(os.path.join(path, 'Dir_{0}'.format(i))))

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
import os

path = os.getcwd()
print(os.listdir(path))
d = '.'
print(list(filter(lambda x: os.path.isdir(os.path.join(d,x)), os.listdir(d))))


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
import os
import shutil

path = os.path.abspath(__file__)
path1 = os.path.join(os.getcwd(), 'L5_copy.py')
f = open(path1, 'wb')
shutil.copyfile(path, path1)
f.close()