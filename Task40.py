# Система уведомлений (Полиморфизм)
# todo: Реализовать систему отправки уведомлений пользователям через разные каналы.
#
# Требования:
# Базовый класс NotificationSender с методом send(message, user)
# Дочерние классы:
# EmailSender: отправляет email с темой "Образовательная платформа"
# SMSSender: отправляет SMS (первые 50 символов сообщения)
# PushSender: отправляет push-уведомление с иконкой "🎓"
#
# Класс пользователя User:
# Свойства: name, preferred_notifications (список объектов NotificationSender)

class NotificationSender:
    def send(self, message, target_user):
        raise NotImplementedError("Метод send должен быть переопределён в подклассе")


class EmailSender(NotificationSender):
    def send(self, message, target_user):
        print(f"[Email] Тема: 'Образовательная платформа'\nДля: {user.name}\nСообщение: {message}")


class SMSSender(NotificationSender):
    def send(self, message, target_user):
        short_message = message[:50]
        print(f"[SMS] Для: {user.name}\nСообщение: {short_message}")


class PushSender(NotificationSender):
    def send(self, message, target_user):
        print(f"[Push] 🎓 Для: {user.name}\nСообщение: {message}")


class User:
    def __init__(self, name, preferred_notifications):
        self.name = name
        self.preferred_notifications = preferred_notifications

# Этот код должен работать после реализации:
user = User("Мария", [EmailSender(), SMSSender(), PushSender()])

# Добавлен SMSSender для отправки СМС.
# 'user' в коде переименован в 'target_user',
# так как 'user' вызывает предупреждение: "Shadows name 'user' from outer scope"
# (переменная 'user' перекрывается одноимённым параметром 'user' внутри функции
# notify_user)

def notify_user(target_user, message):
    for sender in user.preferred_notifications:
        sender.send(message, target_user)

notify_user(user, "Блок аналитики начинается с 27 октября!")
