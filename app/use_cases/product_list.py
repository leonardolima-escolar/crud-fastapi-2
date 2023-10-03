from app.entities.product import Product
from app.repositories.interfaces.product import ProductRepositoryInterface
from app.use_cases.interfaces.product_list import ProductListInterface


class ProductList(ProductListInterface):
    def __init__(self, product_repository: ProductRepositoryInterface) -> None:
        self.__product_repository = product_repository

    def list(self) -> list[Product]:
        response = self.__product_repository.list()
        return response
