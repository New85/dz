class Poison:
    def __init__(self, name: str, price: int, item = []):
        self.name = name
        self.price = price
        self.item = item
        self.view = 0


    def examination(self):
        if self.item == ['подорожник2_0', 'подорожник2_0', 'подорожник2_0']:
            self.view = 1 #  "Целебный отвар"
            print("Данное зелье является целебным отваром")
        elif self.item == ['ХПетрушкаХ ', 'подорожник2_0', 'подорожник2_0']:
            self.view = 2 #  "Приятель"
            print("Это зелье 'Приятель'")
        elif self.item == ['Черемух', 'Черемух', 'Черемух', 'ХПетрушкаХ ', 'ХПетрушкаХ ', 'подорожник2_0']:
            self.view = 3 #  "Прилив сил"
            print("Это зелье 'Прилив сил'")
        else:
            print('Зелье не получилось')


    def show(self):
        print(self.name, self.price, self.view)


#c = Poison("rok", 200, ['подорожник2_0', 'подорожник2_0', 'подорожник2_0'])

#c.show()
#c.examination()
#c.show()

