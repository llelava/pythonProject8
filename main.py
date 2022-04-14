import random

def random_choice():
    choice_number = random.randint(1, 3)
    if choice_number == 1:
        choice = 'rock'
    elif choice_number == 2:
        choice = 'scissors'
    else:
        choice = 'paper'
    return choice

my_choice = input('Choose rock, scissors or paper: ').lower()
if my_choice == "rock" or my_choice == "scissors" or my_choice == "paper":
    opponent_choice = random_choice()
    print('Your opponent chose {}'.format(opponent_choice))
    if my_choice == opponent_choice:
        print("It's a draw!")
    if my_choice == "rock":
        if opponent_choice == 'scissors':
            print('You win!')
        elif opponent_choice == 'paper':
            print("You lose!")
    elif my_choice == "paper":
        if opponent_choice == "scissors":
            print("You Lose")
        elif opponent_choice == "rock":
            print("You lose!")
    elif my_choice == "scissors":
        if opponent_choice == "paper":
            print("You won!")
        elif opponent_choice == "rock":
            print("You lose!")

else:
    print("Enter either rock, paper or scissors!")