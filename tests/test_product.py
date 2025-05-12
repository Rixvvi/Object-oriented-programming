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
