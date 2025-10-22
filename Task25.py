# todo: Шифр Цезаря
# Описание шифра.
# В криптографии шифр Цезаря, также известный шифр сдвига, код Цезаря или сдвиг Цезаря,
# является одним из самых простых и широко известных методов шифрования.
# Это тип подстановочного шифра, в котором каждая буква в открытом тексте заменяется буквой на некоторое
# фиксированное количество позиций вниз по алфавиту. Например, со сдвигом влево 3, D будет заменен на A,
# E станет Б, и так далее. Метод назван в честь Юлия Цезаря, который использовал его в своей частной переписке.

# Задача.
# Считайте файл message.txt и зашифруйте  текст шифром Цезаря, при этом символы первой строки файла должны
# циклически сдвигаться влево на 1, второй строки — на 2, третьей строки — на три и т.д.
# В этой задаче удобно считывать файл построчно, шифруя каждую строку в отдельности.
# В каждой строчке содержатся различные символы. Шифровать нужно только буквы кириллицы.

def caesar_cipher(text, shift):
    alphabet_upper = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    alphabet_lower = alphabet_upper.lower()
    result = ''

    for char in text:
        if char in alphabet_upper:
            idx = alphabet_upper.index(char)
            new_idx = (idx - shift) % len(alphabet_upper)
            result += alphabet_upper[new_idx]
        elif char in alphabet_lower:
            idx = alphabet_lower.index(char)
            new_idx = (idx - shift) % len(alphabet_lower)
            result += alphabet_lower[new_idx]
        else:
            result += char
    return result


# Чтение и шифрование построчно
with open('message.txt', encoding='utf-8') as f:
    lines = f.readlines()

with open('encrypted.txt', 'w', encoding='utf-8') as f_out:
    for i, line in enumerate(lines):
        shift = i + 1
        encrypted_line = caesar_cipher(line.strip(), shift)
        f_out.write(encrypted_line + '\n')


