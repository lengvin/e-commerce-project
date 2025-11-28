class Category:
    """Класс для категории товара"""
    name: str
    description: str
    products: list

    product_count = 0
    category_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products
        Category.product_count += len(products)
        Category.category_count += 1


class Product:
    """Класс для продукта"""
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, prise, quantity):
        self.name = name
        self.description = description
        self.price = prise
        self.quantity = quantity
