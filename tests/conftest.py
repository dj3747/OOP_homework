import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def first_product():
    return Product(
        name="Samsung Galaxy S23 Ultra", description="256GB, Серый цвет, 200MP камера", price=180000.0, quantity=5
    )


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
