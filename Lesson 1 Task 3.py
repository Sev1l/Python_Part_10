## Class Hierarchies
# Task 3 (Areas)



class Rectangle:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def area(self):
        return self.first * self.second

    def __str__(self):
        return f'rectangle {self.first}x{self.second}'


class Square(Rectangle):
    def __init__(self, first):
        super().__init__(first, first)

    def __str__(self):
        return f'square {self.first}x{self.second}'


rectangle = Rectangle(2, 3)
print(rectangle)
print("area:", rectangle.area())

square = Square(4)
print(square)
print("area:", square.area())
