# todo: База данных пользователя.
# Задан массив объектов пользователя

#users = [{'login': 'Piter', 'age': 23, 'group': "admin"},
#         {'login': 'Ivan',  'age': 10, 'group': "guest"},
#         {'login': 'Dasha', 'age': 30, 'group': "master"},
#         {'login': 'Fedor', 'age': 13, 'group': "guest"}]

#Написать фильтр который будет выводить отсортированные объекты по возрасту(больше введеного)
#,первой букве логина, и заданной группе.

#Сперва вводится тип сортировки:
#1. По возрасту
#2. По первой букве
#3. По группе

#тип сортировки: 1

#Затем сообщение для ввода
#Ввидите критерии поиска: 16

#Результат:
#Пользователь: 'Piter' возраст 23 года, группа "admin"
#Пользователь: 'Dasha' возраст 30 лет, группа "master"

# Исходный список пользователей — каждый элемент это словарь с login, age и group
users = [
    {'login': 'Piter', 'age': 23, 'group': "admin"},
    {'login': 'Ivan',  'age': 10, 'group': "guest"},
    {'login': 'Dasha', 'age': 30, 'group': "master"},
    {'login': 'Fedor', 'age': 13, 'group': "guest"}
]

# Запрос типа сортировки от пользователя
print("Выберите тип фильтрации пользователей:")
print("1 — По возрасту (будут выбраны те, чей возраст больше заданного)")
print("2 — По первой букве логина (например, 'D' выберет Dasha)")
print("3 — По группе (например, 'guest' выберет всех из группы guest)")

sort_type = int(input("Введите номер типа фильтрации (1-3): "))

# Запрос критерия поиска с пояснением
if sort_type == 1:
    criteria = int(input("Введите минимальный возраст: "))
elif sort_type == 2:
    criteria = input("Введите первую букву логина: ").lower()
elif sort_type == 3:
    criteria = input("Введите название группы: ").lower()
else:
    print("Неверный тип фильтрации.")
    exit()

# Создаём список отфильтрованных пользователей
filtered_users = []

for user in users:
    login = user['login']
    age = user['age']
    group = user['group']

    # Фильтрация по возрасту
    if sort_type == 1 and age > criteria:
        filtered_users.append(user)

    # Фильтрация по первой букве логина
    elif sort_type == 2 and login[0].lower() == criteria:
        filtered_users.append(user)

    # Фильтрация по группе
    elif sort_type == 3 and group.lower() == criteria:
        filtered_users.append(user)

# Вывод результата
for user in filtered_users:
    print(f"Пользователь: '{user['login']}' возраст {user['age']} года , группа \"{user['group']}\"")

    # Комментарий для фиксации в новом коммите



