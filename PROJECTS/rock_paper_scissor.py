import random

person_win = 0
comp_win = 0

options = ["rock","paper","scissor"]
while True:
    client = input("Type Rock/Paper/Scissor or Q to exit :  ")
    if client.lower() == "q":
        break
    elif client.lower() not in options:
        print("Type a valid option.\n")
        continue

    num = random.randint(0,2)
    comp_num = options[num]
    if client.lower()== "rock" and comp_num=="scissors":
        print("You won !!")
        person_win+=1
        

    elif client.lower()=="scissor" and comp_num=="paper":
        print("You won !!")
        person_win+=1
        

    elif client.lower()=="paper" and comp_num=="rock":
        print("You won !!")
        person_win+=1
        

    else:
        print("You lose :( ")
        comp_win+=1
        
print("Time you won :"+ str(person_win))
print("Times you lost :",str(comp_win))
print("See Ya Later !!")


