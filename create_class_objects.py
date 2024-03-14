class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

e1 = Employee("labib", 2000)
e2 = Employee("shohag", 1800)
e3 = Employee("keila", 1900)

print(e1)
print(e2)
print(e3)

# output:(printed object name, and it's storage reference)
# <__main__.Employee object at 0x745335621b50>
# <__main__.Employee object at 0x745335621b90>
# <__main__.Employee object at 0x745335621bd0>

print(e1.name, e1.salary)
print(e2.name, e2.salary)
print(e3.name, e3.salary)


# output:(printed attributes value)
# labib 2000
# shohag 1800
# keila 1900


# UML:
# --------------------------------
# |           Employee           |
# --------------------------------
# --------------------------------
# |salary : float                |
# |name : str                    |
# --------------------------------
# --------------------------------
# |Employee(name:str,            | 
# salary:float)                  |
# --------------------------------

