class Car:
    def __init__(self, make, model, price):
        self.__make = make
        self.__model = model
        self.__price = price

    def __str__(self):
        return f'{self.__make} {self.__model} {self.__price}'
    def __repr__(self):
        return f'производитель:{self.__make}   модель:{self.__model}  цена:{self.__price} '
    def __eq__(self, other):
        if not isinstance(other, Car):
            raise ValueError('херня какая то')
        return (self.__make == other.__make and
                self.__model == other.__model and
                self.__price == other.__price)
    def __ge__(self, other):
        if not isinstance(other, Car):
            raise ValueError('херня какая то')
        return self.__price >= other.__price
    def __lt__(self, other):
        if not isinstance(other, Car):
            raise ValueError('херня какая то')
        return self.__price < other.__price


car1 = Car('tata', 'tr2', 700)
car2 = Car('mitsubisi', 'sigma', 1000)
car3 = Car('toyota', 'celica', 1700)

print(str(car1))
print(repr(car2))
print(car3 == car2)
print(car1 <= car3)
print(car1 > car3)

# cars = [car1, car2, car3]
# cars.sort()
# print([car.__model for car in cars])


