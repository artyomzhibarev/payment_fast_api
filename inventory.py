import os

from fastapi import FastAPI
from redis_om import get_redis_connection

app = FastAPI()

redis_db = get_redis_connection(
    host=os.getenv("REDIS_DB_HOST"),
    port=os.getenv("REDIS_DB_PORT"),
    password=os.getenv("REDIS_DB_PASS")
)

if __name__ == '__main__':
    r = redis_db
    print(r)
    print(*[f'{item}\n' for item in dir(r) if not item.startswith("__")])
    print(os.getenv("REDIS_DB_PASS"))
