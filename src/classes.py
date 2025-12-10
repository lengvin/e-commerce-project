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
        self.__products = products
        Category.product_count += len(products)
        Category.category_count += 1

    def add_product(self, product):
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        result = ''
        for product in self.__products:
            result = result + f'{product.name}, {product.price} руб. Остаток: {product.quantity} шт. \n'
        return result


class Product:
    """Класс для продукта"""
    name: str
    description: str
    price: float
    quantity: int

    all_products = {}

    def __init__(self, name, description, prise, quantity):
        self.name = name
        self.description = description
        self.__price = prise
        self.quantity = quantity

        Product.all_products[self.name] = self

    @classmethod
    def new_product(cls, data):
        product = cls(data['name'], data['description'], data['price'], data['quantity'])
        if product.name in [key for key in cls.all_products.keys()]:
            present_product = cls.all_products[product.name]

            if present_product.price != product.price:
                present_product.price = max(product.price, present_product.price)
            present_product.quantity += product.quantity

            return present_product
        else:
            cls.all_products[product.name] = product

            return product

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        new_price = float(new_price)

        if new_price <= 0:
            print('Цена не должна быть нулевая или отрицательная')
        else:
            if self.__price > new_price:
                print('Вы точно хотите понизить цену? Введите y - если да или n - если нет')
                while True:
                    user_input = input().lower()
                    if user_input == 'y':
                        self.__price = new_price
                        break
                    elif user_input == 'n':
                        break
                    else:
                        print('Некорректный ввод, повторите попытку')
            else:
                self.__price = new_price
