#todo: Дан массив размера N. Найти минимальное растояние между одинаковыми значениями в массиве и вывести их индексы.
# Одинаковых значение может быть два и более !
#Пример:
#mass = [1,2,17,54,30,89,2,1,6,2]

#Вывод:
#Для числа 1 минимальное растояние в массиве по индексам: 0 и 7
#Для числа 2 минимальное растояние в массиве по индексам: 6 и 9
#Для числа 17 нет минимального растояния т.к элемент в массиве один.

       #0  1  2  3   4  5  6  7  8
mass = [1, 5, 3, 27, 1, 6, 3, 1, 5]

# Шаг 1: собираем индексы для каждого значения
positions = {}
for idx, val in enumerate(mass):
    positions.setdefault(val, []).append(idx)

# Шаг 2: анализируем повторы
for val, idx_list in positions.items():
    if len(idx_list) < 2:
        print(f"Для числа {val} нет минимального растояния т.к элемент в массиве один.") #Если число в массиве одно
    else:
        # Шаг 3: ищем минимальное расстояние
        min_dist = float('inf')
        min_pair = (None, None)
        for i in range(len(idx_list) - 1):
            for j in range(i + 1, len(idx_list)):
                dist = idx_list[j] - idx_list[i]
                if dist < min_dist:
                    min_dist = dist
                    min_pair = (idx_list[i], idx_list[j])
        print(f"Для числа {val} минимальное растояние в массиве по индексам: {min_pair[0]} и {min_pair[1]}")

# Если нужно вывести расстояние между индексами, расскоментировать следующую часть кода:
mass = [1, 5, 3, 27, 1, 6, 3, 1, 5]

# Шаг 1: собираем индексы для каждого значения
positions = {}
for idx, val in enumerate(mass):
    positions.setdefault(val, []).append(idx)

# Шаг 2: анализируем повторы
#for val, idx_list in positions.items():
#    if len(idx_list) < 2:
#        print(f"Для числа {val} нет минимального расстояния, т.к. элемент в массиве один.")
#    else:
#        print(f"Для числа {val} найдены пары индексов:")
#        for i in range(len(idx_list) - 1):
#            for j in range(i + 1, len(idx_list)):
#                dist = abs(idx_list[j] - idx_list[i])
#                between = dist - 1
#                print(f"  Индексы: {idx_list[i]} и {idx_list[j]} — расстояние: {dist}, между ними: {between} индекс(ов)")

