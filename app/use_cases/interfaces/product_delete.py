from abc import ABC, abstractmethod

from app.entities.product import Product


class ProductDeleteInterface(ABC):

    @abstractmethod
    def delete(self, product_id: int) -> Product: pass
