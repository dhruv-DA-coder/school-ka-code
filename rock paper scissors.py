import random
choice=("Rock", "Paper", "Scissors")
# Get the user's choice.
user_choice = input("Choose Rock, Paper, or Scissors: ")

# Generate a random choice for the computer.
computer_choice =random.choice(choice)

# Compare the user's choice to the computer's choice.
if user_choice == computer_choice:
    print("It's a tie!")
elif user_choice == "Rock":
    if computer_choice == "Scissors":
        print("You win!")
    else:
        print("You lose!")
elif user_choice == "Paper":
    if computer_choice == "Rock":
        print("You win!")
    else:
        print("You lose!")
else:
    if computer_choice == "Paper":
        print("You win!")
    else:
        print("You lose!")
