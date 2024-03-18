from abc import ABC
from abc import abstractmethod


# #the abstarct method dosen't check type, which shows no wrror, after providing none
# class Shape(ABC):
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     @abstractmethod
#     def render(self):
#         pass

# class Circle(Shape):
#     pass

# c = Circle(1, 2)


# #let's fix it with type abstract method:
# class Shape(ABC):
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     @abstractmethod
#     def render(self) -> str:
#         pass

# class Circle(Shape):
#     def render(self) -> str:
#         return f"Circle at x:{self.x}, y:{self.y}"

# c = Circle(1, 2)



# we can override the method , let's try overriding the type too
class Shape(ABC):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @abstractmethod
    def render(self) -> str:
        pass

class Circle(Shape):
    def render(self) -> int:
        return 0

c = Circle(1, 2)
print(c.render())

#it prints 0, but according to mypy it is an error, bcz the return type of abstact method is str


#fixed it

class Shape(ABC):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @abstractmethod
    def render(self) -> str:
        pass

class Circle(Shape):
    def render(self) -> str:
        return f"Circle at x:{self.x}, y:{self.y}"

c = Circle(1, 2)
print(c.render())



#@absract_base_class file I allowed NONe, when I was learning abstract class , but Now I know I should stop it to happen

class Shape(ABC):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @abstractmethod
    def render(self) -> str:
        pass

class Circle(Shape):
    def render(self) -> str:
        return f"Rendering circle at x:{self.x}, y:{self.y}"

class Rectangle(Shape):
    def render(self) -> str:
        return f"Rendering circle at x:{self.x}, y:{self.y}"

class Ellipse(Shape):
    def render(self):
        pass

shapes =[
    Circle(30, 40),
    Rectangle(100, 20),
    Ellipse(100, 20),
]

for s in shapes:
    print(s.render())


# fixed it

class Shape(ABC):
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    @abstractmethod
    def render(self) -> str:
        pass

class Circle(Shape):
    def render(self) -> str:
        return f"Rendering circle at x:{self.x}, y:{self.y}"

class Rectangle(Shape):
    def render(self) -> str:
        return f"Rendering circle at x:{self.x}, y:{self.y}"

class Ellipse(Shape):
    def render(self):
        pass

shapes =[
    Circle(30, 40),
    Rectangle(100, 20),
    Ellipse(100, 20),
]

for s in shapes:
    print(s.render())

# =====================================================44
class Shape(ABC):
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    @abstractmethod
    def render(self) -> str:
        pass

class Circle(Shape):
    def render(self) -> str:
        return f"Rendering circle at x:{self.x}, y:{self.y}"

class Rectangle(Shape):
    def render(self) -> str:
        return f"Rendering circle at x:{self.x}, y:{self.y}"

class Ellipse(Shape):
    def render(self):
        return f"Rendering ellipse at x:{self.x}, y:{self.y}"

shapes =[
    Circle(30, 40),
    Rectangle(100, 20),
    Ellipse(100, 20),
]

for s in shapes:
    print(s.render())

