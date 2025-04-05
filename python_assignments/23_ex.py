import random

def get_user_choice():
    user_choice = input("enter your choice (rock,paper,scissors): ")

def get_computer_choice():
         choice = ("rock", "paper", "scissors")
         computer_choice = random.choice(choice)
         print(f"computer choice is : {computer_choice}")

def winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print("it\'s tie")
    elif (user_choice == "rock" and computer_choice == "scissors" or
         user_choice == "paper"and computer_choice == "rock" or
         user_choice == "scissors" and computer_choice == "paper" ):
            print("user win!!")
    else:
         print("computer win!!")


def play():
    round = int(input("enter the round you want to play: "))
    while round > 0:
        print("welcome to the rock paper scissors game")
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        result = winner(user_choice, computer_choice)
        print(result)
        round -= 1

    
play()

         