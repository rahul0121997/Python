import random
from collections import Counter

name = input("what is your name?: ")

print(f"Good Luck {name}")

words = ('rahul','sunil','prithvi','vishnu','deva','manav')
word = random.choice(words)

turns = len(word) + 2
guesses = ' '

while turns > 0:
    failed = 0
    print()
    user = input("enter your guess: ").lower()
    if len(user) != 1 or not user.isalpha():
        print("Please enter only a single letter.")
        continue
    
    if user in guesses:
        print("you have already guessed that letter")
        continue

    guesses += user
    for char in word:
        k = word.count(char)
        if char in  guesses and Counter(guesses) != Counter(word):
            print(char,end=' ')
        elif Counter(guesses) == Counter(word):
            print()
            print(f'you won! you guessed all the letter {used_turns} in turns')
            print(f"the word is {word}")
            break
        else:
            print('-', end = " ")
            failed += 1
    used_turns = (len(word) + 2) - turns
                    
    if failed == 0:
        print()
        print(f'you won! you guessed all the letter in {used_turns} turns')
        print(f"the word is {word}")
        break

    if user not in word:
        print()
        turns -= 1
        print(f"you choose wrong letter you have only {turns} turns left")
        
        if turns == 0 :
            print("you loose!")
            break