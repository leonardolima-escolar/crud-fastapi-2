from app.entities.product import Product
from app.repositories.interfaces.product import ProductRepositoryInterface
from app.use_cases.interfaces.product_delete import ProductDeleteInterface


class ProductDelete(ProductDeleteInterface):
    def __init__(self, product_repository: ProductRepositoryInterface) -> None:
        self.__product_repository = product_repository

    def delete(self, product_id: int) -> Product:
        response = self.__product_repository.delete(product_id)
        return response
