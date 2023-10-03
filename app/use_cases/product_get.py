from app.entities.product import Product
from app.repositories.interfaces.product import ProductRepositoryInterface
from app.use_cases.interfaces.product_get import ProductGetInterface


class ProductGet(ProductGetInterface):
    def __init__(self, product_repository: ProductRepositoryInterface) -> None:
        self.__product_repository = product_repository

    def get(self, product_id: int) -> Product:
        response = self.__product_repository.get(product_id)
        return response
