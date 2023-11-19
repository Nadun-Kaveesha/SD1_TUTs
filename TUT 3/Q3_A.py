

choice=input("""
Welcome to temperature converter !
Pick an option:
        1-Celsius to Fahrenheit
        2-Fahrenheit to Celsius
: """)

try:
    choice=int(choice)
except ValueError as e:
    print("Please enter a number (1-2)")
    exit(1)

if choice==1:
    celsius=input("Enter the temperature in celsius :")
    try:
        celsius=float(celsius)
    except ValueError as e:
        print("Please enter a valid number!")
        exit(1)
    fahrenheit=(celsius*1.8) +32
    print(str(celsius)+" "+"in celsius is," +" "+ str(fahrenheit)+" "+"in fahrenhite!")



elif choice==2:
    fahrenheit=input("Enter the temperature in fahrenheit :")
    try:
        fahrenheit=float(fahrenheit)
    except ValueError as e:
        print("Please enter a valid number!")
        exit(1)
    celsius=(fahrenheit-32) /18
    print(str(fahrenheit)+" "+"in fahrenheit is," +" "+ str(celsius)+" "+"in celsius!")

else:
    print("Enter a valid option")


