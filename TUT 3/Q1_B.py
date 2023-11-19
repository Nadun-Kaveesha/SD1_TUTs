age=input("What is your age :")

try:
    age=int(age)
    if age>=10:
        print("Can vote")
    else:
        print("Cant vote")
except ValueError:
    print("Cannot enter letters as a age!")
