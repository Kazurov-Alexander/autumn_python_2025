# todo: Исправить ошибку в коде игры  ../code/ya_kube.py

# from lesson_5.code import ya_kube

#Задача пока не решена... Проблемы с импортом. Рабочее решение далее.

DICT_DEFINITION_WORD = {'ИНКАПСУЛЯЦИЯ': 'Сокрытие реализации',
                         'ПОЛИМОРФИЗМ': 'Изменение поведение при наследовании'  }

import random
import uuid
import datetime

name = input("Введите имя:")

def print_menu():
    print("""   
       1. Начать игру
       2. Сохранить игру
       3. Загрузить игру
       4. Выход из игры
       5. Настройки 
    """)

print_menu()
num = int(input("Пункт меню:"))


def generate_key() -> str:
    keys = list(DICT_DEFENITION_WORD.keys())
    random.shuffle(keys)
    return keys.pop()


def save_game(id_session, word, mask):
    # dt, id_session, name, word, mask
    f = open("save_game.csv", "at")
    dt = datetime.datetime.now()
    mask = "".join(mask)
    str = f"{dt}|{id_session}|{name}|{word}|{mask}"
    f.write(str)
    f.close()
    print("Сохранил игру!")


def load_game():
    f = open("save_game.csv", "tr")
    indx = 0
    list_str= f.readlines()
    for csv_str in list_str:
       if name in csv_str:
         print(indx, ") ", csv_str)
       indx += 1
    indx_load = int(input("Введите номер сохранения: "))
    sg = list_str[indx_load].split("|")
    key = sg[3]
    mask = sg[4]
    session_uuid = sg[1]
    print(session_uuid,key, list(mask))
    start_game(session_uuid,key.strip(), list(mask))
    exit(0)


def start_game(session_uuid, key, mask):
    list_word = list(key)
    print(DICT_DEFENITION_WORD[key])
    print("".join(mask))  # красивый вывод

    while '#' in mask:
        alfa = input("Введите букву: ").upper()

        if alfa == "2":
            print("Сохранение игры!")
            save_game(session_uuid, key, mask)
            continue

        found = False
        for i, letter in enumerate(list_word):
            if alfa == letter:
                mask[i] = alfa
                found = True

        if not found:
            print("Такой буквы нет.")
        print("".join(mask))


match num:
    case 1:
        key = generate_key()
        list_word = list(key)
        mask = ['#'] * len(key)
        session_uuid = uuid.uuid4()
        start_game(session_uuid,key,mask)
        # print('The UUID is: ' + str(session_uuid))
    case 2:
        pass
    case 3:
        load_game()
    case 4:
        print(f"Спасибо {name} за игру! Заходи еще! ")
        pass

