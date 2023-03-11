class Vector:
    def __init__(self, point1, point2) -> None:
        self.point1_x = point1[0]
        self.point1_y = point1[1]
        self.point2_x = point2[0]
        self.point2_y = point2[1]

    def lenght(self):
        res = (
            (self.point2_x - self.point1_x) ** 2 +
            (self.point2_y - self.point1_y) ** 2) ** 0.5
        return res

    def __eq__(self, other):
        if not isinstance(other, Vector):
            raise ValueError('The second object must be a class Vector')
        return self.lenght() == other.lenght()

    def __ne__(self, other):
        if not isinstance(other, Vector):
            raise ValueError('The second object must be a class Vector')
        return self.lenght() != other.lenght()

    def __ge__(self, other):
        if not isinstance(other, Vector):
            raise ValueError('The second object must be a class Vector')
        return self.lenght() >= other.lenght()

    def __le__(self, other):
        if not isinstance(other, Vector):
            raise ValueError('The second object must be a class Vector')
        return self.lenght() <= other.lenght()

    def __gt__(self, other):
        if not isinstance(other, Vector):
            raise ValueError('The second object must be a class Vector')
        return self.lenght() > other.lenght()

    def __lt__(self, other):
        if not isinstance(other, Vector):
            raise ValueError('The second object must be a class Vector')
        return self.lenght() < other.lenght()


v1 = Vector((0, 0), (0, 1))
v2 = Vector((1, 1), (1, 2))

print(v1 != v2)
