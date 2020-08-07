from math import *

cities_distances = [('X0', 0.0), ("X1", 100.0),
                    ("X2", 200.0), ("X3", 250.0), ("X4", 300.0)]

friends_list = ["A1", "A2", "A3", "A4", "A5"]

friends_location = [("A1", "X1"), ("A2", "X2"), ("A3", "X3"), ("A4", "X4")]


def get_distance(trip):
    distance = 0

    last_place = cities_distances[0]

    for location in trip:
        new_place = list(
            filter(lambda loc: loc[0] == location, cities_distances))[0]

        b = last_place[1]
        c = new_place[1]

        # from the therorem of pythagore
        a = sqrt(c ** 2 - b ** 2)

        distance = distance + ((a) if a > 0 else 0)

        last_place = new_place

    return distance


# print(get_distance(('X0', 'X1', 'X2', 'X3', 'X4', 'X0')))
print(get_distance(('X0', 'X1', 'X2')))
