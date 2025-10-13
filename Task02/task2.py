# todo: Преобразуйте переменную age и foo в число
age = "23"
age_num = int(age)  # преобразование строки в число. Если строка не число, будет ошибка

foo = "23abc"
digits = ""
for char in foo:
    if char.isdigit():  # если символ — цифра
        digits += char
    else:
        break  # остановка на первом нецифровом символе

foo_num = int(digits)  # преобразование извлечённых цифр в число

# todo: Преобразуйте переменную age в Boolean
age_str = "123abc"
age_bool = bool(age_str)

# todo: Преобразуйте переменную flag в Boolean
flag = 1
flag_bool = bool(flag)

# todo: Преобразуйте значение в Boolean
str_one = "Привет"
str_two = ""
str_one_bool = bool(str_one)
str_two_bool = bool(str_two)

# todo: Преобразуйте значение 0 и 1 в Boolean
zero_bool = bool(0)
one_bool = bool(1)

# todo: Преобразуйте False в строку
false_str = str(False)

# Вывод всех результатов
print("age_num =", age_num)
print("foo_num =", foo_num)
print("age_bool =", age_bool)
print("flag_bool =", flag_bool)
print("str_one_bool =", str_one_bool)
print("str_two_bool =", str_two_bool)
print("zero_bool =", zero_bool)
print("one_bool =", one_bool)
print("false_str =", false_str)