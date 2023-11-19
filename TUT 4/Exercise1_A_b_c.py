import random

#Declaring Variables
hidden_num=random.randrange(1,20)
user_num=0

#process
while True:
    user_num=int(input("Make your Guess [1-20] :"))
    if user_num>=21 or user_num<=0:
        print("Please enter number between 1 and 20\n")
    elif user_num>hidden_num:
        print("Too High!\n")
    elif user_num<hidden_num:
        print("Too Low!\n")
    elif user_num != hidden_num:
        print("Wrong Guess!,Try Again\n")
    elif user_num == hidden_num:
        print("Congratulations!,You guessed the correct number\n")
        break
    

