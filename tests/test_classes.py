from src.classes import Product, Category
import pytest


@pytest.fixture
def dict_new_product():
    result = {'name': 'test_new_product',
              'description': 'test_new_description',
              'price': 5000.0,
              'quantity': 6}
    return result


@pytest.fixture
def some_product():
    product = Product("test_name",
                      "test_description",
                      1000.0,
                      5)
    return product


@pytest.fixture
def some_category(some_product):
    Category.product_count = 0
    Category.category_count = 0
    category = Category("test_name",
                        "test_description",
                        [some_product])
    return category


@pytest.fixture
def new_product(dict_new_product):
    Product.all_products.clear()
    new_product = Product.new_product(dict_new_product)
    return new_product


def test_init_product(some_product):
    assert some_product.name == "test_name"
    assert some_product.description == "test_description"
    assert some_product.price == 1000.0
    assert some_product.quantity == 5


def test_init_category(some_category, some_product):
    assert some_category.name == "test_name"
    assert some_category.description == "test_description"
    assert some_category.products == 'test_name, 1000.0 руб. Остаток: 5 шт. \n'
    assert some_category.category_count == 1
    assert some_category.product_count == 1


def test_new_product(new_product):
    assert new_product.name == 'test_new_product'
    assert new_product.description == 'test_new_description'
    assert new_product.price == 5000.0
    assert new_product.quantity == 6


def test_add_products(new_product, some_category, some_product):
    print(f"Категория содержит продукты: {some_category.products}")
    print(f"Добавляем продукт: {new_product.name}, количество: {new_product.quantity}")
    some_category.add_product(new_product)
    print(f"После добавления: {some_category.products}")
    assert some_category.category_count == 1
    assert some_category.product_count == 2
    assert some_category.products == ('test_name, 1000.0 руб. Остаток: 5 шт. \n'
                                      'test_new_product, 5000.0 руб. Остаток: 6 шт. \n')
