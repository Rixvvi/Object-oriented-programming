import pytest

from src.category import Category


@pytest.fixture
def counting_everything() -> None:
    Category.category_count = 0
    Category.product_count = 0


@pytest.fixture
def category_init(counting_everything):
    return Category("Бытовая техника", "Качественные товары", ["Ноутбук", "Кофемашина"])


def test_category(category_init) -> None:
    assert category_init.name == "Бытовая техника"
    assert category_init.description == "Качественные товары"
    assert category_init.products == ["Ноутбук", "Кофемашина"]


def test_counting(category_init) -> None:
    assert Category.category_count == 1
    assert Category.product_count == 2
