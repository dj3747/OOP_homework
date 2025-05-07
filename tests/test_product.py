import pytest

from src.product import BaseProduct, LawnGrass, Product, Smartphone


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
    assert lawn_grass.germination_period == "7 дней"
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


def test_add_product_to_category(category, smartphone, lawn_grass):
    """Проверяем, что можно добавить корректные продукты в категорию."""
    category.add_product(smartphone)
    category.add_product(lawn_grass)
    assert smartphone in category.get_products()
    assert lawn_grass in category.get_products()


# Тест на проверку создания базового продукта
def test_product_creation(capsys):
    first_product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000, 5)
    assert first_product.name == "Samsung Galaxy S23 Ultra"
    assert first_product.description == "256GB, Серый цвет, 200MP камера"
    assert first_product.price == 180000
    assert first_product.quantity == 5

    captured = capsys.readouterr()
    assert "Создан объект класса Product" in captured.out


# Тест на создание газонной травы с проверкой базового класса и миксина
def test_lawn_grass_creation_with_base_and_mixin(capsys):
    lawn_grass = LawnGrass("Газонная трава", "Описание", 500, 20, "Россия", "7 дней", "Зеленый")

    # Проверка атрибутов
    assert lawn_grass.name == "Газонная трава"
    assert lawn_grass.price == 500
    assert lawn_grass.quantity == 20
    assert lawn_grass.country == "Россия"
    assert lawn_grass.germination_period == "7 дней"

    # Проверка наследования от BaseProduct
    assert isinstance(lawn_grass, BaseProduct)

    # Проверка логирования из InitLoggingMixin
    captured = capsys.readouterr()
    assert "Создан объект класса LawnGrass" in captured.out

# Тест на использование миксина InitLoggingMixin
def test_init_logging_mixin(capsys):
    # Создаем объект LawnGrass для проверки работы миксина
    lawn_grass = LawnGrass("Газонная трава", "Описание",
                           500, 20, "Россия", "7 дней", "Зеленый")

    # Проверяем логирование в выводе
    captured = capsys.readouterr()
    assert "Создан объект класса LawnGrass" in captured.out

    # Проверяем наличие метода __repr__, добавленного миксином
    assert hasattr(lawn_grass, "__repr__")

# Тест на попытку создать товар с нулевым количеством
def test_product_with_zero_quantity():
    with pytest.raises(ValueError, match="Товар с нулевым количеством не может быть добавлен"):
        Product("Test Product", "Описание", 1500.0, 0)
