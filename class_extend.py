# without extending:
class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Circle(Shape):
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def render(self):
        return f"Rendering circle at x:{self.x}, y:{self.y}."

class Rectangle(Shape):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def render(self):
        return f"Rendering rectangle at x:{self.x}, y:{self.y}."

shapes = [
    Circle(30, 40, 15),
    Rectangle(100, 20, 40, 20),
]

for s in shapes:
    print(s.render())

# after extending:
class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Circle(Shape):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def render(self):
        return f"Rendering circle at x:{self.x}, y:{self.y}."

class Rectangle(Shape):
    def __init__(self, x, y, width, height): #-----> override
        super().__init__(x, y) #------> call base class
        self.width = width #------->Extend behaviour
        self.height = height

    def render(self):
        return f"Rendering rectangle at x:{self.x}, y:{self.y}."

shapes = [
    Circle(30, 40, 15),
    Rectangle(100, 20, 40, 20),
]

for s in shapes:
    print(s.render())



class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_year_salary(self):
        return self.salary * 12

class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    def get_year_salary(self):
        return self.salary *12 + self.bonus

e = Employee("Antonio", 2000)
m = Manager("Wolfgang", 2400, 150)
print(e.get_year_salary())
print(m.get_year_salary())