from app.entities.product import Product
from app.repositories.interfaces.product import ProductRepositoryInterface
from app.use_cases.interfaces.product_update import ProductUpdateInterface


class ProductUpdate(ProductUpdateInterface):
    def __init__(self, product_repository: ProductRepositoryInterface) -> None:
        self.__product_repository = product_repository

    def update(self, product_id: int,
               updated_product: Product) -> Product:
        response = self.__product_repository.update(
            product_id, updated_product)
        return response
