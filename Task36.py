# Инкапсуляция и property
# todo: Класс "Пользователь" (Валидация email)
# Создайте класс User. У него должны быть свойства email и password.
# При установке email проверяйте, что строка содержит символ @ (простая валидация).
# При установке пароля, храните не сам пароль, а его хеш (для простоты можно использовать hash()).
# Сделайте метод check_password(password), который проверяет, соответствует ли хеш переданного
# пароля сохраненному хешу.

class User:
    def __init__(self, email: str, password: str):
        self.email = email
        self.password = password  # вызывает setter

    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, value: str):
        if "@" not in value:
            raise ValueError("Некорректный email: отсутствует '@'")
        self._email = value

    @property
    def password(self):
        raise AttributeError("Доступ к паролю запрещён")

    @password.setter
    def password(self, value: str):
        self._password_hash = hash(value)

    def check_password(self, password: str) -> bool:
        return hash(password) == self._password_hash

user = User("test@example.com", "secret")
print(user.email)  # test@example.com
# print(user.password) # AttributeError
print(user.check_password("secret"))  # True
print(user.check_password("wrong"))   # False