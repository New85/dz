class Tower:
    def __init__(self,name: str, armor: int, health: int):
        self.__name = name
        self.__armor = armor
        self.__health = health

    def __repr__(self):
        return self.__name

    # def damage(self):
    #     return self.__health - 10

    @property
    def armor(self):
        return self.__armor

    @property
    def health(self):
        return self.__health
    @property
    def __sub__(self, other): # уменьшение здоровья и брони башни
        self.__armor -= other
        # if self.__armor >= 0:
        #     self.__armor - other
        #     return self.__armor
        # else:
        #     self.__health - other
        #     return self.__health

    def show(self):
        print(f'Башня { self.__name}, броня башни составляет {self.__armor},  здоровье башни  {self.__health}')




class Shooter(Tower):               # башня принимает дополнительный параметр стрельба
    def __init__(self,name: str, armor: int, health: int, shoot: int):
        self.__name = name
        self.__armor = armor
        self.__health = health
        self.__shoot = shoot

    # @property
    # def show(self):
    #     print(f'Башня { self.__name}, броня башни составляет {self.__armor},  здоровье башни  {self.__health}, урон башни {self.__shoot}')

defender = Tower('Жук', 100, 100)
strelok = Shooter('Бабуин',100, 100, 10)

#strelok.show
print(defender)

# strelok - 10
strelok.show

