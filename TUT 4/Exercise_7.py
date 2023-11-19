import random

first_dice=0
second_dice=0
count=0
doubles=0

while count<=100:
        first_dice=random.randrange(1,7)
        second_dice=random.randrange(1,7)
        count+=1
        if first_dice==second_dice:
                doubles+=1
        print (str(first_dice)+"   "+str(second_dice))
        
print("\nOut of 100 you rolled ",str(doubles)," Doubles")


    

