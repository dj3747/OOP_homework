import pytest

from src.category import Category
from src.product import LawnGrass, Product, Smartphone


@pytest.fixture
def first_product():
    return Product(
        name="Samsung Galaxy S23 Ultra", description="256GB, Серый цвет, 200MP камера", price=180000.0, quantity=5
    )


@pytest.fixture
def second_product():
    return Product(name="Iphone 15", description="512GB, Gray space", price=210000.0, quantity=8)


@pytest.fixture
def first_category():
    Category.category_count = 0  # Сбросить значение переменной класса перед тестами
    Category.product_count = 0

    product4 = Product(name='55" QLED 4K', description="Фоновая подсветка", price=123000.0, quantity=7)

    return Category(
        name="Телевизоры",
        description="Современный телевизор, "
        "который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        products=[product4],
    )


# Фикстура для подтверждения ввода
@pytest.fixture
def confirmation_input(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "y")


@pytest.fixture
def sample_category():
    return Category("Test Category", "Test Description", [])


@pytest.fixture
def sample_product():
    return Product("Test Product", "Test Description", 100.0, 10)


@pytest.fixture
def smartphone():
    return Smartphone(
        name="Iphone 15",
        description="512GB, Gray space",
        price=210000.0,
        quantity=8,
        efficiency=98.2,
        model="15",
        memory=512,
        color="Gray space",
    )


@pytest.fixture
def lawn_grass():
    return LawnGrass(
        name="Газонная трава",
        description="Элитная трава для газона",
        price=500,
        quantity=20,
        country="Россия",
        germination_period="7 дней",
        color="Зеленый",
    )


@pytest.fixture
def category():
    return Category(name="Смартфоны", description="Высокотехнологичные устройства", products=[])
