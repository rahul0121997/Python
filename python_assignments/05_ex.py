def is_prime(number):
    # Numbers less than 2 are not prime
    if number < 2:
        return False
    
    # 2 is the only even prime number
    if number == 2:
        return True
    
    # All other even numbers are not prime
    if number % 2 == 0:
        return False
    
    # Check odd divisors up to the square root of the number
    # (No need to check beyond square root - if there's a divisor larger than sqrt,
    # there must be a corresponding smaller divisor we would have already found)
    i = 3
    while i * i <= number:
        if number % i == 0:
            return False
        i += 2
    
    # If no divisors found, the number is prime
    return True