from series import Series
from favorite_series import Favorite_series
from season import Season
import random

series_ = []
list_series = ['ser1', 'ser2', 'ser3', 'ser4', 'ser5', 'ser6']
name_series = ['Злые суслики', 'Леголайз', 'Молод и красив',
               'Вечный', 'Старый дом', 'Большой Лебовски']
cast_list = ['Дензел Вашингтон', 'Изабель Юппер', 'Дэниел Дей-Льюис', 'Киану Ривз',
             'Роб Морган',
              'Николь Кидман', 'Сон Кан-хо', 'Тони Сервилло', 'Чжао Тао', 'Виола Дэвис',
             'Сирша Ронан', 'Джулианна Мур', 'Хоакин Феникс', 'Тильда Суинтон', 'Оскар Айзек',
             'Майкл Б. Джордан', 'Ким Мин Хи', 'Элфри Вудард', 'Уиллем Дефо', 'Уэс Стьюди']
director = ['Клинт Иствуд', 'Пон Чжун Хо', 'Питер Джексон', 'Асгар Фархади', 'Дени Вильнёв',
            'Мартин Скорсезе', 'Квентин Тарантино', 'Кристофер Нолан',
            'Алехандро Гонсалес Иньярриту', 'Уэс Андерсон']
genre = ['Комедии', 'Ужасы', 'Фантастика', 'Триллеры', 'Боевики', 'Мелодрамы', 'Детективы']

def rand(): # рандом актеров
    cast = []
    a = random.randint(2, 5)
    for i in range(a):
        cast.append(random.choice(cast_list))

    return cast

for i in range(6):    #  создание списка сериалов
    film = Series(name_series[random.randint(0, 5)],
                  random.randint(2000, 2023),
                  rand(),
                  random.choice(director),
                  random.choice(genre),
                  random.randint(1, 4))

    series_.append(film)

for i in series_:                    #  просмотр списка сериалов
    i.show()

