# Rock paper scissors game

import random
item_list = ["Rock", "Paper", "Scissor"]

user_choice =input("Enter your move=Rock, Paper, Scissor=")
comp_choice=random.choice(item_list)

print(f"User Choice ={user_choice}, computer choice ={comp_choice}")

if(user_choice ==comp_choice):
    print("Both Choices same : = Match Tie")

elif(user_choice =="Rock"):
    if(comp_choice == "Paper"):
        print("Paper covers Rock = Computer")
    else:
        print("Rock samshes Scissor = You win")

elif user_choice == "Paper":
    if comp_choice == "Scissor":
        print("Scissor cuts the paper, Computer Win")
    else:
        print("Pper covers Rock, You Win")

elif user_choice == "Scissor":
    if comp_choice =="Paper":
        print("Scissor cuts the paper,You Win")
    else:
        print("Rock smashes the Scissors, Computer Win")       
       
    


    