from random import *
import json

films = []

def save():
    with open("films.json", "w", encoding = "utf-8") as fh:
        fh.write(json.dumps(films, ensure_ascii = False))
        print("Успешное сохранение в файле films.json")

def load():
    with open("films.json", "r", encoding = "utf-8") as fh: #ключ r - read
        films = json.load(fh)
    print("Успешное загрузка из файла films.json")

try:
    with open("films.json", "r", encoding = "utf-8") as fh: #ключ r - read
        films = json.load(fh)
    print("Успешное загрузка из файла films.json")
    #load(films.json)
except:
    films.append('matrica')
    films.append('kingdoom')
    films.append('elektronik')
    films.append('viy')
    films.append('office')

while True:
    command = input("введите команду: ")
    if command == "/start":
        print('Бот начал свою работу')

    elif command == "/stop":
        print("Бот завершил работу.")
        save()
        break

    elif command == "/show_all":
        print("текущий список фильмов:")
        print(films)

    elif command == "/add":
        f = input("введите название фильмa: ")
        films.append(f)
        print("фильм добавлен")

    elif command == "/help":
        print("показали мануал")

    elif command == "/del":
        f = input("введите название фильмa для его удаления: ")
        """
        if f in films:  # первый способ
            films.remove(f)
            print("фильм удален")
        else:
            print("такого фильма в коллекции нет")
        """   
        try:  # второй способ
            films.remove(f)
            print("фильм удален")
        except:
            print("такого фильма в коллекции нет")  

    elif command == "/random":
        # rnd = randint(0, len(films) - 1)  # 1 sposob
        # print("Рекомендуемый фильм: " + films[rnd])     
        print("Рекомендуемый фильм: " + choice(films))  # 2 sposob

    elif command == "/save":
        save()

    elif command == "/load":
        load()

    else:
        print("неизвестная команда. изучите мануал по команде /help")
