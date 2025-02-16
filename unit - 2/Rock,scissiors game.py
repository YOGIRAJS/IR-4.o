import random

choices = ["Rock","Paper","Scissors"]

user_choice = input("enter rock, paper or scissors")
computer_choice = random.choice(choices)
if (user_choice==computer_choice):
    print("Draw")
else:
    print(f"Computer choose {computer_choice}")
