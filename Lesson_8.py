import requests
import sqlite3
import os
import sys
import json

conn = sqlite3.connect('pogoda.db')
c = conn.cursor()
from urllib.request import urlopen

cities1 = json.load(open('files/city.list.json'))
print(cities1[0])
app_id = open('files/app_id.txt', 'r').read()
print(app_id)
cities = '524901'
url = "http://api.openweathermap.org/data/2.5/weather?id={}&units=metric&appid={}".format(city_id, app_id)
print(url)
pogoda = urlopen(url)
pogoda = json.load(pogoda)
print(pogoda)
# запрос по нескольким городам city1,city2,city3 в url

def get_city(city):
    a = {}
    with open('city_list.json', 'r', encoding='utf-8') as fh:
        cities = json.load(fh)
    for item in cities:
        if city in item.values():
            a = item
    return a['id']

a = open("files/app_id.txt")  # открываем файл с ключом
my_app_id = a.read()  # читаем ключ в переменную
city = input("Введите город на английском языке: ")  # смотрим какой город нужен пользователю
url = "http://api.openweathermap.org/data/2.5/weather?id={}&units=metric&appid={}".format(get_city(city), my_app_id) #формируем url запрос
a.close()  # закрываем файл с ключом

try:  # Проверим, есть ли город в базе
    inquiry = urlopen(url)  # Отправим запрос на получение данных
    data = inquiry.json()  # Сохраним полученные данные (принимаем формат json())
    print("В {} сейчас {} градусов".format(data["name"], data["main"]["temp"]))  # по ключам вытаскиваем из json файла значения
except:
    sys.exit("Такого города нет в базе!")

save_data = input("Хотите сохранить данные в SQLite? y/n: ")
if save_data.lower() == "y":
    weather_info = [(data["id"], data["name"], data["dt"], data["main"]["temp"],
                data["weather"][0]["id"])]  # по ключам вытаскиваем данные
    conn = sqlite3.connect("pogoda.db") #коннектим базу sql
    c = conn.cursor() #создаем курсор
    c.execute(
        """CREATE TABLE IF NOT EXISTS {} (id_города INTEGER PRIMARY KEY, Город VARCHAR(255), Дата DATE, Температура INTEGER, id_погоды INTEGER)""".format(
            data["name"]))
    c.executemany("INSERT OR REPLACE INTO {} VALUES (?, ?, ?, ?, ?)".format(data["name"]),
                  weather_info)  #перезаписываем данные для другого города
    conn.commit()
    c.close()
    conn.close()
    print("Город в базе данных cities.db создан!")
else:
    print("Хорошо, создавать БД не будем.")
