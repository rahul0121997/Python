import random
from words import words


def guess_words():
    num = random.choice(words)
    dashes = ["-"] * len(num)
    hidden_word = list(num)
    lives = 6
    guessed_letters = set()

    print("Welcome to Hangman!")

    while lives > 0:
        print("\nWord to guess:", "".join(dashes))
        print(f"Lives remaining: {lives}")


        user_guess = input("enter a character (a-z)").lower()


        if user_guess in guessed_letters:
            print("you already guessed the number")
            continue

        guessed_letters.add(user_guess) 

        
        if user_guess in num:
            print(f"good guess the {user_guess} is in word")
            

            for i in range(len(num)):
                if num[i] == user_guess:
                    dashes[i] = user_guess



            if "-" not in dashes:
                print("\nWord: " + "".join(dashes))
                print(f"Congratulations! You guessed the word: {num}")
                return




        elif user_guess not in num:
            print("wrong guess try again")
            lives -= 1

    print("\nGame Over! You've run out of lives.")
    print(f"The word was: {num}")
guess_words()
