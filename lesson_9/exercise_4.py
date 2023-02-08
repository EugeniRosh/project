"""Модуль расчитывающий длинну марсшрута между координатными точками"""
distance = ((1, 1), (2, 3), (5, 8))


def route_length(coordinates: tuple) -> float:
    total = 0
    for i in range(len(coordinates) - 1):
        total += (
            (coordinates[i + 1][0] - coordinates[i][0]) ** 2 +
            (coordinates[i + 1][1] - coordinates[i][1]) ** 2) ** 0.5
    return total


print(route_length(distance))
