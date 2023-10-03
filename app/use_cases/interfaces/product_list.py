from abc import ABC, abstractmethod

from app.entities.product import Product


class ProductListInterface(ABC):

    @abstractmethod
    def list(self) -> list[Product]: pass
