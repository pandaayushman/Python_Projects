import random

# first number

start_num = input("Enter the starting number : ")
if start_num.isdigit():
    start_num = int(start_num)

    if start_num <= 0:
        print("Enter a number greater than zero.")
        quit()

else:
    print("Enter a number the next time. Thank you.")
    quit()

# last number

end_num = input("Enter a ending number : ")
if end_num.isdigit():
    end_num = int(end_num)

    if end_num <= 0:
        print("Enter a number greater than zero.")
        quit()

else:
    print("Enter a number the next time. Thank you.")
    quit()

#random number generation

random_num = random.randint(start_num,end_num + 1)


#guess game 
count = 0
while True:
    count += 1
    guessed_num = input("Guess the integer in the range specified by you....  ")
    if guessed_num.isdigit():
        guessed_num=int(guessed_num)
    else:
        print("Enter a number tne next time.")
        continue

    if random_num == guessed_num:
        print("Hurray! You got it right.")
        break
    else:
        if guessed_num > random_num:
            print("You are greater than the actual number.")
        else:
            print("You are below the number. ")

    

print("Number of Attempts : ",count)  #NO. OF ATTEMPTS
