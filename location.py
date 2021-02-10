from geopy.distance import great_circle




city_coordinates = {'Омск': '54.9924, 73.3686',
                    'Москва':  '55.4507, 37.3656',
                    'Калининград': '54.4223,  20.3039',
                    'Челябинск': '55.154, 61.4291',
                    'Красноярск': '56.0106, 92.5201',
                    'Пермь': '58.0174, 56.2855',
                    'Владивосток': '43.1056, 131.8741',
                    'Михайловка': '50.0647, 43.2284'}


def distance(from_city, to_city):
    if from_city in city_coordinates:
        if to_city in city_coordinates:
            return great_circle(city_coordinates[from_city], city_coordinates[to_city]).km
        else:
            return f'Координат города {to_city} нет в словаре'
    else:
        return f'Координат города {from_city} нет в словаре'



