import asyncio
from datetime import datetime
from fastapi import APIRouter, BackgroundTasks, Depends, HTTPException, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from app.entities.product import Product
from app.repositories.product import ProductRepository
from app.use_cases.product_create import ProductCreate
from app.use_cases.product_delete import ProductDelete
from app.use_cases.product_get import ProductGet
from app.use_cases.product_list import ProductList
from app.use_cases.product_update import ProductUpdate


router = APIRouter(prefix="/products")


def get_product_repository() -> ProductRepository:
    return ProductRepository()


async def create_product_log(product: Product):
    await asyncio.sleep(5)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_message = f"""{timestamp} - ID: {product.id}
                      Name: {product.name}
                      Price: {product.price}
                      Quantity: {product.quantity}
                  """

    with open("create_product.log", "a", encoding="utf-8") as log_file:
        log_file.write(log_message + "\n")


@router.get("/")
async def list_products(repository: ProductRepository = Depends(get_product_repository)):
    use_case = ProductList(repository)
    products = use_case.list()
    await asyncio.sleep(10)
    return JSONResponse(content=jsonable_encoder(products))


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_product(product: Product, background_tasks: BackgroundTasks,
                   repository: ProductRepository = Depends(get_product_repository)):
    use_case = ProductCreate(repository)
    product = use_case.create(product)
    background_tasks.add_task(create_product_log, product)
    if product:
        return JSONResponse(content=jsonable_encoder(product))
    raise HTTPException(status_code=400, detail="Product already exists.")


@router.get("/{product_id}")
def read_product(product_id: int, repository: ProductRepository = Depends(get_product_repository)):
    use_case = ProductGet(repository)
    product = use_case.get(product_id)
    if product:
        return JSONResponse(content=jsonable_encoder(product))
    raise HTTPException(status_code=404, detail="Product not found")


@router.put("/{product_id}")
def update_product(product_id: int, updated_product: Product,
                   repository: ProductRepository = Depends(get_product_repository)):
    use_case = ProductUpdate(repository)
    product = use_case.update(product_id, updated_product)
    if product:
        return JSONResponse(content=jsonable_encoder(updated_product))
    raise HTTPException(status_code=404, detail="Product not found")


@router.delete("/{product_id}")
def delete_product(product_id: int,
                   repository: ProductRepository = Depends(get_product_repository)):
    use_case = ProductDelete(repository)
    product = use_case.delete(product_id)
    if product:
        return JSONResponse(content=jsonable_encoder(product))
    raise HTTPException(status_code=404, detail="Product not found")
