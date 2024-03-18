from typing import Protocol
from abc import AB
from abc import abstractmethod

class Shape(Protocol):
    def area(self) -> float: ...

class Circle:
    def area(self) -> float:
        return 42.0

c: Shape = Circle()





#created a abstract class for phone, galaxy may support touch facility, but what about old phones
class Phone(ABC):
    @abstractmethod
    def call(self) -> None: ...
    @abstractmethod
    def text(self) -> None: ...
    @abstractmethod
    def slide_to_unlock(self) -> None: ...

class Galaxy(Phone):
    def call(self) -> None:
        print("Call with Galaxy.")
    def text(self) -> None:
        print("Text with Galaxy.")
    def slide_to_unlock(self) -> None:
        print("Slide to unlock Galaxy.")


# for old phones it should add new class 
class Phone(ABC):
    @abstractmethod
    def call(self) -> None: ...
    @abstractmethod
    def text(self) -> None: ...
    @abstractmethod
    def slide_to_unlock(self) -> None: ...

class Galaxy(Phone):
    def call(self) -> None:
        print("Call with Galaxy.")
    def text(self) -> None:
        print("Text with Galaxy.")
    def slide_to_unlock(self) -> None:
        print("Slide to unlock Galaxy.")

class Nokia(Phone):
    def call(self) -> None:
        print("Call with Nokia.")
    def text(self) -> None:
        print("Text with Nokia.")
    def slide_to_unlock(self) -> None:
        raise NotImplementedError("not implemented") 


# Now i will fix it , by not violating liskov substitue , 
# bcz nokia is pushed to implement slide_to_unloack method               

class Connectable(Protocol):
    def call(self) -> None: ...
    def text(self) -> None: ...
    def slide_to_unlock(self) -> None: ...

class Touchable(Protocol):
    def slide_to_unlock(self) -> None: ...

class Galaxy:
    def call(self) -> None:
        print("Call with Galaxy.")
    def text(self) -> None:
        print("Text with Galaxy.")
    def slide_to_unlock(self) -> None:
        print("Slide to unlock Galaxy.")

class Nokia:
    def call(self) -> None:
        print("Call with Nokia.")
    def text(self) -> None:
        print("Text with Nokia.")

connectable_devices: List[Connectable] = [Galaxy(), Nokia()]
touchable_devices: List[Touchable] = [Galaxy(), Nokia()]


# another example
class Shape(Protocol):
    def render(self) -> str: ...

class Circle:
    def render(self) -> str:
        return f"Circle geometry"

c: Shape = Circle()



#fixed here
class Shape(Protocol):
    x: float
    y: float
    def render(self) -> str: ...

class Circle:
    def __init__(self, x: float, y: float) -> None:
      self.x = x
      self.y = y

    def render(self) -> str:
        return f"Circle geometry"

c: Shape = Circle(10.5, 20.25)