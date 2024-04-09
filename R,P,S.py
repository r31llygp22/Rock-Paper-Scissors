import random

while True:
    print("Choose your charater, Rock, Paper, Scissors (say quit to end the game):")
    your_choice = input("Your choice: ").lower()

    if your_choice == 'quit':
        break

    try:
        if your_choice not in ['rock', 'paper', 'scissors']:
            raise ValueError("Invalid choice")
    except ValueError:
        print(" I SAID CHOOSE rock, paper, scissors, or 'QUIT >:(.")
        continue

    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    print(f"Computer chooses {computer_choice}")

    if your_choice == computer_choice:
        print("Its a tie PLS PLAY AGAIN")
    elif (
        (your_choice == 'rock' and computer_choice == 'scissors') or
        (your_choice == 'paper' and computer_choice == 'rock') or
        (your_choice == 'scissors' and computer_choice == 'paper')
    ):
        print("You win :'(")
    else:
        print("You lose hahahahahah XD.")

print("Goodbye hope to play with you again :D")