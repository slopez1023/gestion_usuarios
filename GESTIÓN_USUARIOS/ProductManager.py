from Product import Product

class ProductManager:
    def __init__(self):
        self.products = []

    def add_product(self, product: Product):
        self.products.append(product)

    def update_product(self, sku, **kwargs):
        product = next((p for p in self.products if p.sku == sku), None)
        if product is None:
            raise ValueError("Product not found")

        for key, value in kwargs.items():
            if hasattr(product, key):
                setattr(product, key, value)

    def delete_product(self, sku):
        product = next((p for p in self.products if p.sku == sku), None)
        if product is None:
            raise ValueError("Product not found")

        self.products.remove(product)
