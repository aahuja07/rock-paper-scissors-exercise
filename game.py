import random #loading random module

print("Rock, Paper, Scissors, Shoot!")
# USER INPUT
user_selection = input("Please select 'rock', 'paper' or 'scissors'!") 
print("You chose:", user_selection)
#VALIDATE USER INPUT

#COMPUTER CHOICE

options = ["rock", "paper", "scissors"]
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





#RESULT
