import pytest

from src.product import Product, Smartphone


def test_product_creation(first_product):
    assert first_product.name == "Samsung Galaxy S23 Ultra"
    assert first_product.description == "256GB, Серый цвет, 200MP камера"
    assert first_product.price == 180000.0
    assert first_product.quantity == 5


def test_product_attributes(first_product):
    assert isinstance(first_product.name, str)
    assert isinstance(first_product.description, str)
    assert isinstance(first_product.price, float)
    assert isinstance(first_product.quantity, int)


# Тесты для проверки установки положительной цены
def test_price_setter_positive(first_product, confirmation_input):
    first_product.price = 150000
    assert first_product.price == 150000


# Тесты для проверки попытки установки отрицательной цены
def test_price_setter_negative(first_product, monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "n")
    first_product.price = -5000
    assert first_product.price == 180000  # Цена не должна измениться


# Тесты для проверки попытки установки нулевой цены
def test_price_setter_zero(first_product):
    first_product.price = 0
    assert first_product.price == 180000  # Цена не должна измениться


# Тесты для проверки установки более низкой цены с подтверждением
def test_price_setter_lower_confirmed(first_product, confirmation_input):
    first_product.price = 160000  # Новая цена
    assert first_product.price == 160000


# Понижение цены при отказе пользователя
def test_price_setter_lower_rejected(first_product, monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "n")
    first_product.price = 100000
    assert first_product.price == 180000


# Уже существующий товар обновляется


def test_new_product_existing():
    existing = [Product("iPhone 15 Pro", "512GB Titanium", 199999, 2)]
    data = {"name": "iPhone 15 Pro", "description": "512GB Titanium", "price": 189999, "quantity": 1}
    updated = Product.new_product(data, existing)
    assert updated.quantity == 3
    assert updated.price == 199999


# Тест для проверки сложения продуктов
def test_product_addition(first_product, second_product):
    assert first_product + second_product == 2580000.0  # 180000.0 * 5 + 210000.0 *8 =2580000


# Тест на создание смартфона
def test_smartphone_creation(smartphone):
    """Проверяем, что объект смартфона создаётся с правильными атрибутами."""
    assert smartphone.name == "Iphone 15"
    assert smartphone.description == "512GB, Gray space"
    assert smartphone.price == 210000.0
    assert smartphone.quantity == 8
    assert smartphone.efficiency == 98.2
    assert smartphone.model == "15"
    assert smartphone.memory == 512
    assert smartphone.color == "Gray space"


# Тест на создание газонной травы
def test_lawn_grass_creation(lawn_grass):
    """Проверяем, что объект газонной травы создаётся с правильными атрибутами."""
    assert lawn_grass.name == "Газонная трава"
    assert lawn_grass.description == "Элитная трава для газона"
    assert lawn_grass.price == 500
    assert lawn_grass.quantity == 20
    assert lawn_grass.country == "Россия"
    assert lawn_grass.germination_period == 7
    assert lawn_grass.color == "Зеленый"


# Тест на сложение объектов одного класса (например, смартфонов)
def test_addition_same_class(smartphone):
    """Проверяем сложение двух объектов класса Smartphone."""
    smartphone2 = Smartphone(
        name="Samsung Galaxy S22",
        description="256GB, Черный",
        price=70000,
        quantity=3,
        efficiency=90.0,
        model="S22",
        memory=256,
        color="Черный",
    )
    assert smartphone + smartphone2 == (210000.0 * 8) + (70000.0 * 3)


def test_addition_different_classes(smartphone, lawn_grass):
    """Проверяем, что сложение объектов разных классов вызывает TypeError."""
    with pytest.raises(TypeError):
        smartphone + lawn_grass


# Тест на добавление продуктов в категорию
def test_add_product_to_category(category, smartphone, lawn_grass):
    """Проверяем, что можно добавить корректные продукты в категорию."""
    category.add_product(smartphone)
    category.add_product(lawn_grass)
    assert smartphone in category.get_products()
    assert lawn_grass in category.get_products()
