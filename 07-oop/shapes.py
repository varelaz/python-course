class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        pass

    def get_square(self):
        raise NotImplementedError()

    def get_center(self):
        return self.x, self.y

    def __str__(self):
        return f'Shape with center {self.x} {self.y}'


class Circle(Shape):
    def __init__(self, x, y, r):
        super().__init__(x, y)

        self.r = r

    def get_square(self):
        raise NotImplementedError()

    def __str__(self):
        return f'Circle with center {self.x} {self.y} and radius {self.r}'


class EquilateralTriangle(Shape):
    # Треугольник у которого все стороны равны
    def __init__(self, x, y, a):
        super().__init__(x, y)

        self.a = a
        self.b = b

    def get_square(self):
        raise NotImplementedError()

    def __str__(self):
        return f'EquilateralTriangle with center {self.x} {self.y} and length of all sides {self.a}'


class Rectangle(Shape):
    def __init__(self, x, y, a, b):
        super().__init__(x, y)
        self.a = a
        self.b = b

    def get_square(self):
        raise NotImplementedError()

    def __str__(self):
        return f'Rectangle with center {self.x} {self.y} and length of all side {self.a} and {self.b}'
