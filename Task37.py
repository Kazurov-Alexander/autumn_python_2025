# Инкапсуляция и property
# todo: Класс "Товар" (Защита от отрицательной цены)
# Создайте класс Product. У него есть свойства name (простая строка) и price.
# При установке цены проверяйте, что она не отрицательная.
# Если пытаются установить отрицательную цену, устанавливайте 0.

class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price  # вызывает setter

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, value: float):
        if value < 0:
            self._price = 0
        else:
            self._price = value

product = Product("Book", 10)
print(product.price)  # 10
product.price = -5
print(product.price)  # 0