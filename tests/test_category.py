import pytest
from src.product import Product
from src.category import Category


@pytest.fixture
def counting_everything() -> None:
    Category.category_count = 0
    Category.product_count = 0


@pytest.fixture
def category_init(counting_everything):
    product1 = Product("Ноутбук", "Для учебы", 80000.0, 2)
    product2 = Product("Кофемашина", "Для дома", 15000.0, 3)
    return Category("Бытовая техника", "Качественные товары", [product1, product2])


def test_category(category_init) -> None:
    assert category_init.name == "Бытовая техника"
    assert category_init.description == "Качественные товары"
    assert category_init.products == ['Ноутбук, 80000.0 руб. Остаток: 2 шт.',
                                      'Кофемашина, 15000.0 руб. Остаток: 3 шт.']


def test_counting(category_init) -> None:
    assert Category.category_count == 1
    assert Category.product_count == 2


@pytest.fixture
def list_product(counting_everything):
    product1 = Product("Яблоки", "Вкусные и сочные", 120.0, 21)
    product2 = Product("Бананы", "Спелые и питательные", 170.0, 10)
    product3 = Product("Апельсины", "Крупные и сладкие", 99.0, 14)
    return Category("Фрукты",
                    "Привезены из лучших стран-производителей",
                    [product1, product2, product3])


def test_add_product(list_product):
    product4 = Product("Груши", "Большие и мягкие", 200.0, 6)

    list_product.add_product(product4)

    assert Category.product_count == 4


def test_products(list_product):
    result = list_product.products
    my_data = ['Яблоки, 120.0 руб. Остаток: 21 шт.',
               'Бананы, 170.0 руб. Остаток: 10 шт.',
               'Апельсины, 99.0 руб. Остаток: 14 шт.']

    assert result == my_data


@pytest.fixture
def category():
    return Category("Электроника", "Гаджеты", [])


def test_isinstance(category):
    with pytest.raises(TypeError):
        category.add_product("Не продукт")


def test_str_category(list_product):
    assert str(list_product) == 'Фрукты, количество продуктов: 45 шт.'
