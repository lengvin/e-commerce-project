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
        Category.product_count += len(self.__products)
        Category.category_count += 1

    def __str__(self):
        return f'{self.name}, количество продуктов: {len(self.__products)}'

    def add_product(self, product):
        if product not in self.__products:
            self.__products.append(product)
            Category.product_count += 1

    @property
    def products(self):
        result = ''
        for product in self.__products:
            result += str(product) + ' \n'
        return result


class Product:
    """Класс для продукта"""
    name: str
    description: str
    price: float
    quantity: int

    all_products = {}

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

        Product.all_products[self.name] = self

    def __str__(self):
        return f'{self.name}, {self.price} руб. Остаток: {self.quantity} шт.'

    def __add__(self, other):
        result = self.__price * self.quantity + other.price * other.quantity
        return result

    @classmethod
    def new_product(cls, data):
        if data['name'] in [key for key in cls.all_products.keys()]:
            present_product = cls.all_products[data['name']]

            if present_product.price != data['price']:
                present_product.price = max(data['price'], present_product.price)
            present_product.quantity += data['quantity']

            return present_product
        else:
            product = cls(data['name'], data['description'], data['price'], data['quantity'])

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
