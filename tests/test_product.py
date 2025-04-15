from src.product import Category, Product


def test_product_creation(first_product):
    assert first_product.name == "Samsung Galaxy S23 Ultra"
    assert first_product.description == "256GB, Серый цвет, 200MP камера"
    assert first_product.price == 180000
    assert first_product.quantity == 5


def test_product_attributes(first_product):
    assert isinstance(first_product.name, str)
    assert isinstance(first_product.description, str)
    assert isinstance(first_product.price, int)
    assert isinstance(first_product.quantity, int)


def test_category_creation(first_category):
    assert first_category.name == "Телевизоры"
    assert first_category.description == (
        "Современный телевизор, который позволяет наслаждаться просмотром, " "станет вашим другом и помощником"
    )
    assert first_category.products[0].name == '55" QLED 4K'


def test_category_attributes(first_category):
    assert isinstance(first_category.name, str)
    assert isinstance(first_category.description, str)
    assert isinstance(first_category.products, list)
    assert all(isinstance(product, Product) for product in first_category.products)


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
    assert len(category2.products) == 2

    assert Category.category_count == 2
    assert Category.product_count == 3
