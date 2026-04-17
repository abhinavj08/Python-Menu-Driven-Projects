from .logic import get_computer_choice, determine_winner

def display_main_menu():
    """Prints the main menu options."""
    print("\n" + "="*30)
    print(" STONE - PAPER - SCISSORS ")
    print("="*30)
    print("1. Play a Round")
    print("2. Exit")
    print("="*30)

def play_round():
    """Handles the interaction for a single round."""
    print("\nChoose your weapon:")
    print("1. Stone")
    print("2. Paper")
    print("3. Scissors")
    
    user_input = input("Enter 1, 2, or 3: ")
    choices_map = {'1': 'Stone', '2': 'Paper', '3': 'Scissors'}
    
    if user_input in choices_map:
        user_choice = choices_map[user_input]
        computer_choice = get_computer_choice()
        
        print(f"\n> You chose:      {user_choice}")
        print(f"> Computer chose: {computer_choice}")
        
        # Calculate and show the result
        result = determine_winner(user_choice, computer_choice)
        print(f"\n*** {result} ***")
    else:
        print("\nInvalid choice. Please enter a valid number.")

def start_application():
    """The infinite loop driving the menu system."""
    while True:
        display_main_menu()
        choice = input("Select an option (1-2): ")

        if choice == '1':
            play_round()
        elif choice == '2':
            print("\nExiting the game. Thanks for playing!")
            break
        else:
            print("\nInvalid input. Please type 1 or 2.")