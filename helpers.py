from models import Product, Order


def get_product_object(pk: str):
    product = Product.get(pk=pk)
    return product


def get_order_object(pk: str):
    order = Order.get(pk=pk)
    return order
