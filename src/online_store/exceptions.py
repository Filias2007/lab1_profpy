class StoreError(Exception):
    """Base exception for store operations."""


class InvalidProductDataError(StoreError):
    """Raised when product attributes fail validation."""