import random
from re import X #loading random module

print("Rock, Paper, Scissors, Shoot!")
# USER INPUT
user_selection = input("Please select 'rock', 'paper' or 'scissors'!") 
print("You chose:", user_selection)

#VALIDATE USER INPUT
options = ["rock", "paper", "scissors"]
user_selection = user_selection.lower()

if user_selection not in options:
    print ("Not a valid option, please choose 'rock, 'paper' or 'scissors'")
    exit()
#COMPUTER CHOICE

computer_choice = random.choice(options)
print("Computer chose:", computer_choice)


#WINNER
if user_selection == computer_choice:
    print("You both chose", user_selection, "It's a tie!")

elif user_selection == "rock":
    if computer_choice == "scissors":
        print("Rock beats scissors. You win!")
    else:
        print("Paper beats rock. Computer wins!") 

elif user_selection == "scissors":
    if computer_choice == "paper":
        print("Scissors beats Paper. You win!")
    else:
        print("Rock beats scissors. Computer wins!")

elif user_selection == "paper":
    if computer_choice == "rock":
        print("Paper beats Rock. You win!")
    else:
        print("Scissors beat Paper. Computer wins!")  
