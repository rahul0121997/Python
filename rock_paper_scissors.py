import random

def play():
    player_name = input("enter your name : ")
    round = input("enter round you want to play : ")
    print(f"welcomr {player_name} to the rock paper scissors")
    player_choice = input("choose : rock ,paper ,scissors \n")

    computer_choice = random.choice(["rock","paper","scissors: \n"])

    print(f"you choose : {player_choice}")
    print(f"computer choose : {computer_choice}")

    if(player_choice == computer_choice):
        return "it\'s tie"
    elif(player_choice == "rock" and computer_choice == "scissors") or \
        (player_choice == "paper" and computer_choice == "rock") or \
        (player_choice == "scissors" and computer_choice == "paper"):
        return "you won"
    return "you loose"


print(play())