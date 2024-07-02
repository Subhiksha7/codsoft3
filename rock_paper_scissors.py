import tkinter as tk
from tkinter import messagebox
import random

# Initialize scores
user_score = 0
computer_score = 0

# Function to determine the winner
def determine_winner(user_choice):
    global user_score, computer_score

    # Computer makes a random choice
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    
    # Determine the result
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        result = "You win!"
        user_score += 1
    else:
        result = "You lose!"
        computer_score += 1

    # Update the result and scores
    result_label.config(text=f"You chose {user_choice}, Computer chose {computer_choice}. {result}")
    score_label.config(text=f"User Score: {user_score} - Computer Score: {computer_score}")

# Function to reset the game
def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    result_label.config(text="")
    score_label.config(text=f"User Score: {user_score} - Computer Score: {computer_score}")

# Set up the main window
root = tk.Tk()
root.title("Rock-Paper-Scissors")

# Create labels and buttons
instructions_label = tk.Label(root, text="Choose rock, paper, or scissors:")
instructions_label.pack(pady=10)

button_rock = tk.Button(root, text="Rock", command=lambda: determine_winner('rock'))
button_rock.pack(pady=5)

button_paper = tk.Button(root, text="Paper", command=lambda: determine_winner('paper'))
button_paper.pack(pady=5)

button_scissors = tk.Button(root, text="Scissors", command=lambda: determine_winner('scissors'))
button_scissors.pack(pady=5)

result_label = tk.Label(root, text="", font=("Helvetica", 12))
result_label.pack(pady=10)

score_label = tk.Label(root, text=f"User Score: {user_score} - Computer Score: {computer_score}", font=("Helvetica", 12))
score_label.pack(pady=10)

reset_button = tk.Button(root, text="Reset Game", command=reset_game)
reset_button.pack(pady=10)

# Run the application
root.mainloop()
