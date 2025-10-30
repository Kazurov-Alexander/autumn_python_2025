# Модель учебных материалов
# todo: Создайте иерархию классов для представления различных типов учебных материалов.
#
# Требования: Базовый класс LearningMaterial:
# Свойства: title, author, duration_minutes
# Методы:
# display_info() - выводит основную информацию
# get_difficulty() - возвращает сложность материала (должен быть переопределен в дочерних классах)
#
# Дочерние классы:
# VideoLesson:
# Дополнительные свойства: video_quality, subtitles_available
# Сложность: "Средняя"
#
# Article:
# Дополнительные свойства: word_count, reading_level
# Сложность: рассчитывается как word_count / 1000 (легкая если <1, средняя 1-3, сложная >3)
#
# Quiz:
# Дополнительные свойства: questions_count, passing_score
# Сложность: "Высокая" если passing_score > 80, иначе "Средняя"

class LearningMaterial:
    def __init__(self, title, author, duration_minutes):
        self.title = title
        self.author = author
        self.duration_minutes = duration_minutes

    def display_info(self):
        return (f"Название: {self.title}, Автор: ({self.author}), "
                f"Длительность - {self.duration_minutes} мин.")

    def get_difficulty(self):
        raise NotImplementedError("Метод должен быть переопределён в подклассе")

class VideoLesson(LearningMaterial):
    def __init__(self, title, author, duration_minutes, video_quality, subtitles_available):
        super().__init__(title, author, duration_minutes)
        self.video_quality = video_quality
        self.subtitles_available = subtitles_available

    def get_difficulty(self):
        return "Средняя"

class Article(LearningMaterial):
    def __init__(self, title, author, word_count, reading_level):
        # duration_minutes можно оценить как word_count / 200 (примерная скорость чтения)
        duration_minutes = word_count // 200
        super().__init__(title, author, duration_minutes)
        self.word_count = word_count
        self.reading_level = reading_level

    def get_difficulty(self):
        ratio = self.word_count / 1000
        if ratio < 1:
            return "Лёгкая"
        elif 1 <= ratio <= 3:
            return "Средняя"
        else:
            return "Сложная"

class Quiz(LearningMaterial):
    def __init__(self, title, author, duration_minutes, passing_score, questions_count):
        super().__init__(title, author, duration_minutes)
        self.passing_score = passing_score
        self.questions_count = questions_count

    def get_difficulty(self):
        return "Высокая" if self.passing_score > 80 else "Средняя"

# Этот код должен работать после реализации:
materials = [
    VideoLesson("Python ООП", "Иван Иванов", 45, "1080p", True),
    Article("Глубокое обучение", "Анна Петрова", 1200, "advanced"),
    Quiz("Проверка знаний", "Платформа", 20, 75, 10)
]

for material in materials:
    print(f"{material.title}: {material.get_difficulty()}")