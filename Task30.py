# todo: Вы работаете с данными цен товаров, которые приходят в разном формате.
# Создайте список числовых значений цен,  игнорируя некорректные записи.
# Все цены переведите в рубли. Задачу следует решить с использованием списковых включений.

prices = ["₽1500", "20.50 USD", "invalid", "€25.00", "$15.99",  "18.99", "N/A", "¥5000"]

# Функция для извлечения числового значения и валюты
def parse_price(p):
    p = p.strip()
    if p.startswith("₽"):
        return float(p[1:]), "RUB"
    elif p.endswith("USD") or p.startswith("$"):
        return float(p.replace("USD", "").replace("$", "").strip()), "USD"
    elif p.endswith("EUR") or p.startswith("€"):
        return float(p.replace("EUR", "").replace("€", "").strip()), "EUR"
    elif p.endswith("JPY") or p.startswith("¥"):
        return float(p.replace("JPY", "").replace("¥", "").strip()), "JPY"
    elif p.replace(".", "", 1).isdigit():
        return float(p), "RUB"
    else:
        return None

# Курсы валют
exchange_rates = {
    "USD": 93.0,
    "EUR": 98.0,
    "JPY": 0.63,
    "RUB": 1.0
}

# Списковое включение с фильтрацией и переводом в рубли
converted_prices = [
    round(value * exchange_rates[currency], 2)
    for p in prices
    if (parsed := parse_price(p)) is not None
    for value, currency in [parsed]
]

print(converted_prices)