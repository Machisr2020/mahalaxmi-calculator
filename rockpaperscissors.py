import random
choices=["rock","paper","scissors"]
while True:
    user = input("Choose rock, paper, scissors or 'quit' to stop: ").lower()
    computer=random.choice(choices)
    break
    if user not in choices:
        print("Invalid choice!")
    continue

    computer = random.choice(choices)
    print(f"You chose {user}, computer chose {computer}.")

    if user == computer:
        print("It's a tie!")
    elif( 
         (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer=="rock")or
         (user == "scissors"and computer=="paper")
         ):

        print("You win!")
    else:
        print("You lose!")
        print(f"Computer chose:{computer}")
    if user == "quit":
        print("Thanks for playing!")
