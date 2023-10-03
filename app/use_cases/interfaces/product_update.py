from abc import ABC, abstractmethod

from app.entities.product import Product


class ProductUpdateInterface(ABC):

    @abstractmethod
    def update(self, product_id: int,
               updated_product: Product) -> Product: pass
