print("Welcome to quiz !")

correct_answers = 0

playing = input("Would you like to play ?  ")
if playing.lower() != "yes":
    quit()
print("Let's play !!!")

ans = input("What is the national capital of India ?  ")

if ans == "New Delhi":
    print("Absolutely Correct :) ")
    correct_answers+=1
else:print("Incorrect Answer :( ")

ans2 = input("What is the economic capital of India ?  ")

if ans2 == "Mumbai":
    print("Absolutely Correct :) ")
    correct_answers+=1
else:print("Incorrect Answer :( ")

ans3 = input("What does PTO stand for ? ")

if ans3.lower() == "please turn over":
    print("Absolutely Correct :) ")
    correct_answers+=1
else:print("Incorrect Answer :( ")

ans4 = input("Who was the first female CM of Odisha ?  ")

if ans4 == "Nandini Satpathy":
    print("Absolutely Correct :) ")
    correct_answers+=1
else:print("Incorrect Answer :( ")

print()
print("The total number of correct answers is "+ str(correct_answers) + " .")
