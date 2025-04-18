class Category:
    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list) -> None:
        self.name = name
        self.description = description
        self.products = products

        # Увеличение значения атрибутов класса
        Category.category_count += 1
        Category.product_count += len(products) if products else 0
