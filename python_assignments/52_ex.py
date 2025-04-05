class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")  # Overrides the speak() method of the Animal class

# Create an instance of Dog
dog = Dog()
dog.speak()  # Output: Dog barks

# Create an instance of Animal
animal = Animal()
animal.speak()  # Output: Animal speaks
