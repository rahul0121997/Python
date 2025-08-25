def play_21_game():
    print("🎮 Welcome to the 21 Number Game!")
    print("Rules:")
    print("- Take turns adding 1, 2, or 3 consecutive numbers")
    print("- The player who reaches 21 LOSES!")
    print("- Numbers must be consecutive (like 1,2,3 or just 4)")
    print("-" * 40)
    
    current_number = 0
    main_number = []
    
    print("Who goes first?")
    print("1. You go first")
    print("2. Computer goes first")
    
    user_inp = int(input("Enter 1 or 2: "))
    player_turn = (user_inp == 1)
    
    while current_number < 21:
        if player_turn:
            print(f"\nCurrent Number: {current_number}")
            print(f"Numbers so far: {main_number}")
            
            while True:
                count = int(input("How many numbers do you want to add (1, 2, or 3)? "))
                if count in [1, 2, 3]:
                    break
                else:
                    print("Invalid choice. Please enter 1, 2, or 3.")
            
            new_numbers = []
            for _ in range(count):
                current_number += 1
                new_numbers.append(current_number)
                main_number.append(current_number)
                if current_number >= 21:
                    print("You said 21. Computer wins!")
                    return
            print(f"You said: {new_numbers}")
        
        else:
            print("\nComputer's turn")
            numbers_to_add = (4 - (current_number % 4)) or 1
            if numbers_to_add > 3:
                numbers_to_add = 1
            
            new_numbers = []
            for _ in range(numbers_to_add):
                current_number += 1
                new_numbers.append(current_number)
                main_number.append(current_number)
                if current_number >= 21:
                    print(f"Computer said {new_numbers}. You win!")
                    return
            print(f"Computer said: {new_numbers}")
        
        player_turn = not player_turn

play_21_game()
