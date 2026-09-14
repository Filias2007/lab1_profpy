import pytest
from online_store.exceptions import InvalidProductDataError
from online_store.models import Product
from online_store.services import (
    add_product,
    calculate_total_inventory_value,
    filter_by_category,
    find_most_expensive_product,
    find_product_by_name,
)


@pytest.fixture
def sample_products() -> list[Product]:
    """Фікстура зі зразковим набором товарів для тестування."""
    return [
        Product(name="Ноутбук", category="Електроніка", price=25000.0, quantity=2),
        Product(name="Мишка", category="Аксесуари", price=500.0, quantity=10),
        Product(name="Клавіатура", category="Аксесуари", price=1500.0, quantity=4),
        Product(name="Монітор", category="Електроніка", price=8000.0, quantity=1),
    ]


def test_product_validation() -> None:
    """Перевірка валідації полів моделі Product."""
    with pytest.raises(InvalidProductDataError):
        Product(name="Товар", category="Категорія", price=-10.0, quantity=5)

    with pytest.raises(InvalidProductDataError):
        Product(name="Товар", category="Категорія", price=100.0, quantity=-2)

    with pytest.raises(InvalidProductDataError):
        Product(name="", category="Категорія", price=100.0, quantity=1)


def test_product_total_value() -> None:
    """Перевірка обчислення вартості одного товару."""
    product = Product(name="Планшет", category="Електроніка", price=12000.0, quantity=3)
    assert product.total_value == 36000.0


def test_add_product(sample_products: list[Product]) -> None:
    """Перевірка додавання товару до списку."""
    initial_count = len(sample_products)
    created = add_product(sample_products, "Навушники", "Аудіо", 2000.0, 5)

    assert len(sample_products) == initial_count + 1
    assert created.name == "Навушники"
    assert created in sample_products


def test_calculate_total_inventory_value(sample_products: list[Product]) -> None:
    """Перевірка підрахунку сумарної вартості всіх залишків."""
    # (25000 * 2) + (500 * 10) + (1500 * 4) + (8000 * 1) = 50000 + 5000 + 6000 + 8000 = 69000
    assert calculate_total_inventory_value(sample_products) == 69000.0
    assert calculate_total_inventory_value([]) == 0.0


def test_find_product_by_name(sample_products: list[Product]) -> None:
    """Перевірка пошуку товару за повною та частковою назвою."""
    found = find_product_by_name(sample_products, "ноут")
    assert found is not None
    assert found.name == "Ноутбук"

    not_found = find_product_by_name(sample_products, "Смартфон")
    assert not_found is None


def test_filter_by_category(sample_products: list[Product]) -> None:
    """Перевірка фільтрації за назвою категорії."""
    accessories = filter_by_category(sample_products, "аксесуари")
    assert len(accessories) == 2
    assert all(item.category == "Аксесуари" for item in accessories)

    empty_result = filter_by_category(sample_products, "Одяг")
    assert len(empty_result) == 0


def test_find_most_expensive_product(sample_products: list[Product]) -> None:
    """Перевірка визначення найдорожчого товару."""
    most_expensive = find_most_expensive_product(sample_products)
    assert most_expensive is not None
    assert most_expensive.name == "Ноутбук"
    assert most_expensive.price == 25000.0

    assert find_most_expensive_product([]) is None