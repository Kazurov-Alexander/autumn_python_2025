# todo: Создайте иерархию классов для экспорта данных в разные форматы.
# Требования:
# Абстрактный базовый класс DataExporter:
#
# Методы:
# export(self, data) - абстрактный метод
# get_format_name(self) - возвращает название формата
# validate_data(self, data) - общий метод проверки данных (не пустые ли)
#
# Конкретные реализации:
# JSONExporter:
# Экспортирует данные в JSON-формат
# Добавляет поле "export_timestamp" с текущим временем
#
# CSVExporter:
# Экспортирует данные в CSV (если data - список словарей)
# Автоматически определяет заголовки из ключей первого элемента
#
# XMLExporter:
# Создает XML структуру с корневым элементом <report>
# HTMLExporter (дополнительно):
# Создает красивую HTML-таблицу с CSS-стилями

import json
import csv
import datetime
import xml.etree.ElementTree as ET
from abc import ABC, abstractmethod


class DataExporter(ABC):
    @abstractmethod
    def export(self, data):
        pass

    @abstractmethod
    def get_format_name(self):
        pass

    def validate_data(self, data):
        if not data:
            raise ValueError("Данные пусты или отсутствуют.")


class JSONExporter(DataExporter):
    def export(self, data):
        self.validate_data(data)
        export_data = {
            "data": data,
            "export_timestamp": datetime.datetime.now().isoformat()
        }
        print(json.dumps(export_data, indent=2, ensure_ascii=False))

    def get_format_name(self):
        return "JSON"


class CSVExporter(DataExporter):
    def export(self, data):
        self.validate_data(data)
        if not isinstance(data, list) or not all(isinstance(row, dict) for row in data):
            raise ValueError("Для CSV экспортируются только списки словарей.")
        fieldnames = list(data[0].keys())
        with open("output.csv", "w", newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for row in data:
                writer.writerow(row)
        print(','.join(fieldnames))
        for row in data:
            print(','.join(str(row[field]) for field in fieldnames))

    def get_format_name(self):
        return "CSV"


class XMLExporter(DataExporter):
    def export(self, data):
        self.validate_data(data)
        root = ET.Element("report")
        for item in data:
            entry = ET.SubElement(root, "item")
            for key, value in item.items():
                child = ET.SubElement(entry, key)
                child.text = str(value)
        xml_str = ET.tostring(root, encoding='unicode')
        print(xml_str)

    def get_format_name(self):
        return "XML"


class HTMLExporter(DataExporter):
    def export(self, data):
        self.validate_data(data)
        headers = list(data[0].keys())
        header_cells = ''.join(f"         <th>{h.capitalize()}</th>\n" for h in headers)
        row_lines = []
        for row in data:
            cells = ''.join(f"         <td>{row.get(h, '')}</td>\n" for h in headers)
            row_html = "      <tr>\n" + cells + "      </tr>\n"
            row_lines.append(row_html)
        body_rows = ''.join(row_lines)

        html = f"""<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <title>Отчёт</title>
  <style>
    body {{
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
      margin: 30px;
      background-color: #f5f5f5;
      color: #333;
    }}
    h2 {{
      color: #e67e22;
      border-bottom: 2px solid #f1c40f;
      padding-bottom: 8px;
      margin-top: 0;
    }}
    table {{
      border-collapse: collapse;
      width: 100%;
      margin-top: 15px;
      box-shadow: 0 4px 10px rgba(0, 0, 0, 0.08);
      border-radius: 6px;
      overflow: hidden;
    }}
    th, td {{
      border: 1px solid #d5dbdb;
      padding: 12px 15px;
      text-align: left;
    }}
    th {{
      background-color: #f1c40f;
      color: #2c3940;
      font-weight: bold;
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }}
    tr:nth-child(even) {{
      background-color: #fdf2e5;
    }}
    tr:hover {{
      background-color: #ffeaa7;
    }}
    td {{
      color: #2c3940;
    }}
  </style>
</head>
<body>
  <h2>Отчёт по товарам</h2>
  <table>
    <thead>
      <tr>
{header_cells}      </tr>
    </thead>
    <tbody>
{body_rows}    </tbody>
  </table>
</body>
</html>"""
        print(html)

    def get_format_name(self):
        return "HTML"


# Демонстрация работы
sales_data = [
    {
        "product": "Laptop",
        "price": 1000,
        # "quantity": 2,  # закомментировано как ненужное поле
        # "sku": "LTP-1000",  # пример дополнительных полей, закомментированы
        # "manufacturer": "BrandX",
    },
    {
        "product": "Mouse",
        "price": 50,
        # "quantity": 10,  # закомментировано
        # "color": "black",
    }
]

exporters = [
    JSONExporter(),
    CSVExporter(),
    XMLExporter(),
    HTMLExporter(),
]

for exporter in exporters:
    print(f"Формат: {exporter.get_format_name()}")
    exporter.export(sales_data)
    print("---")

# Этот код должен работать после реализации:
sales_data = [
    {"product": "Laptop", "price": 1000, "quantity": 2},
    {"product": "Mouse", "price": 50, "quantity": 10}
]

exporters = [
    JSONExporter(),
    CSVExporter(),
    XMLExporter()
]

for exporter in exporters:
    print(f"Формат: {exporter.get_format_name()}")
    exporter.export(sales_data)
    print("---")