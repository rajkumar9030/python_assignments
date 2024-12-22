class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length ** 2

shape = Shape()
square = Square(4)

print("Area of shape:", shape.area())
print("Area of square:", square.area())