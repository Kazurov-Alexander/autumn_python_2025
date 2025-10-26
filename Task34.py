# todo: Перепишите игру "Поле чудес" на классах.

import uuid
import datetime
import random
from db import DICT_DEFENITION_WORD


def generate_key() -> str:
    keys = list(DICT_DEFENITION_WORD.keys())
    random.shuffle(keys)
    return keys.pop()


class Yakube:
    def __init__(self):
        # Сохранение имени игрока до старта
        self.name = input("Введите имя:")

        self.session_uuid = None
        self.key = None
        self.mask = []
        self.list_word = []
    @staticmethod
    def print_menu():
       print("""   
                1. Начать игру
                2. Сохранить игру
                3. Загрузить игру
                4. Выход из игры
                5. Настройки 
            """)
    def start_game(self, key=None, mask=None, list_word=None):
        if key is None:
            self.key = generate_key()
            self.mask = ['#'] * len(self.key)
            self.list_word = list(self.key)
            self.session_uuid = uuid.uuid4()
        else:
            self.key = key
            self.mask = mask
            self.list_word = list_word

        print(DICT_DEFENITION_WORD[self.key])
        print(self.mask)

        while '#' in self.mask:
            alfa = input("Введите букву: (2 - сохранить игру, 4 - выход из игры)")
            if alfa == "2":
                print("Сохранение игры!")
                self.save_game()
                continue
            elif alfa == "4":
                print("Выход из игры")
                return

            cnt = 0
            for i in self.list_word:
                if alfa == i:
                    self.mask[cnt] = alfa
                cnt += 1

            print(self.mask)
        print("Слово полностью угадано:", self.key)
    def save_game(self):
        if  self.key is None:
            print("Нет активной игры для сохранения!")
            return
        f = open("save_game.csv", "at", encoding="utf-8")
        dt = datetime.datetime.now()
        mask_str = "".join(self.mask)
        str_to_write = f"{dt}|{self.session_uuid}|{self.name}|{self.key}|{mask_str}\n"
        f.write(str_to_write)
        f.close()
        print("Сохранил игру!")
    def load_game(self):
        try:
            with open("save_game.csv", "r", encoding="utf-8") as f:
                list_str = f.readlines()
            saved_games = []
            for csv_str in list_str:
                if self.name in csv_str:
                    saved_games.append(csv_str.strip())
            if not saved_games:
                print("Нет сохраненных игр связанных с учётной записью!")
                return False

            yakube_game = Yakube()
            yakube_game.run()

            for idx, yakube_game in enumerate(saved_games):
                print(f"{idx}) {game}")
            try:
                index_load = int(input("Введите номер:"))
                if index_load < 0 or index_load >= len(saved_games):
                    print("Неверный номер сохранения!")
                    return False

                sg = saved_games[index_load].split("|")
                if len(sg) < 5:
                    print("Неверный файл сохранения")
                    return False

                key = sg[3]
                mask_str = (sg[4])
                mask = list(mask_str)
                # Преобразуем строку в UUID
                session_uuid = uuid.UUID(sg[1])

                print ("Загрузка игры:", session_uuid, mask_str)

                self.session_uuid = session_uuid

                self.start_game(key, mask, list(key))
                return True

            except ValueError:
                print("Неверный номер сохранения")
                return False
        except FileNotFoundError:
            print("Файл сохранений не найден")
            return False

    def run(self):
        while True:
            self.print_menu()
            try:
                num = int(input("Пункт меню:"))
                match num:
                    case 1:
                        self.start_game()
                    case 2:
                        self.save_game()
                    case 3:
                        self.load_game()
                    case 4:
                        print(f"Спасибо {self.name} за игру! Заходи еще! ")
                        return
                    case 5:
                        print(f"Спасибо за интерес, {self.name}, настройки пока в разработке! ")
                    case _:
                        print("Неверный пункт меню!")
            except ValueError:
                print("Неверный пункт меню!")

if __name__ == "__main__":
    game = Yakube()
    game.run()