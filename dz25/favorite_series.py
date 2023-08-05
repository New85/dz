import Series

class Favorite_series:
    def __init__(self):
        self.__fav_ser = []

    def append_series(self, *series: Series):
        self.__fav_ser.append(series)

