import random


def guess(x):
    guess = 0
    count = 0
    random_number = random.randint(1, x)
    while guess != random_number:
        guess = int(input(f"enter your guess number between 1 and {x}:"))
        count += 1
        if guess < random_number:
            print("too low")
        elif guess > random_number:
           print("too high")
    print(f"congo!! you guess the right number {random_number} in {count} attempt")


guess(100)
