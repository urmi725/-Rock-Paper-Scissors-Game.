import random

def get_computer_choice():
    """Randomly selects between rock, paper, and scissors."""
    return random.choice(['rock', 'paper', 'scissors'])

def get_user_choice():
    """Prompts the user for their choice and validates it."""
    while True:
        user_input = input("Choose rock, paper, or scissors: ").lower().strip()
        if user_input in ['rock', 'paper', 'scissors']:
            return user_input
        print("Invalid choice. Please choose rock, paper, or scissors.")

def determine_winner(user_choice, computer_choice):
    """Determines the winner based on game rules."""
    if user_choice == computer_choice:
        return 'tie'
    
    winning_combinations = {
        'rock': 'scissors',
        'paper': 'rock',
        'scissors': 'paper'
    }

    if winning_combinations[user_choice] == computer_choice:
        return 'user'
    else:
        return 'computer'

def display_result(user_choice, computer_choice, winner):
    """Displays the choices and the result of the round."""
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    if winner == 'tie':
        print("It's a tie!")
    elif winner == 'user':
        print("You win!")
    else:
        print("You lose!")

def play_game():
    """Main function to play the Rock-Paper-Scissors game."""
    user_score = 0
    computer_score = 0
    
    print("Welcome to Rock-Paper-Scissors!")

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        winner = determine_winner(user_choice, computer_choice)
        
        display_result(user_choice, computer_choice, winner)
        
        if winner == 'user':
            user_score += 1
        elif winner == 'computer':
            computer_score += 1
            
        print(f"\nScores:\n- You: {user_score}\n- Computer: {computer_score}")

        while True:
            play_again = input("\nDo you want to play another round? (yes/no): ").lower()
            if play_again in ['yes', 'no']:
                break
            print("Invalid input. Please enter 'yes' or 'no'.")

        if play_again == 'no':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    play_game()