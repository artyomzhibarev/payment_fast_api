from redis_om import HashModel

from redis_db import redis_db


class Product(HashModel):
    name: str
    price: float
    quantity: int

    class Meta:
        database = redis_db
