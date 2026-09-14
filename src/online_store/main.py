from online_store.exceptions import InvalidProductDataError
from online_store.models import Product
from online_store.services import (
    add_product,
    calculate_total_inventory_value,
    filter_by_category,
    find_most_expensive_product,
    find_product_by_name,
)


def get_demo_products() -> list[Product]:
    return [
        Product(name="Ноутбук Lenovo", category="Електроніка", price=28500.0, quantity=5),
        Product(name="Мишка бездротова", category="Аксесуари", price=750.0, quantity=24),
        Product(name="Монітор Dell 27", category="Електроніка", price=9200.0, quantity=8),
        Product(name="Механічна клавіатура", category="Аксесуари", price=3100.0, quantity=12),
        Product(name="Офісне крісло", category="Меблі", price=6400.0, quantity=3),
    ]


def print_products(products: list[Product]) -> None:
    if not products:
        print("Список порожній.")
        return

    print(f"\n{'Назва':<25}{'Категорія':<16}{'Ціна (грн)':>12}{'К-сть':>8}{'Разом (грн)':>14}")
    print("-" * 75)
    for p in products:
        print(
            f"{p.name:<25}{p.category:<16}{p.price:>12.2f}{p.quantity:>8}{p.total_value:>14.2f}"
        )


def print_menu() -> None:
    print("\n=== Меню керування магазином ===")
    print("1. Показати всі товари")
    print("2. Додати новий товар")
    print("3. Обчислити загальну вартість залишків")
    print("4. Пошук товару за назвою")
    print("5. Фільтрація за категорією")
    print("6. Показати найдорожчий товар")
    print("0. Вихід")


def handle_add_product(products: list[Product]) -> None:
    try:
        name = input("Назва товару: ").strip()
        category = input("Категорія: ").strip()
        price = float(input("Ціна: "))
        quantity = int(input("Кількість на складі: "))
        product = add_product(products, name, category, price, quantity)
        print(f"Товар '{product.name}' успішно додано!")
    except ValueError:
        print("Помилка: ціна та кількість мають бути числовими значеннями.")
    except InvalidProductDataError as err:
        print(f"Помилка валідації: {err}")


def main() -> None:
    products = get_demo_products()

    while True:
        print_menu()
        choice = input("Виберіть дію: ").strip()

        if choice == "1":
            print_products(products)
        elif choice == "2":
            handle_add_product(products)
        elif choice == "3":
            total = calculate_total_inventory_value(products)
            print(f"\nЗагальна вартість усіх товарів на складі: {total:,.2f} грн")
        elif choice == "4":
            query = input("Введіть назву для пошуку: ")
            product = find_product_by_name(products, query)
            if product:
                print(f"Знайдено: {product.name} | {product.category} | {product.price:.2f} грн | {product.quantity} шт.")
            else:
                print("Товар не знайдено.")
        elif choice == "5":
            category = input("Введіть категорію: ")
            filtered = filter_by_category(products, category)
            print_products(filtered)
        elif choice == "6":
            expensive = find_most_expensive_product(products)
            if expensive:
                print(f"\nНайдорожчий товар: {expensive.name} ({expensive.price:.2f} грн)")
            else:
                print("Товари відсутні.")
        elif choice == "0":
            print("Роботу завершено.")
            break
        else:
            print("Невідома команда. Спробуйте ще раз.")


if __name__ == "__main__":
    main()