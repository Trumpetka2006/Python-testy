from pytest import xfail


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __bool__(self):
        if self.x == 0 and self.y == 0:
            return False
        else:
            return True

    def __int__(self):
        return int(self.x**2 + self.y**2)

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        if isinstance(other, int):
            return Vector(self.x * other, self.y * other)
        if isinstance(other, Vector):
            return Vector(self.x * other.x, self.y * other.y)

    def __eq__(self, other) -> bool:
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y
        else:
            return False

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"
