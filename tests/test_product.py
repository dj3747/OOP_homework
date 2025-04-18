from tests.conftest import first_product
from src.product import Product


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