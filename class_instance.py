class Circle:
    def render(self):
        return "Circle geometry"

class Rectangle:
    pass

shapes = [Circle(), Rectangle()]

# for s in shapes:
#     print(s.render())

#it show shows erro, s,render() missing
# Polymorphism is everywhere in python

objects = [19, "Hardcastle"]

for o in objects:
    print(o)



#how print method works:
# def print(o):
#     if o is an int:
#         o.number
#     elif o is a string:
#         o,text    
nums = [0 , 1 , 2, 3]
print(dir(nums))
# here an instance is created where it has __str__, __len__

# ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

class A:
    pass

a = A()
print(len(a))

#instance created without __len__
# Traceback (most recent call last):
#   File "/media/towhid/Files/OOP-Demonstration/class_instance.py", line 39, in <module>
#     print(len(a))
#           ^^^^^^
# TypeError: object of type 'A' has no len()


