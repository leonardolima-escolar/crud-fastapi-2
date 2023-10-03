from abc import ABC, abstractmethod

from app.entities.product import Product


class ProductCreateInterface(ABC):

    @abstractmethod
    def create(self, product: Product) -> Product: pass
