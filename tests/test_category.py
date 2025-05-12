import pytest

from src.category import Category


@pytest.fixture
def category_init():
    return Category("Бытовая техника", "Качественные товары", ["Ноутбук", "Кофемашина"])


def test_category(category_init):
    assert category_init.name == "Бытовая техника"
    assert category_init.description == "Качественные товары"
    assert category_init.products == ["Ноутбук", "Кофемашина"]
