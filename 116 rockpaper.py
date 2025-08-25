#rock paper scissors
import random

chances = int(input('enter the number of round you want to play: '))

while chances > 0:
    choices = ('rock','paper', 'scissors')
    user_choice = int(input("""enter your choice: 
                            1 - rock
                            2 - paper
                            3 - scissors
                            """))

    computer_choice = random.choices(choices)
    
    if user_choice == "paper" and computer_choice == "rock" or user_choice == "rock" and computer_choice == "scissors" or user_choice == "scissors" and computer_choice == "paper":
        print("you win!!!")
    else:
        print("computer win!!")
        
    chances -= 1   