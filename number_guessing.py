import random

lower_bound = int(input("enter the Lower bound: "))
upper_bound = int(input("enter the Upper bound: "))

res = random.randint(lower_bound, upper_bound)
lives = 1

while lives < 7:
    guess = int(input("enter your guess: "))
    if guess > res:
        print("you guessed too high")
    elif guess < res :
        print("you guessed too low")
    else:
        print(f"you guessed correct number{res} in {lives} tries")
        break
        
    lives += 1

if lives > 7:
    print(f"you are out of tries correct answer is {res}")
        