class Employee:
    def __init__(self, first_name,middle_name, last_name, salary):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.salary = salary
    def get_full_name(self):
        return f'Employee Name is {self.first_name} {self.middle_name} {self.last_name}'   
    
    def raise_salary(self, percentage):
        print("kk", self.salary)
        per_value = int(percentage.strip('%'))
        self.salary = self.salary + (self.salary * (per_value/100))    
    def add_bonus(self, amount):
        self.salary = self.salary + amount    
e1 = Employee('Shah', 'Ali', 'Kamal', 12000)        
e2 = Employee('Jamal', 'Ali', 'Rahim', 18000)    
e1.raise_salary('15%')  
e2.add_bonus(2000)  

print(e1.get_full_name())
print(e1.salary)
print(e2.salary)


# output:
# kk 12000
# Employee Name is Shah Ali Kamal
# 13800.0
# 20000

# UML:
# --------------------------------
# |           Employee           |
# --------------------------------
# --------------------------------
# |salary : float                |
# |first_name : str              |
# |last_name : str               |
# |middle_name : str             |
# --------------------------------
# --------------------------------
# |Employee(name:str,            | 
# get_full_name(): str           |
# raise_salary(percentage        |
# : float) : None                |
# --------------------------------