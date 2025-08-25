#method oerriding

class Animal():
    def __init__(self):
        print("inside the parent class")
        
    def make_sound(self):
        print("animal sound")
        
class Dog(Animal):
    
    def make_sound(self):
        print("dog is barking")
        super().make_sound()
        

d = Dog()
d.make_sound()