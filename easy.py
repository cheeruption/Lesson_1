import os


def new_dir(name_dir):       # создание новой папки
    os.mkdir(name_dir)


def delete_dir(name_dir):       # удаление папки
    os.rmdir(name_dir)

def list_dir():        #содержимое текущей директории
    print(os.listdir(os.getcwd()))

def change_dir(dir_name):                       # смена директории
    os.chdir(path)
