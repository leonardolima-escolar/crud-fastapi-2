from app.entities.product import Product
from app.repositories.interfaces.product import ProductRepositoryInterface
from app.use_cases.interfaces.product_create import ProductCreateInterface


class ProductCreate(ProductCreateInterface):
    def __init__(self, product_repository: ProductRepositoryInterface) -> None:
        self.__product_repository = product_repository

    def create(self, product: Product) -> Product:
        response = self.__product_repository.create(product)
        return response
