from abc import ABC, abstractmethod

from app.entities.product import Product


class ProductGetInterface(ABC):

    @abstractmethod
    def get(self, product_id: int) -> Product: pass
