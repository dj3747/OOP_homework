from src.product import Product


class Category:
    name: str
    description: str
    __products: list # Приватный атрибут
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list) -> None:
        self.name = name
        self.description = description
        self.__products = products

        # Увеличение значения атрибутов класса
        Category.category_count += 1
        Category.product_count += len(products) if products else 0

    def add_product(self, product: Product) -> None:
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты класса Product или его наследников")
        self.__products.append(product)
        Category.product_count += 1

    @property
    def product(self) -> str:
        return "\n".join(
                [f"{p.name}, {p.price} руб. Остаток: {p.quantity} шт." for p in self.__products]
    )


    def get_products(self) -> list:
        return self.__products

