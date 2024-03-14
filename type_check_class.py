class Employee:
    def __init__(self, first_name: str, last_name: str, salary: float) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def get_full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def raise_salary(self, percentage: float) -> None:
        self.salary = self.salary * (100 + percentage) / 100

e = Employee("Vera", "Schimdt", 2000)
# print(e.get_full_name())
# e.raise_salary(10)
# print(e.salary)



# if we want to annotate self parameter:
from typing import Self

class Employee:
    def __init__(self: Self, first_name: str, last_name: str, salary: float) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def get_full_name(self: Self) -> str:
        return f"{self.first_name} {self.last_name}"

    def raise_salary(self: Self, percentage: float) -> None:
        self.salary = self.salary * (100 + percentage) / 100

e = Employee("Vera", "Schimdt", 2000)
# print(e.get_full_name())
# e.raise_salary(10)
# print(e.salary)



# -----------------wrong----------------------
numbers = [1, 4, 9, 2, 5, None, 2]

for n in numbers:
    print(n * 2)

# ERORR:
# Traceback (most recent call last):
#   File "/media/towhid/Files/OOP-Demonstration/type_check_class.py", line 46, in <module>
#     print(n * 2)
#           ~~^~~
# TypeError: unsupported operand type(s) for *: 'NoneType' and 'int'    

# -----------------fixed----------------------
from typing import List

numbers: List[int] = [1, 4, 9, 2, 5, None, 2]

for n in numbers:
    print(n * 2) #now showing correct error

