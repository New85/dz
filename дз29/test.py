class Student:
    def __init__(self, firstName: str, lastName: str, group: str, double_averageMark: int = 0):
        self.__firstName = firstName
        self.__lastName = lastName
        self.__group = group
        self.__double_averageMark = double_averageMark  # средний бал
        self.__scholarship = 0  # степендия

    def getScholarship(self, double_averageMark):
        self.__double_averageMark = double_averageMark
        if self.__double_averageMark == 5:
            self.__scholarship = 2000
        elif self.__double_averageMark == (4 or 3 or 2 or 1):
            self.__scholarship = 1900
        else:
            print('Не верно установленная средняя оценка')

    def show(self):
        print('Имя студента :', self.__firstName, ',', 'Фамилия :', self.__lastName, ',',
              'руппа :', self.__group, ',', 'Степендия составляет: ', self.__scholarship, 'руб')

    def get_averageMark(self):
        return self.__double_averageMark


class Aspirant():
    def __init__(self, firstName: str, lastName: str, group: str, double_averageMark: int = 0):
        self.__firstName = firstName
        self.__lastName = lastName
        self.__group = group
        self.__double_averageMark = double_averageMark
        self.__scholarship = 0  # степендия


    def show(self):
        print('Имя студента :', self.__firstName, ',', 'Фамилия :', self.__lastName, ',',
              'руппа :', self.__group, ',', 'Степендия составляет: ', self.__scholarship, 'руб')

    def get_averageMark(self):
        return self.__double_averageMark


    def getScholarship(self, double_averageMark):
        self.__double_averageMark = double_averageMark
        if self.__double_averageMark == 5:
            self.__scholarship = 2000
        elif self.__double_averageMark == (4 or 3 or 2 or 1):
            self.__scholarship = 1900
        else:
            print('Не верно установленная средняя оценка')


a = Aspirant('Иванов', 'Иван', 'Е124', 3)
b = Student('Олег', 'Олегов', 'У74', 4)
c = Student('Федор', 'Федоров', 'З445', 2)
d = Aspirant('Артем', 'Артемов', 'Г21', 3)
list_ = [a, b, c, d]

# def showIN():
#     for i in list_:
#         if type(i) == Aspirant:
#             if 0 > i.self.__double_averageMark > 5:
#                 print(i, 'Степендия 2200')
#             elif 6 > i.self.__double_averageMark > 4:
#                 print(i, 'Степендия 2500')
#             else:
#                 print('Не верная средняя оценка')
#         if type(i) == Student:
#             if 0 > i.self.__double_averageMark > 5:
#                 print(i, 'Степендия 1900')
#             elif 6 > i.self.__double_averageMark > 4:
#                 print(i, 'Степендия 2000')
#             else:
#                 print('Не верная средняя оценка')

b.getScholarship()
b.show()

