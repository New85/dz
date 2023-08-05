class Series:
    def __init__(self, name: str = '', year: int = 1,
                 cast_list: list = [], director: str = '',
                 genre: str = '', season: int = 1):
        self.__name = name
        self.__year = year
        self.__cast_list = cast_list
        self.__director = director
        self.__genre = genre
        self.__season =season


    def show(self):           # общий список сериалов
        print(self.__name,
              self.__year,
              self.__cast_list,
              self.__director,
              self.__genre,
              self.__season)




