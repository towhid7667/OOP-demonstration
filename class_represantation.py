class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

products = [
    Product(1, "Headphones", 49.99),
    Product(2, "Monitor speaker", 150.0),
    Product(3, "Soundcard", 78.5),
]

# for p in products:
#     print(p)

# output:
# <__main__.Product object at 0x7f3332221b50>
# <__main__.Product object at 0x7f3332221b90>
# <__main__.Product object at 0x7f3332221bd0>    

# for string represantation we can use str
class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price
    def __str__(self):
        return f"{self.name} ({self.product_id})"
products = [
    Product(1, "Headphones", 49.99),
    Product(2, "Monitor speaker", 150.0),
    Product(3, "Soundcard", 78.5),
]

# for p in products:
#     print(p)


# output:
# Headphones (1)
# Monitor speaker (2)
# Soundcard (3)

# for debugging we can use repr
class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price
    def __repr__(self):
        return f"{self.name} ({self.product_id})"
products = [
    Product(1, "Headphones", 49.99),
    Product(2, "Monitor speaker", 150.0),
    Product(3, "Soundcard", 78.5),
]

# for p in products:
    # print(p)

# for p in products:
    # print(str(p))
    # print(repr(p))    