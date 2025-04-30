class Product:
    name: str
    description: str
    __price: float  # Приватный атрибут
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if not isinstance(other, Product):
            raise TypeError("Можно складывать только объекты класса Product")
        return self.price * self.quantity + other.price * other.quantity

    @classmethod
    def new_product(cls, product_dict: dict, existing_products: list):
        """Создаёт новый товар или обновляет существующий"""
        for product in existing_products:
            if product.name == product_dict["name"]:
                # Обновляем количество товара и выбираем более высокую цену
                product.quantity += product_dict["quantity"]
                product.price = max(product.price, max(0, product_dict["price"]))  # Учитываем отрицательную цену
                return product

        # Создаем новый товар, если такого еще нет
        return cls(**product_dict)  # Используем ** для распаковки словаря

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        elif value < self.__price:
            confirm = input(f"Цена понижается с {self.__price} до {value}. Вы уверены? (y/n): ")
            if confirm.lower() == "y":
                self.__price = value
                print(f"Цена изменена на {value}")
            else:
                print("Изменение цены отменено")
        else:
            self.__price = value

class Smartphone(Product):
    def __init__(self, name: str, description: str, price: float, quantity: int,
                efficiency: str, model: str, memory: int, color: str):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __str__(self):
        return  (f"{self.name}, Модель: {self.model}, Память: {self.memory}GB, Производительность: {self.efficiency},"
                 f" Цвет: {self.color}, Цена: {self.price} руб. Остаток: {self.quantity} шт.")

    def __add__(self, other):
        if type(self) is not type(other): # Используем type() для проверки типа объекта
            raise TypeError("Складывать можно только объекты класса Smartphone")
        return super().__add__(other)

class LawnGrass(Product):
    def __init__(self, name: str, description: str, price: float, quantity: int,
                country: str, germination_period: int, color: str):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __str__(self):
        return (f"{self.name}, Страна: {self.country},"
                f" Срок прорастания: {self.germination_period} дней, Цвет: {self.color}")

    def __add__(self, other):
        if type(self) is not type(other): # Используем type() для проверки типа объекта
            raise TypeError("Складывать можно только объекты класса LawnGrass")
        return super().__add__(other)

class ProductCategory:
    def __int__(self):
        self.products = []

    def add_products(self, product):
        if not isinstance(product, Product): # Проверка через isinstance
            raise TypeError("Можно добавлять объекты только класса Product и его наследников")
        self.products.append(product)

    def __str__(self):
        return "\n".join(str(product) for product in self.products)
