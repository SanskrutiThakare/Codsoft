import tkinter as tk
from tkinter import ttk
import random

def play_game(player_choice):
    choices = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(choices)

    result = determine_winner(player_choice, computer_choice)

    result_label.config(text=f"Computer chose {computer_choice}. {result}")

def determine_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    elif (
        (player == 'Rock' and computer == 'Scissors') or
        (player == 'Paper' and computer == 'Rock') or
        (player == 'Scissors' and computer == 'Paper')
    ):
        return "You win!"
    else:
        return "Computer wins!"

# Create the main window
root = tk.Tk()
root.title("Rock, Paper, Scissors Game")

# Create and configure frames
main_frame = ttk.Frame(root, padding="20")
main_frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))
main_frame.columnconfigure(0, weight=1)
main_frame.rowconfigure(0, weight=1)

# Create and configure widgets
title_label = ttk.Label(main_frame, text="Rock, Paper, Scissors", font=("Arial", 18, "bold"))

rock_button = ttk.Button(main_frame, text="Rock", command=lambda: play_game('Rock'))
paper_button = ttk.Button(main_frame, text="Paper", command=lambda: play_game('Paper'))
scissors_button = ttk.Button(main_frame, text="Scissors", command=lambda: play_game('Scissors'))

result_label = ttk.Label(main_frame, text="", font=("Arial", 12, "italic"))

# Arrange widgets in the grid
title_label.grid(column=0, row=0, columnspan=3, pady=10)
rock_button.grid(column=0, row=1, padx=5, pady=10)
paper_button.grid(column=1, row=1, padx=5, pady=10)
scissors_button.grid(column=2, row=1, padx=5, pady=10)
result_label.grid(column=0, row=2, columnspan=3, pady=10)

# Start the GUI event loop
root.mainloop()
