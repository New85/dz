# Для данного задания понадобится класс товар (название, тип(одежда, обувь, украшение), стоимость)
class Product:
    def __init__(self, name: str = 't-short', type_p: str = 'clothes', cost: int = 100):
        if not (type_p in ['одежда', 'обувь',
                           'украшение']): raise 'type is not одежда, обувь, украшение'  # type_p == 'одежда' or type_p == 'обувь'
        if cost < 0: raise 'cost is below zero'  # raise вызываем ошибку
        if not (type(cost) in [int, float]): raise 'cost is not int or float'

        self.__name = name
        self.__type = type_p
        self.__cost = cost

    def show(self):
        print(self.__name,
              self.__type,
              self.__cost)

    @property
    def cost(self):
        return self.__cost