#todo: Требуется создать csv-файл «algoritm.csv» со следующими столбцами:
# id) - номер по порядку (от 1 до 10);
# значение из списка algoritm

import csv

algoritm = [
    "C4.5", "k - means", "Метод опорных векторов",
    "Apriori", "EM", "PageRank", "AdaBoost", "kNN",
    "Наивный байесовский классификатор", "CART"
]

with open("algoritm.csv", mode="w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)

    # Записываем заголовки (опционально)
    writer.writerow(["id)", "Алгоритм"])

    # Записываем строки
    for idx, name in enumerate(algoritm, start=1):
        writer.writerow([f"{idx})", name])

# Комментарий для фиксации в новом коммите
