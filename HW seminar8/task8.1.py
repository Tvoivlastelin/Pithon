# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt.
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
#
# Программа должна выводить данные
# Программа должна сохранять данные в текстовом файле
# Пользователь может ввести одну из характеристик для поиска определенной записи
# (Например имя или фамилию человека)
# Использование функций. Ваша программа не должна быть линейной

def all_contact():
    with open('phonebook.txt', 'r', encoding='utf-8') as file:
        data = file.read()
        print(data)

def add_contact():
    surname = input('Введите фамилию: ')
    name = input('Введите имя: ')
    otchest = input('Введите отчество: ')
    number = input('Введите номер телефона: ')
    new_contact = (f"{surname} {name} {otchest} {number}")
    with open('phonebook.txt', 'a', encoding='utf-8') as file:
        file.write('\n'+new_contact)
    print("Контакт добавлен")
#
def finding():
    param = input("Введите параметр поиска (фамилия / имя / отчество / номер телефона) ")
    with open('phonebook.txt', 'r', encoding='utf-8') as file:
        data = file.read()
        for line in data.split("\n"):
            parts = line.split(" ")
            if param in parts:
                print(f"Фамилия:{parts[0]}, Имя:{parts[1]}, Отчество:{parts[2]}, Телефон:{parts[3]}")

print("Меню: ")
print("1. Показать весь справочник")
print("2. Добавить контакт")
print("3. Найти контакт")
print("4. Выход")
choice = int(input("Выберите пункт меню: "))
if choice == 1:
    all_contact()
elif choice == 2:
    add_contact()
elif choice == 3:
    finding()
else:
    print("Некорректный ввод")