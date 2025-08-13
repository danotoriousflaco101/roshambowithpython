# Import the random library to make random choices
import random

# User welcome message
print("Let's play Roshambo! ✂️📄🪨")

# Get user choice
user_choice = input("Pick your weapon (rock, paper, or scissors): ").lower()

# Generate the computer's choice
options = ["rock", "paper", "scissors"]
computer_choice = random.choice(options)

# Show the choices made 
print(f"\nYour choice: {user_choice}")
print(f"Opponent's weapon: {computer_choice}\n")

# Determine the winner
if user_choice not in options:
    print("Gotta choose something if you want to play! 😅")

# When it's a draw:
elif user_choice == computer_choice:
    print("It's a DRAW!")

# All winning conditions for the user:
elif (user_choice == "rock" and computer_choice == "scissors") or \
     (user_choice == "paper" and computer_choice == "rock") or \
     (user_choice == "scissors" and computer_choice == "paper"):
    print("SUPREME VICTORY! 🎉")

# If the user loses:
else:
    print("DEFEATED! Try your luck again! 😢")