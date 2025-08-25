# Simple 21 Number Game
# Goal: Don't be the player who reaches 21!

def play_21_game():
    print("🎮 Welcome to the 21 Number Game!")
    print("Rules:")
    print("- Take turns adding 1, 2, or 3 consecutive numbers")
    print("- The player who reaches 21 LOSES!")
    print("- Numbers must be consecutive (like 1,2,3 or just 4)")
    print("-" * 40)
    
    # Game variables
    current_number = 0  # Start from 0, first player will start with 1
    numbers_said = []   # Keep track of all numbers said
    
    # Choose who goes first
    print("Who goes first?")
    print("1. You go first")
    print("2. Computer goes first")
    
    choice = input("Enter 1 or 2: ")
    
    if choice == "1":
        player_turn = True
    else:
        player_turn = False
    
    # Main game loop
    while current_number < 21:
        
        if player_turn:
            # Player's turn
            print(f"\nCurrent number: {current_number}")
            print("Numbers said so far:", numbers_said)
            
            # Get player input
            while True:
                try:
                    count = int(input("How many numbers do you want to add (1, 2, or 3)? "))
                    if count in [1, 2, 3]:
                        break
                    else:
                        print("Please enter 1, 2, or 3 only!")
                except:
                    print("Please enter a valid number!")
            
            # Add the numbers
            new_numbers = []
            for i in range(count):
                current_number += 1
                new_numbers.append(current_number)
                numbers_said.append(current_number)
            
            print(f"You added: {new_numbers}")
            
            # Check if player loses
            if current_number >= 21:
                print(f"\n💀 You reached {current_number}! YOU LOSE!")
                break
                
        else:
            # Computer's turn
            print(f"\nCurrent number: {current_number}")
            print("Numbers said so far:", numbers_said)
            print("\nComputer's turn...")
            
            # Computer strategy: try to leave multiples of 4 for the player
            # This is a winning strategy!
            numbers_to_add = ((current_number - 1) % 4) + 1
            if numbers_to_add > 3:
                numbers_to_add = 1
            
            # Add computer's numbers
            new_numbers = []
            for i in range(numbers_to_add):
                current_number += 1
                new_numbers.append(current_number)
                numbers_said.append(current_number)
            
            print(f"Computer added: {new_numbers}")
            
            # Check if computer loses
            if current_number >= 21:
                print(f"\n🎉 Computer reached {current_number}! YOU WIN!")
                break
        
        # Switch turns
        player_turn = not player_turn
    
    # Ask to play again
    print("\nWant to play again? (y/n)")
    if input().lower() == 'y':
        play_21_game()
    else:
        print("Thanks for playing! 👋")

# Start the game
if __name__ == "__main__":
    play_21_game()