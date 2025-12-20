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

    def add_product(self, product):
        if product not in self.__products:
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

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

        Product.all_products[self.name] = self

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


# product1 = Product('1', '1', 1, 1)
# productN = Product.new_product({'name': '2',
#                                 'description': '2',
#                                 'price': 2,
#                                 'quantity': 2})
# print(Product.all_products)
# print(product1.quantity)
# print(productN.quantity)
#
# category1 = Category('aaa', 'aaa', [product1])
# print(Product.all_products)
# print(product1.quantity)
# print(productN.quantity)
# print(category1.product_count)
# print(category1.products)
#
# category1.add_product(productN)
# print(Product.all_products)
# print(product1.quantity)
# print(productN.quantity)
# print(category1.product_count)
# print(category1.products)
