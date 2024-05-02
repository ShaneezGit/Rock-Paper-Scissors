import random
import time

# Function to determine the winner of a round
def determine_winner(user_input, computer_pick):
    if user_input == computer_pick:
        return "It's a tie!"    # If both the user and computer picks are the same
    elif (user_input == "rock" and computer_pick == "scissors") or \
        (user_input == "paper" and computer_pick == "rock") or \
        (user_input == "scissors" and computer_pick == "paper"):
        return "You won!"       
    else:
        return "You lost!"      # If none of the above conditions are met, the user loses

# Initialize win counts for user and computer    
user_wins = 0
computer_wins = 0

# List of options for the game
options = ["rock", "paper", "scissors"]

# Main game loop
    # Prompt the user for input
    # Check if the user wants to quit
while True:
    print("\n** Rock-Paper-Scissors! **")
    user_input = input("\nType Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break

    time.sleep(1)

    # Check if the user input is valid
    if user_input not in options:
        print("Invalid input. Please enter Rock, Paper, or Scissors.")
        continue

    # Generate a random pick for the computer
    random_number = random.randint(0,2)
    # rock: 0, paper: 1, scissors: 2
    computer_pick = options[random_number]
    print("\nComputer picked", computer_pick + ".")

    # Determine the winner of the round
    result = determine_winner(user_input, computer_pick)
    print(result)

    # Update win counts based on the result
    if result == "You won!":
        user_wins += 1
    elif result == "You lost!":
        computer_wins += 1

# Print the final results
print("\nYou won", user_wins, "times.")
print("The computer won", computer_wins, "times.")
print("Goodbye!")
