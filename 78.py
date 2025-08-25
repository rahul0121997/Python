#abstraction
from abc import ABC ,abstractmethod

class Animal(ABC):
    
    @abstractmethod
    def make_sound(self):
        pass
    
class Dog(Animal):
    
    def make_sound(self):
        print(f" Dog is barking outside")
    
class Cat(Animal):
    
    def make_sound(self):
        print(f"Cat meow meow!")
        

a = Dog()
a.make_sound()