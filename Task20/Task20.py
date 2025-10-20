#todo: Выведите все строки данного файла в обратном порядке, допишите их в этот же файл.
# Для этого считайте список всех строк при помощи метода readlines().

#Содержимое файла inverted_sort.txt
#Beautiful is better than ugly.
#Explicit is better than implicit.
#Simple is better than complex.
#Complex is better than complicated.

# Результат
#Complex is better than complicated.
#Simple is better than complex.
#Explicit is better than implicit.
#Beautiful is better than ugly.

# Исходные строки
lines = [
    "Beautiful is better than ugly.",
    "Explicit is better than implicit.",
    "Simple is better than complex.",
    "Complex is better than complicated."
]

# Шаг 1: открываем файл на перезапись (очистка + запись)
with open("inverted_sort.txt", mode="w", encoding="utf-8") as file:
    # Записываем оригинальные строки
    for line in lines:
        file.write(line + "\n")

    # Записываем перевёрнутые строки
    for line in reversed(lines):
        file.write(line + "\n")

        # Комментарий для фиксации в новом коммите

