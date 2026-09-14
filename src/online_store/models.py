from dataclasses import dataclass
from online_store.exceptions import InvalidProductDataError


@dataclass
class Product:
    name: str
    category: str
    price: float
    quantity: int

    def __post_init__(self) -> None:
        if self.price < 0:
            raise InvalidProductDataError("Ціна не може бути від'ємною.")
        if self.quantity < 0:
            raise InvalidProductDataError("Кількість не може бути від'ємною.")
        if not self.name.strip():
            raise InvalidProductDataError("Назва товару не може бути порожньою.")
        if not self.category.strip():
            raise InvalidProductDataError("Категорія не може бути порожньою.")

    @property
    def total_value(self) -> float:
        """Повертає повну вартість залишків конкретного товару."""
        return self.price * self.quantity