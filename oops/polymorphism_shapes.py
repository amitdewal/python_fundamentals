class Shape:
    def area(self):
        print("Area method not implemented")


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        print("Area of Rectangle: ", self.width * self.height)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print("Area of Circle: ", 3.14 * self.radius * self.radius)


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        print("Area of Square: ", self.side * self.side)


rect = Rectangle(10,20)
circ = Circle(7)
square = Square(8)

shapes = [rect, circ, square]
for shape in shapes:
    shape.area() # method calling


