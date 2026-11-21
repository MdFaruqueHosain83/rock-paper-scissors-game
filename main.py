import random

print("=== Rock Paper Scissors Game ===")
print("Made by Md Faruque Hosain")
print("\nRules: Rock beats Scissors, Scissors beats Paper, Paper beats Rock")

choices = ["rock", "paper", "scissors"]

while True:
    user = input("\nChoose rock / paper / scissors (or quit to exit): ").lower()

    if user == "quit":
        print("\nThanks for playing! Bye 👋")
        break

    if user not in choices:
        print("Invalid choice! Try again.")
        continue

    computer = random.choice(choices)
    print(f"\nYou chose: {user}")
    print(f"Computer chose: {computer}")

    if user == computer:
        print("Result: It's a Tie! 🤝")
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        print("Result: You WIN! 🎉")
    else:
        print("Result: Computer WINS! 💻")
