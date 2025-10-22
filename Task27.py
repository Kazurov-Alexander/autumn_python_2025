#todo: Числа в буквы
#Замените числа, написанные через пробел, на буквы. Не числа не изменять.

#Пример.
#Input	                            Output
#8 5 12 12 15	                    hello
#8 5 12 12 15 , 0 23 15 18 12 4 !	hello, world!

def numbers_to_letters(text):
    result = ''
    for token in text.split():
        if token.isdigit():
            num = int(token)
            if 1 <= num <= 26:
                result += chr(ord('a') + num - 1)  # 1 → a, 2 → b, ..., 26 → z
            else:
                result += token  # число вне диапазона
        else:
            result += token  # не число — оставить как есть
    return result

# Примеры для проверки
input_1 = "8 5 12 12 15"
input_2 = "8 5 12 12 15 , 23 15 18 12 4 !"

print(numbers_to_letters(input_1))  # hello
print(numbers_to_letters(input_2))  # hello, world!


