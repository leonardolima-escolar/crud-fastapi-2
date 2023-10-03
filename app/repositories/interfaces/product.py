from abc import ABC, abstractmethod

from app.entities.product import Product


class ProductRepositoryInterface(ABC):

    @abstractmethod
    def list(self) -> list[Product]: pass

    @abstractmethod
    def get(self, product_id: int) -> Product | None: pass

    @abstractmethod
    def create(self, product: Product) -> Product | None: pass

    @abstractmethod
    def update(self, product_id: int,
               updated_product: Product) -> Product | None: pass

    @abstractmethod
    def delete(self, product_id: int) -> Product | None: pass
