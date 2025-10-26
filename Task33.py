# todo: Flask App https://daehnhardt.com/blog/2025/02/11/todo-flask-app/
# Расширьте приложение и добавьте него поля ввода:
# description - описание задачи
# start_date - когда начать задачу
# При добавлении двух дополнительных полей откорректируйте структуру таблицы,
# запросы на сохранение данных и шаблон вывода-вывода.

from flask import Flask, render_template, request, redirect, url_for, g
import sqlite3                                                          # Работа с SQLite базой данных
from datetime import datetime                                           # Для проверки корректности даты

app = Flask(__name__)                                                   # Инициализируем Flask-приложение
DB_PATH = 'todo.db'                                                     # Путь к файлу базы данных

# Подключение к базе данных и создание таблицы
def get_db():
    if '_db' not in g: # Проверяем, есть ли подключение к БД в контексте приложения
        g._db = sqlite3.connect(DB_PATH)  # Подключаемся к SQLite
        # Создаём таблицу задач, если она ещё не существует
        g._db.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,  -- Уникальный ID
                task TEXT NOT NULL,                    -- Название задачи
                priority INTEGER NOT NULL,             -- Приоритет (0–2)
                complete BOOLEAN NOT NULL CHECK (complete IN (0, 1)),  -- Статус выполнения
                description TEXT,                      -- Описание задачи
                start_date TEXT                        -- Дата начала (в формате YYYY-MM-DD)
            )
        ''')
    return g._db                                                        # Возвращаем подключение

# Закрытие подключения к БД после завершения запроса
@app.teardown_appcontext
def close_db(exception):
    db = g.pop('_db', None)                                             # Удаляем подключение из контекста
    if db:
        db.close()                                                      # Закрываем соединение

# Получение всех задач из базы
def fetch_tasks():
    cur = get_db().execute('SELECT * FROM tasks')                       # Получаем все строки из таблицы
    columns = [desc[0] for desc in cur.description]                     # Получаем названия столбцов
    return [dict(zip(columns, row)) for row in cur.fetchall()]          # Преобразуем строки в словари

# Проверка корректности даты
def validate_date(date_str):
    try:
        datetime.strptime(date_str, '%Y-%m-%d')                  # Пробуем распарсить дату
        return True
    except ValueError:
        return False                                                    # Если формат неверный — возвращаем False

# Главная страница: отображение всех задач
@app.route('/')
def index():
    return render_template('index.html', tasks=fetch_tasks())           # Передаём список задач в шаблон

# Добавление новой задачи
@app.route('/add', methods=['POST'])
def add():
    form = request.form                                                 # Получаем данные из формы
    start_date = form.get('start_date', '')                             # Получаем дату начала

    if start_date and not validate_date(start_date):                    # Проверяем корректность даты, если она указана
        return 'Некорректный формат даты'

    # Добавляем новую задачу в базу
    get_db().execute('''
        INSERT INTO tasks (task, priority, complete, description, start_date)
        VALUES (?, ?, ?, ?, ?)
    ''', (form['task'], int(form['priority']), False, form.get('description', ''), start_date))
    get_db().commit()                                                   # Сохраняем изменения
    return redirect(url_for('index'))                                   # Перенаправляем на главную

@app.route('/complete/<int:task_id>')                                   # Переключение статуса выполнения задачи
def complete(task_id):
    get_db().execute('UPDATE tasks SET complete = NOT complete WHERE id = ?', (task_id,))
    get_db().commit()
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')                                     # Удаление задачи
def delete(task_id):
    get_db().execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    get_db().commit()
    return redirect(url_for('index'))

@app.route('/edit/<int:task_id>', methods=['GET', 'POST'])              # Редактирование задачи
def edit(task_id):
    db = get_db()
    if request.method == 'POST':
        form = request.form
        start_date = form.get('start_date', '')

        if start_date and not validate_date(start_date):                # Проверяем корректность даты
            return 'Некорректный формат даты'
        # Обновляем данные задачи
        db.execute('''
            UPDATE tasks
            SET task = ?, priority = ?, description = ?, start_date = ?
            WHERE id = ?
        ''', (form['task'], int(form['priority']), form.get('description', ''), start_date, task_id))
        db.commit()
        return redirect(url_for('index'))
    else:                                                               # Получаем данные задачи для отображения в форме
        cur = db.execute('SELECT * FROM tasks WHERE id = ?', (task_id,))
        task = cur.fetchone()
        if not task:
            return 'Задача не найдена', 404
        columns = [desc[0] for desc in cur.description]
        return render_template('edit.html', **dict(zip(columns, task))) # Передаём данные в шаблон

if __name__ == '__main__':
    app.run(debug=True)                                                 # Запускаем Flask в режиме отладки