from classes import Product, Category
import json


def read_json_file(file_path):
    """
    Открытие JSON-файла
    """
    try:
        with open(file_path, encoding='utf-8') as file:
            json_file = json.load(file)
    except Exception as e:
        print(e)
        return []
    else:
        return json_file


def create_product(data):
    """
    Создание продукта из словаря
    """
    product_dict = {}
    for key, value in data.items():
        product_dict[key] = value
    product = Product(product_dict['name'],
                      product_dict['description'],
                      product_dict['price'],
                      product_dict['quantity'])
    return product


def create_category(file):
    """
    Создание категории из словаря
    """
    category_dict = {}
    result_list = []
    for data in file:
        for key, value in data.items():
            category_dict[key] = value
        category_dict['products'] = [create_product(product) for product in category_dict['products']]
        category = Category(category_dict['name'], category_dict['description'], category_dict['products'])
        result_list.append(category)
    return result_list
