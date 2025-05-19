from abc import ABC, abstractmethod

import pytest

from src.product import Product, Smartphone, LawnGrass, BaseProduct


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


def test_type():
    product1 = Product("Яблоки", "Вкусные и сочные", 120.0, 21)
    product2 = Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")
    with pytest.raises(TypeError):
        product1 + product2


def test_added_new_class():
    smartphone1 = Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5,
                             "S23 Ultra", 256, "Серый")
    assert smartphone1.name == "Samsung Galaxy S23 Ultra"
    assert smartphone1.description == "256GB, Серый цвет, 200MP камера"
    assert smartphone1.price == 180000.0
    assert smartphone1.quantity == 5
    assert smartphone1.efficiency == 95.5
    assert smartphone1.model == "S23 Ultra"
    assert smartphone1.memory == 256
    assert smartphone1.color == "Серый"


def test_added_class():
    grass1 = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
    assert grass1.name == "Газонная трава"
    assert grass1.description == "Элитная трава для газона"
    assert grass1.price == 500.0
    assert grass1.quantity == 20
    assert grass1.country == "Россия"
    assert grass1.germination_period == "7 дней"
    assert grass1.color == "Зеленый"


def test_base_instantiated():
    with pytest.raises(TypeError):
        BaseProduct("Перец", "Болгарский", 100.0, 6)


def test_mixin(capsys):
    Product("Трактор", "Новый красный трактор с прицепом", 2300000.0, 1)
    captured = capsys.readouterr()
    assert "Product('Трактор', 'Новый красный трактор с прицепом', 2300000.0, 1)\n" == captured.out
