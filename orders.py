# Orders stuff:
import datetime

from fastapi import FastAPI
from starlette.requests import Request

from helpers import get_order_object, Order

app = FastAPI()


@app.post('/orders', description="http://127.0.0.1:8001/orders")
async def create_order(request: Request):
    order = await request.json()
    order_data = {
        "price": order["price"],
        "product_id": order['pk'],
        "total": order["price"] * 1.2,
        "status": "payed",
        "date": datetime.date.today(),
        "quantity": 1
    }
    order = Order(**order_data)
    order.save()
    return order


@app.get("/orders")
async def get_orders():
    return [get_order_object(pk) for pk in Order.all_pks()]
