# Parent class
class Animal:
    def speak(self):
        print("Animal speaks")

# Child class inheriting from one parent
class Dog(Animal):
    def bark(self):
        print("Dog barks")

# Usage
d = Dog()
d.speak()  # Inherited from Animal
d.bark()   # Defined in Dog


# Parent class 1
class Flyable:
    def fly(self):
        print("Can fly")

# Parent class 2
class Swimmable:
    def swim(self):
        print("Can swim")

# Child inheriting from two parents
class Duck(Flyable, Swimmable):
    def quack(self):
        print("Duck quacks")

# Usage
duck = Duck()
duck.fly()   # From Flyable
duck.swim()  # From Swimmable
duck.quack() # Defined in Duck


# Grandparent class
class Vehicle:
    def start(self):
        print("Vehicle started")

# Parent class inheriting from Vehicle
class Car(Vehicle):
    def drive(self):
        print("Car is driving")

# Child inheriting from Car
class ElectricCar(Car):
    def charge(self):
        print("Electric car charging")

# Usage
tesla = ElectricCar()
tesla.start()  # From Vehicle
tesla.drive()  # From Car
tesla.charge() # Defined in ElectricCar



# Parent class
class Bird:
    def chirp(self):
        print("Bird chirping")

# Child class 1
class Sparrow(Bird):
    def fly(self):
        print("Sparrow flying")

# Child class 2
class Penguin(Bird):
    def swim(self):
        print("Penguin swimming")

# Usage
s = Sparrow()
p = Penguin()

s.chirp()  # From Bird
s.fly()    # Defined in Sparrow

p.chirp()  # From Bird
p.swim()   # Defined in Penguin



# Base class
class Person:
    def greet(self):
        print("Hello from Person")

# Intermediate class 1
class Student(Person):
    def study(self):
        print("Student studying")

# Intermediate class 2
class Teacher(Person):
    def teach(self):
        print("Teacher teaching")

# Child inheriting from both Student and Teacher
class TA(Student, Teacher):
    def assist(self):
        print("TA assisting")

# Usage
ta = TA()
ta.greet()  # From Person
ta.study()  # From Student
ta.teach()  # From Teacher
ta.assist() # Defined in TA



