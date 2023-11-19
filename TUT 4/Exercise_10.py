import random
#Declaring variables
user_num=0
i=0
hidden_no=random.randrange(1,20)

while i<5:
    user_num=int(input("Make Your guess :"))
    i+=1
    if user_num>hidden_no:
        print("Too high1\n")
    elif user_num<hidden_no:
        print("Too Low\n")
    elif user_num==hidden_no:
        print("You Guessed the correct number!,It was ",str(hidden_no)+" ."+" You took ",str(i)+" "+"Attempts")
        break
    
if i==5:
    print("Not guessed! Correct answer was:",str(hidden_no))





    
    

        
