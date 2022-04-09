import os

from redis_om import get_redis_connection

redis_db = get_redis_connection(
    host=os.getenv("REDIS_DB_HOST"),
    port=os.getenv("REDIS_DB_PORT"),
    password=os.getenv("REDIS_DB_PASS")
)
