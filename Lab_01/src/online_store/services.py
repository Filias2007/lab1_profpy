from online_store.models import Product


def add_product(
    products: list[Product],
    name: str,
    category: str,
    price: float,
    quantity: int,
) -> Product:
    """Створює новий товар і додає його до списку."""
    product = Product(name=name, category=category, price=price, quantity=quantity)
    products.append(product)
    return product


def calculate_total_inventory_value(products: list[Product]) -> float:
    """Обчислює загальну вартість залишків усіх товарів."""
    return sum(product.total_value for product in products)


def find_product_by_name(products: list[Product], query: str) -> Product | None:
    """Пошук першого товару за точною або частковою назвою (без урахування регістру)."""
    normalized_query = query.strip().lower()
    for product in products:
        if normalized_query in product.name.lower():
            return product
    return None


def filter_by_category(products: list[Product], category: str) -> list[Product]:
    """Фільтрація списку товарів за категорією."""
    normalized_category = category.strip().lower()
    return [
        product
        for product in products
        if product.category.lower() == normalized_category
    ]


def find_most_expensive_product(products: list[Product]) -> Product | None:
    """Визначення найдорожчого товару за одиницю ціни."""
    if not products:
        return None
    return max(products, key=lambda product: product.price)