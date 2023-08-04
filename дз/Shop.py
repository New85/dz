# через класс магазин
# Создать класс Корзина товаров ->
# Для данного задания понадобится класс товар (название, тип(одежда, обувь, украшение), стоимость)
# реализовать общий список всех товаров
# список добавленных товаров в корзину
# необходимо реализовать возможность подсчета товаров
from Product import Product


# общий список товаров
# добавление товара в магазин
# удаление товара из магазина
class Shop:
    def __init__(self, name: str = '', *products: Product):
        if not (type(name) == str): raise 'name is not str'
        if not (type(products) in [Product, tuple]): raise 'products is not Product or tuple'

        self.__name = name
        self.__products = []
        for product in products:
            self.__products.append(product)

    def show(self):
        print(self.__name, ' : ')
        for product in self.__products:
            product.show()

    # def get_product(self, i):
    #     return self.__products[i]

    @property
    def products(self):
        return self.__products

    def append_product(self, *products: Product):
        if not (type(products) in [Product, tuple]): raise 'products is not Product or tuple'
        for product in products:
            self.__products.append(product)

    def del_product(self, product: Product):
        if not (type(product) == Product): raise 'products is not Product '
        self.__products.remove(product)


shop = Shop('SHOP_2_0', Product('short', 'одежда', 250), Product('boots', 'обувь', 2000),
            Product('jerry', 'украшение', 10000))
shop.show()
# Shop() # == __new__()