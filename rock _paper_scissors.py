import random

def play():

    player_name = input("enter your name :")
    total_round = int(input("enter the round you want to play :"))
    print(f"welcome {player_name} to rock paper scissors")

    player_score = 0
    computer_score = 0

    for round in range(total_round):
        print(f"round {round+1}/{total_round}")

        player_choice = input("choose rock, paper or scissors\n").lower()
        if player_choice not in(["rock","paper","scissors"]):
            return "invalid choice"

        computer_choice = random.choice(["rock","paper","scissors"])

        print(f"you chose : {player_choice}")
        print(f"computer chose :{computer_choice}")

        if player_choice == computer_choice:
            print("It's a tie!")
        elif (player_choice == "rock" and computer_choice == "scissors") or \
             (player_choice == "paper" and computer_choice == "rock") or \
             (player_choice == "scissors" and computer_choice == "paper"):
            print("You win this round!")
            player_score += 1

        else:
            print("you lose this round")
            computer_score += 1 

    print("game over!!!")
    print(f"player_score : {player_score}")
    print(f"computer_score : {computer_score}")

    if(player_score > computer_score):
        print("player win!")
    elif(player_score < computer_choice):
        print("computer win!")
    else:
        print("it is tie")


print(play())