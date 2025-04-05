class Calculator:
    def add(self, a, b=0):
        # If only one argument is provided, treat b as 0
        return a + b

# Create an instance of Calculator
calc = Calculator()

# Call the method with one argument
print("Sum with one argument:", calc.add(5))  # Output: 5

# Call the method with two arguments
print("Sum with two arguments:", calc.add(5, 10))  # Output: 15
