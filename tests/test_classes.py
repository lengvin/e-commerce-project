from src.classes import Product, Category
import pytest


@pytest.fixture
def some_product():
    product = Product("test_name",
                      "test_description",
                      1000.0,
                      5)
    return product


@pytest.fixture
def some_category(some_product):
    category = Category("test_mame",
                        "test_description",
                        [some_product])
    return category


def test_init_product(some_product):
    assert some_product.name == "test_name"
    assert some_product.description == "test_description"
    assert some_product.price == 1000.0
    assert some_product.quantity == 5


def test_init_category(some_category, some_product):
    assert some_category.name == "test_mame"
    assert some_category.description == "test_description"
    assert some_category.products == [some_product]
    assert some_category.category_count == 1
    assert some_category.product_count == 1
