from src.product import Product


class Category:
    category_count = 0
    product_count = 0

    name: str
    description: str
    products: list

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.product_count += len(products)

    def add_product(self, product):
        if not isinstance(product, Product):
            raise TypeError("Можно добавить только объекты класса Product или его наследников")
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        result = []
        for product in self.__products:
            result.append(f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.")
        return result

    def __str__(self):
        result = 0
        for product in self.__products:
            result += product.quantity
        return f'{self.name}, количество продуктов: {result} шт.'

    def middle_price(self):
        counter = 0
        try:
            for product in self.__products:
                counter += product.price
            result = counter / len(self.__products)
            return result
        except ZeroDivisionError:
            return 0
