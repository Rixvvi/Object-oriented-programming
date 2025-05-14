import pytest

from src.product import Product


@pytest.fixture
def product_init():
    return Product("Машина", "Черная матовая", 1800000.0, 1)


def test_product(product_init) -> None:
    assert product_init.name == "Машина"
    assert product_init.description == "Черная матовая"
    assert product_init.price == 1800000.0
    assert product_init.quantity == 1


def test_new_product():
    new_product = Product.new_product(
        {"name": "Iphone 15 pro max",
         "description": "Новейшая модель с объемным функционалом",
         "price": 112000.0,
         "quantity": 3})
    assert new_product.name == "Iphone 15 pro max"
    assert new_product.description == "Новейшая модель с объемным функционалом"
    assert new_product.price == 112000.0
    assert new_product.quantity == 3


def test_price():
    product = Product("Яблоки", "Вкусные и сочные", 120.0, 21)
    product.price = 200.0
    assert product.price == 200.0


def test_price_zero():
    product = Product("Яблоки", "Вкусные и сочные", 120.0, 21)
    product.price = 0
    assert product.price == 120.0


def test_str_product():
    first_product = Product("Мотоцикл", "Алый глянцевый", 300000.0, 3)
    assert str(first_product) == 'Мотоцикл, 300000.0 руб. Остаток: 3 шт.'


def test_add_product():
    first = Product("Медведь", "Бурый трусливый", 1000000.0, 2)
    second = Product("Мышь", "Крупная, серого цвета", 600.0, 8)

    result = first + second
    assert result == 2004800.0
