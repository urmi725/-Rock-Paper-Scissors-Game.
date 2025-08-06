import tkinter as tk
import random

# --- Game Logic ---
ASCII_ART = {
    'rock': """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",
    'paper': """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
""",
    'scissors': """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
}

def determine_winner(user_choice, computer_choice):
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

# --- GUI Application ---
class RockPaperScissorsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock-Paper-Scissors Game")

        self.user_score = 0
        self.computer_score = 0

        # --- Widgets ---
        self.instruction_label = tk.Label(root, text="Choose your weapon:", font=('Helvetica', 14))
        self.instruction_label.pack(pady=10)

        self.choice_frame = tk.Frame(root)
        self.choice_frame.pack(pady=10)

        self.rock_button = tk.Button(self.choice_frame, text="Rock", width=15, command=lambda: self.play('rock'))
        self.rock_button.pack(side=tk.LEFT, padx=5)

        self.paper_button = tk.Button(self.choice_frame, text="Paper", width=15, command=lambda: self.play('paper'))
        self.paper_button.pack(side=tk.LEFT, padx=5)

        self.scissors_button = tk.Button(self.choice_frame, text="Scissors", width=15, command=lambda: self.play('scissors'))
        self.scissors_button.pack(side=tk.LEFT, padx=5)

        self.result_label = tk.Label(root, text="", font=('Helvetica', 12, 'bold'))
        self.result_label.pack(pady=20)

        self.choices_display = tk.Label(root, text="", font=('Courier', 10), justify=tk.LEFT)
        self.choices_display.pack(pady=10)

        self.score_label = tk.Label(root, text="Score: You 0 - 0 Computer", font=('Helvetica', 12))
        self.score_label.pack(pady=10)

        self.play_again_button = tk.Button(root, text="Play Again", command=self.reset_game, state=tk.DISABLED)
        self.play_again_button.pack(pady=10)

    def play(self, user_choice):
        computer_choice = random.choice(['rock', 'paper', 'scissors'])
        winner = determine_winner(user_choice, computer_choice)

        # Update scores
        if winner == 'user':
            self.user_score += 1
            self.result_label.config(text="You Win!", fg='green')
        elif winner == 'computer':
            self.computer_score += 1
            self.result_label.config(text="You Lose!", fg='red')
        else:
            self.result_label.config(text="It's a Tie!", fg='blue')

        # Display choices with ASCII art
        user_art = f"Your Choice:\n{ASCII_ART[user_choice]}"
        computer_art = f"Computer's Choice:\n{ASCII_ART[computer_choice]}"
        self.choices_display.config(text=f"{user_art}\n{computer_art}")

        # Update score display
        self.score_label.config(text=f"Score: You {self.user_score} - {self.computer_score} Computer")

        # Disable choice buttons and enable play again
        self.rock_button.config(state=tk.DISABLED)
        self.paper_button.config(state=tk.DISABLED)
        self.scissors_button.config(state=tk.DISABLED)
        self.play_again_button.config(state=tk.NORMAL)

    def reset_game(self):
        self.result_label.config(text="")
        self.choices_display.config(text="")
        self.rock_button.config(state=tk.NORMAL)
        self.paper_button.config(state=tk.NORMAL)
        self.scissors_button.config(state=tk.NORMAL)
        self.play_again_button.config(state=tk.DISABLED)

if __name__ == "__main__":
    main_window = tk.Tk()
    app = RockPaperScissorsApp(main_window)
    main_window.mainloop()