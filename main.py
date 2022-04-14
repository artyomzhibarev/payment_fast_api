from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from models import Product
from helpers import get_product_object

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)


# Products stuff:

@app.get('/products')
async def get_products():
    return [get_product_object(pk=pk) for pk in Product.all_pks()]


@app.get('/products/{pk}')
async def get_product(pk: str):
    return Product.get(pk=pk)


@app.post('/products')
async def create_product(product: Product):
    return product.save()


@app.delete('/products/{pk}')
async def delete_product(pk: str):
    return Product.delete(pk=pk)
