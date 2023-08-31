import json

# Загрузка данных из Json-файла
def load_data(filename):
    try:
        with open(filename, "r") as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        return {}


# Сохранение данных в Json-файл
def save_data(data, filename):
    with open(filename, "w") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


# Основная функция
def main():
    filename = "phonebook.json"
    phonebook = load_data(filename)

    while True:
        print()
        print("Телефонный справочник")
        print("1. Просмотр всех записей справочника")
        print("2. Добавление нового контакта")
        print("3. Поиск контакта по имени")
        print("4. Удаление контакта")
        print("5. Сохранение контакта")
        print("6. Выход из программы")

        choice = input("Выберите номер нужного действия: ")
        print()

        if choice == "1":
            for name, contact in phonebook.items():
                print(f"Имя: {name}")
                print(f"Телефоны: {contact['Phone']}")
                print(f"День рождения: {contact['birthday']}")
                print(f"e-mail: {contact['e-mail']}")
                print("-" * 40)

        elif choice == "2":
            name = input("Введите имя: ")
            phone = input("Введите номер телефона: ")
            birthday = input("Введите день рождения: ")
            email = input("Введите e-mail: ")

            phonebook[name] = {"Phone": phone, "birthday": birthday, "e-mail": email}
            save_data(phonebook, filename)
            print(f"Контакт {name} успешно добавлен и сохранен.")

        elif choice == "3":
            search_name = input("Введите имя для поиска: ")
            if search_name in phonebook:
                print("Найдено:")
                contact = phonebook[search_name]
                print(f"Имя: {search_name}")
                print(f"Телефоны: {', '.join(contact['Phone'])}")
                print(f"День рождения: {contact['birthday']}")
                print(f"e-mail: {contact['e-mail']}")
            else:
                print("Контакт не найден.")

        elif choice == "4":
            delete_name = input("Введите имя для удаления: ")
            if delete_name in phonebook:
                del phonebook[delete_name]
                print("Контакт удален.")
                save_data(phonebook, filename)
            else:
                print("Контакт не найден.")

        elif choice == "5":
            save_data(phonebook, filename)
            print("Данные сохранены.")

        elif choice == "6":
            save_data(phonebook, filename)
            print("Данные сохранены. Программа завершена.")
            break

main()