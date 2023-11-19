#Declaring variables
total=0
count=0
score=0
ave=0

#Getting inputs

#proces
while score != -9:
    score=int(input("Enter the score,(Enter -9 to end) :"))
    if score == -9 and count==0:
        print("At least one score should be enterd")
    else:
        total +=score
        count +=1

if count>=1:
    ave=float((total+9)/(count-1))
    print("Class average is",ave)

    
    




