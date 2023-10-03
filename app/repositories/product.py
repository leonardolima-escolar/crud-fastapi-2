from app.entities.product import Product
from app.repositories.interfaces.product import ProductRepositoryInterface


products = {}


class ProductRepository(ProductRepositoryInterface):

    @classmethod
    def list(cls) -> list[Product]:
        return products

    @classmethod
    def get(cls, product_id: int) -> Product | None:
        product = products.get(product_id)
        if product:
            return product
        return None

    @classmethod
    def create(cls, product: Product) -> Product | None:
        if not products.get(product.id):
            products[product.id] = product
            return product
        return None

    @classmethod
    def update(cls, product_id: int,
               updated_product: Product) -> Product | None:
        product = products.get(product_id)
        if product:
            products[product.id] = updated_product
            return updated_product
        return None

    @classmethod
    def delete(cls, product_id: int) -> Product | None:
        product = products.get(product_id)
        if product:
            return products.pop(product_id)
        return None
