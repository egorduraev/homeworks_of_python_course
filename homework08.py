# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
# для изменения и удаления данных.

def read_sprav():
    sprav = []
    path = 'tel_sprav.txt'
    tel_sprav = open(path, 'r', encoding='utf-8')
    for line in tel_sprav:
        n = line.split(' ')
        # print (n)
        dict_ = {
            "second_name": n[2],
            "first_name": n[1],
            "last_name": n[0],
            "tel": n[3],
        }
        sprav.append(dict_)
    tel_sprav.close()
    return sprav

def print_sprav(tel_sprav):
    for item in tel_sprav:
        print(item['last_name'], item['first_name'], item['second_name'], item['tel'])
    return None

def add_contact():
    tel_sprav = open('tel_sprav.txt', 'a', encoding='utf-8')
    s = input("Введите ФИО, тел, разделенные пробелами: ")
    tel_sprav.writelines(f'\n{s}')
    tel_sprav.close()

def find_last_name(last_name: str, my_sprav):
    for item in my_sprav:
        if item["last_name"] == last_name.capitalize():
            print(item)

def delete_contact(tel_sprav):
    print("1: Для ввода фамилии удаляемого контакта")
    print("2: Для ввода имени удаляемого контакта")
    flag = True
    x = input()
    if x == "1":
        last_name: str = input("Введите фамилию: ")
    elif x == "2":
        first_name: str = input("Введите имя: ")
        flag = False
    else:
        print("неверная команда")
        return
    
    with open('tel_sprav.txt', 'w', encoding='utf-8') as data:
        for item in tel_sprav:
            if flag == True:
                if item["last_name"] == last_name.capitalize():
                    continue
            else:
                if item["first_name"] == first_name.capitalize():
                    continue
            data.write(item['last_name'] + " " + item['first_name'] + " " + item['second_name'] + " " + item['tel'])

def change_contact(tel_sprav):
    print("1: Для ввода фамилии изменяемого контакта")
    print("2: Для ввода имени изменяемого контакта")
    flag = True
    x = input()
    if x == "1":
        last_name: str = input("Введите фамилию: ")
    elif x == "2":
        first_name: str = input("Введите имя: ")
        flag = False
    else:
        print("неверная команда")
        return
    
    with open('tel_sprav.txt', 'w', encoding='utf-8') as data:
        for item in tel_sprav:
            if flag == True:
                if item["last_name"] == last_name.capitalize():
                    print(item)
                    print("Что хотите изменить?")
                    print("1: Изменить фамилию")
                    print("2: Изменить имя")
                    print("3: Изменить отчество")
                    print("4: Изменить номер")
                    print("5: Изменить все")
                    a = input()
                    if a == "1":
                        item['last_name'] = input("Введите новую фамилию: ")
                    elif a == "2":
                        item['first_name'] = input("Введите новое имя: ")
                    elif a == "3":
                        item['second_name'] = input("Введите новое отчество: ")
                    elif a == "4":
                        item['tel'] = input("Введите новый номер: ")
                    elif a == "4":
                        item['tel'] = input("Введите новый номер: ")
                    elif a == "5":
                        s = input("Введите ФИО, тел, разделенные пробелами: ")
                        data.write(s)
                        continue
                    else:
                        print("неверная команда")
                        return
            else:
                if item["first_name"] == first_name.capitalize():
                    print(item)
                    print("Что хотите изменить?")
                    print("1: Изменить фамилию")
                    print("2: Изменить имя")
                    print("3: Изменить отчество")
                    print("4: Изменить номер")
                    print("5: Изменить все")
                    a = input()
                    if a == "1":
                        item['last_name'] = input("Введите новую фамилию: ")
                    elif a == "2":
                        item['first_name'] = input("Введите новое имя: ")
                    elif a == "3":
                        item['second_name'] = input("Введите новое отчество: ")
                    elif a == "4":
                        item['tel'] = input("Введите новый номер: ")
                    elif a == "4":
                        item['tel'] = input("Введите новый номер: ")
                    elif a == "5":
                        s = input("Введите ФИО, тел, разделенные пробелами: ")
                        data.write(s)
                        continue
                    else:
                        print("неверная команда")
                        return
            data.write(item['last_name'] + " " + item['first_name'] + " " + item['second_name'] + " " + item['tel'])

def main():
    while True:
        print("Что хотите сделать?")
        print("1: Вывести данные")
        print("2: Записать новый контакт")
        print("3: Найти контакт")
        print("4: Удалить контакт")
        print("5: Изменить контакт")
        print("0: Выйти")

        x = input()
        tel_sprav = read_sprav()
        if x == "1":
            print_sprav (tel_sprav)
        elif x == "2":
            add_contact()
        elif x == "3":
            find_last_name(input("Введите фамилию: "), my_sprav=tel_sprav)
        elif x == "4":
            delete_contact(tel_sprav)
        elif x == "5":
            change_contact(tel_sprav)
        elif x == "0":
            break
        else:
            print("неверная команда")


if __name__ == "__main__":
    main()