import random

def get_computer_choice():
    """Generates a random choice for the computer."""
    options = ['Stone', 'Paper', 'Scissors']
    return random.choice(options)

def determine_winner(user_choice, computer_choice):
    """Contains the logic to determine the winner of a single round."""
    if user_choice == computer_choice:
        return "It's a tie!"
    
    # Winning conditions for the user
    if (user_choice == 'Stone' and computer_choice == 'Scissors') or \
       (user_choice == 'Paper' and computer_choice == 'Stone') or \
       (user_choice == 'Scissors' and computer_choice == 'Paper'):
        return "You win!"
    
    # If it's not a tie and the user didn't win, the computer wins
    return "Computer wins!"