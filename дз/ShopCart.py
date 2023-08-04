# Создать класс Корзина товаров ->
# список добавленных товаров в корзину
# необходимо реализовать возможность подсчета товаров
from Product import Product


# список доавленных товаров
class ShopCart:
    def __init__(self):
        self.__products = []
        self.__sum = 0

    def show(self):
        print('\n ***************shop_cart***************')
        for product in self.__products:
            product.show()

    def append_product(self, *products: Product):
        if not (type(products) in [Product, tuple]): raise 'products is not Product or tuple'
        for product in products:
            self.__products.append(product)

    def del_product(self, product: Product):
        if not (type(product) == Product): raise 'products is not Product '
        self.__products.remove(product)

    @property
    def cost_products(self):
        for product in self.__products:
            self.__sum += product.cost
        return self.__sum
    #################
    def get_cost(self):
        return self.__cost