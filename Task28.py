#todo: Взлом шифра
#Вы знаете, что фраза зашифрована кодом цезаря с неизвестным сдвигом.
#Попробуйте все возможные сдвиги и расшифруйте фразу.


#grznuamn zngz cge sge tuz hk uhbouay gz loxyz atrkyy eua'xk jazin.

def caesar_decrypt(text, shift):
    result = ''
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base - shift) % 26 + base)
        else:
            result += char
    return result

# Зашифрованная фраза
cipher_text = "grznuamn zngz cge sge tuz hk uhbouay gz loxyz atrkyy eua'xk jazin."

# Перебор всех возможных сдвигов
for shift in range(1, 26):
    decrypted = caesar_decrypt(cipher_text, shift)
    print(f"Сдвиг {shift:2}: {decrypted}")

#Единственная осмысленная фраза из вывода: "although that way may not be obvious at first unless you're dutch".
# Перевод: "Хотя этот путь может быть неочевиден поначалу, если вы не голландец".
