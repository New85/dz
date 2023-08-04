# Создать Корзина товаров -> список товаров пользователя
# Для данного задания понадобится класс товар (название, тип(одежда, обувь, украшение), стоимость)
# + реализовать общий список всех товаров
# + список добавленных товаров в корзину
#
#необходимо реализовать возможность подсчета стоимости товаров в корзине -> геттер для cost
from Product import Product
from random import randint as r# r(start,end) === random.randint(start,end)

def append_to_shop_cart():
    #цикл для добавления товаров пользователем
    while True:
        #номер товара опеделяет пользователь
        user_choice = input('would you like the product of number ... ')# дописать условия добавления и т.д. выход из системы
        if user_choice == '0':
            break

        #добавит блок проверки перед добавлением в корзину попапку
        shop_cart.append(list_products[int(user_choice)-1])




def show_shop_cart():
    i = 1
    print('\n ***************shop_cart***************')
    for product in shop_cart:
        print(str(i)+". ", end='')
        product.show()
        i+=1
 #######################################
    sum_card = 0
    for i in shop_cart:
        sum_card += i.cost

    print('сумма ваших покупок составляет ',sum_card)


#список всех товаров в магазине
list_products = [Product('short', 'одежда', 250), Product('boots', 'обувь', 2000), Product('jerry', 'украшение', 10000)]

i = 1
shop_cart = [ ]
for product in list_products:
    print(str(i)+". ", end='')
    product.show()
    i+=1


append_to_shop_cart()




# список добавленных товаров в корзину
show_shop_cart()
