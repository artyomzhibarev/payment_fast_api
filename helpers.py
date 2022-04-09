from main import Product


def get_product_object(pk: str):
    product = Product.get(pk=pk)
    return product
