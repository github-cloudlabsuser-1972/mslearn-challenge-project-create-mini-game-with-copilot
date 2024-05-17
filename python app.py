import random

def get_user_choice():
    user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
    while user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid input. Please enter rock, paper, or scissors.")
        user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
    return user_choice^

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    if (user_choice == "rock" and computer_choice == "scissors") or \
       (user_choice == "paper" and computer_choice == "rock") or \
       (user_choice == "scissors" and computer_choice == "paper"):
        return "user"
    return "computer"

def play_game():
    user_score = 0
    computer_score = 0
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        winner = determine_winner(user_choice, computer_choice)
        if winner == "user":
            user_score += 1
            print(f"You chose {user_choice}, computer chose {computer_choice}. You win this round!")
        elif winner == "computer":
            computer_score += 1
            print(f"You chose {user_choice}, computer chose {computer_choice}. Computer wins this round!")
        else:
            print(f"Both you and the computer chose {user_choice}. It's a tie!")
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break
    print(f"Final score: You - {user_score}, Computer - {computer_score}")

play_game()