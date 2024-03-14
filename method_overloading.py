class Calculator:
    def add(self, x=0, y=0, z=0):
        if z == 0:
            return x + y
        else:
            return x + y + z

# # Using the add method with different parameter combinations
calc = Calculator()
print(calc.add(2, 3))     # Output: 5
print(calc.add(2, 3, 4))  # Output: 9



class Shape:
    def area(self, x):
        return x * x

    def area(self, x, y):
        return x * y

# # Trying to call the area method with different argument types
shape = Shape()
print(shape.area(5))      # Output: 25 (calls area(self, x))
print(shape.area(5, 6))   # Output: 30 (calls area(self, x, y))





class Device:
    def set_address(self, address):
        self.address = address

    def set_address(self, ip, port):
        self.address = ip + ":" + port

device = Device()
device.set_address("127.0.0.1:8000")
print(device.address)

# ERROR:
# Traceback (most recent call last):
#   File "/media/towhid/Files/OOP-Demonstration/method_overloading.py", line 39, in <module>
#     device.set_address("127.0.0.1:8000")
# TypeError: Device.set_address() missing 1 required positional argument: 'port'


class Device:
    def set_address(self, address, port=None):
        if port is None:
            self.address = address
        else:
            self.address = address + ":" + port


device = Device()
device.set_address("127.0.0.1", port="8000")
print(device.address)



# 0r----

class Device:
    def set_address(self, address):
        self.address = address

    def set_address_from_ip_and_port(self, ip, port):
        self.address = ip + ":" + port


device = Device()
device.set_address("127.0.0.1", port="8000")
print(device.address)