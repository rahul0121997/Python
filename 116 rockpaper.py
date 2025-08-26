import random

choices = ('paper','rock','scissors')
computer_choice = random.choice(choices)

number_of_round = int(input("enter the number of round you want play: "))

computer_win = 0
user_win = 0
tie = 0
while number_of_round > 0:
    user_choice = input("enter you choice from(rock,paper,scissors): ")
    print(computer_choice)
    
    if user_choice == computer_choice:
        tie += 1
        print("it's tieee!!!")
    elif user_choice == 'rock' and computer_choice == 'scissors' or user_choice == 'paper' and computer_choice == 'rock' or user_choice == 'scissors' and computer_choice == 'paper':
        print("you win!!!!")
        user_win += 1
    else:
        print("computer win!!!")
        computer_win += 1
    number_of_round -= 1
    

if computer_win > user_win:
    print(f"computer is overall winner with won {computer_win}")
elif user_win > computer_win:
    print(f"you won overall with number of round:{user_win}")
else:
    print("it's tiee")