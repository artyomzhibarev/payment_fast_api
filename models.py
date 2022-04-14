import datetime
from typing import Optional

from redis_om import HashModel

from redis_db import redis_db


class Product(HashModel):
    name: str
    price: float
    quantity: int

    class Meta:
        database = redis_db


class Order(HashModel):
    product_id: str
    price: float
    total: float
    quantity: int
    status: Optional[str]
    date: datetime.date

    class Meta:
        database = redis_db
