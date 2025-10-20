#todo: Задан шаблон config_default.txt, где каждому в текстовом файле параметру
# нужно сопоставить данные для подстановки.

# Данные для подстановки
config_values = {
    'app_name': 'NextGen',
    'version': '1.0.0',
    'debug': True,
    'db_host': 'localhost',
    'db_port': 5432,
    'db_name': 'my_database',
    'db_user': 'admin',
    'db_password': 'secret123',
    'api_key': 'ak_123456789',
    'api_secret': 'sk_987654321',
    'base_url': 'https://api.example.com',
    'log_file': '/var/log/app.log',
    'data_dir': '/opt/app/data',
    'temp_dir': '/tmp/app',
    'max_workers': 10,
    'timeout': 30,
    'retry_attempts': 3
}

# Читаем содержимое шаблона
with open('config_default.txt', 'r', encoding='utf-8') as file:
    template_lines = file.readlines()


def process_line(line):
    has_placeholder = '? =' in line or '= ?' in line
    parts = line.split('=')
    param_part = parts[0].strip() if has_placeholder and len(parts) >= 2 else None
    value = config_values.get(param_part)

    if value is not None:
        formatted_value = f'"{value}"' if isinstance(value, str) else str(value)
        return f"{param_part:<12} = {formatted_value}\n"
    return line


result_lines = [process_line(line) for line in template_lines]

# Записываем результат в новый файл
with open('config.txt', 'w', encoding='utf-8') as file:
    file.writelines(result_lines)

print("Файл config.txt успешно создан!")

# Комментарий для фиксации в новом коммите