from abc import ABC
from abc import abstractmethod

class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @abstractmethod
    def render(self):
        pass

class Circle(Shape):
    def render(self):
        return f"Rendering circle at x:{self.x}, y:{self.y}."

class Rectangle(Shape):
    def render(self):
        return f"Rendering rectangle at x:{self.x}, y:{self.y}."

shapes = [
    Circle(30, 40),
    Rectangle(100, 20),
    Shape(50, 50),
]

for s in shapes:
    print(s.render())


# error before using abstract:
# Traceback (most recent call last):
#   File "/media/towhid/Files/OOP-Demonstration/abstract_base_class.py", line 28, in <module>
#     print(s.render())
#           ^^^^^^^^
# AttributeError: 'Shape' object has no attribute 'render'

# # after using abstract:
# Rendering circle at x:30, y:40.
# Rendering rectangle at x:100, y:20.
# None



from abc import ABC
from abc import abstractmethod

class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @abstractmethod
    def render(self):
        pass

class Circle(Shape):
    def render(self):
        return f"Rendering circle at x:{self.x}, y:{self.y}."

class Rectangle(Shape):
    def render(self):
        return f"Rendering rectangle at x:{self.x}, y:{self.y}."

class Ellipse(Shape):
    def render(self):
        pass

shapes = [
    Circle(30, 40),
    Rectangle(100, 20),
    Ellipse(100, 20),
]

for s in shapes:
    print(s.render())