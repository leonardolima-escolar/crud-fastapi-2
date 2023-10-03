from fastapi import FastAPI
from app.middlewares.audit_log_transaction import audit_log_transaction
from app.routers import product

app = FastAPI()

app.include_router(product.router)

app.middleware("http")(audit_log_transaction)
