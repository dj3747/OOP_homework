from src.category import Category
from src.product import Product


def test_category_creation(first_category):
    assert first_category.name == "Телевизоры"
    assert first_category.description == (
        "Современный телевизор, который позволяет наслаждаться просмотром, " "станет вашим другом и помощником"
    )
    assert first_category.get_products()[0].name == '55" QLED 4K'


def test_category_attributes(first_category):
    assert isinstance(first_category.name, str)
    assert isinstance(first_category.description, str)
    assert isinstance(first_category.get_products(), list)
    assert all(isinstance(product, Product) for product in first_category.get_products())


def test_category_and_product_count(first_category):
    assert Category.category_count == 1
    assert Category.product_count == 1

    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000, 8)
    category2 = Category(
        "Смартфоны",
        (
            "Смартфоны, как средство не только коммуникации, "
            "но и получения дополнительных функций для удобства жизни"
        ),
        [product1, product2],
    )

    assert category2.name == "Смартфоны"
    assert category2.description == (
        "Смартфоны, как средство не только коммуникации, " "но и получения дополнительных функций для удобства жизни"
    )
    assert len(category2.get_products()) == 2

    assert Category.category_count == 2
    assert Category.product_count == 3


def test_empty_category():
    category = Category("Книги", "Для саморазвития", [])
    assert category.name == "Книги"
    assert category.description == "Для саморазвития"
    assert category.get_products() == []


def test_products_property_output():
    product = Product("Смарт-часы", "AMOLED экран, датчик пульса", 12000, 7)
    category = Category("Электроника", "Полезные устройства", [product])
    expected = "Смарт-часы, 12000 руб. Остаток: 7 шт."
    assert category.products == expected


def test_add_product_successful(sample_category, sample_product):
    """Проверяет успешное добавление продукта в категорию."""
    initial_product_count = Category.product_count
    sample_category.add_product(sample_product)
    assert len(sample_category.get_products()) == 1
    assert sample_category.get_products()[0] is sample_product  # Проверяем, что это тот же самый продукт
    assert Category.product_count == initial_product_count + 1
