from src.classes import Product, Category, Smartphone, LawnGrass
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


@pytest.fixture
def smartphone():
    test_smartphone = Smartphone('test_name', 'test_description', 10, 10, 90.5, 'test_model', 256, 'test_color')
    return test_smartphone


@pytest.fixture
def law_grass():
    test_law_grass = LawnGrass('test_name', 'test_description', 5, 5, 'test_country', 'test_days', 'test_color')
    return test_law_grass


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
    some_category.add_product(new_product)
    assert some_category.category_count == 1
    assert some_category.product_count == 2
    assert some_category.products == ('test_name, 1000.0 руб. Остаток: 5 шт. \n'
                                      'test_new_product, 5000.0 руб. Остаток: 6 шт. \n')


def test_sum_products():
    product1 = Product('test_name1', '', 5, 2)
    product2 = Product('test_name2', '', 6, 3)
    result = product1 + product2
    assert result == 28


def test_init_smartphone(smartphone):
    assert smartphone.name == 'test_name'
    assert smartphone.description == 'test_description'
    assert smartphone.price == 10
    assert smartphone.quantity == 10
    assert smartphone.efficiency == 90.5
    assert smartphone.model == 'test_model'
    assert smartphone.memory == 256
    assert smartphone.color == 'test_color'


def test_init_law_grass(law_grass):
    assert law_grass.name == 'test_name'
    assert law_grass.description == 'test_description'
    assert law_grass.price == 5
    assert law_grass.quantity == 5
    assert law_grass.country == 'test_country'
    assert law_grass.germination_period == 'test_days'
    assert law_grass.color == 'test_color'
