secret_word="apple"
turns=1
guess=''


while True:
    if turns <= len(secret_word)+3 :
        guess=str(input("Make your guess :"))
        turns+=1
    else:
        print("Sorry your turns are over!")
        break
