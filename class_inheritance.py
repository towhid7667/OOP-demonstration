class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_info(self):
        return f"Employee {self.name}, salary {self.salary}"

class Manager(Employee):
    def get_info(self):
        return f"Manager {self.name}, salary {self.salary}"

employees = [
    Manager("rahim", 2000),
    Employee("kamal", 1800),
    Employee("karim", 1900),
]

# for e in employees:
#     print(e.get_info())


# output:
# Manager rahim, salary 2000
# Employee kamal, salary 1800
# Employee karim, salary 1900


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
#  salary:float)                 |
# |get_info() : str              | 
# --------------------------------
            #    ^
            #    |
            #    |
            #    |
# --------------------------------
# |           Manager            |
# --------------------------------
# --------------------------------
# |                              |
# |                              |
# --------------------------------
# --------------------------------
# |get_info() : str              |
# --------------------------------               

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_info(self):
        return f"Employee {self.name}, salary {self.salary}"

class Manager(Employee):
    def get_info(self):
        return f"Manager {self.name}, salary {self.salary}"

class Programmer(Employee):
    def get_info(self):
        return f"Programmer {self.name}, salary {self.salary}"

employees = [
    Manager("Vera", 2000),
    Programmer("Chuck", 1800),
    Programmer("Dave", 1900),
]

for e in employees:
    print(e.get_info())



# output:
# Manager Vera, salary 2000
# Programmer Chuck, salary 1800
# Programmer Dave, salary 1900