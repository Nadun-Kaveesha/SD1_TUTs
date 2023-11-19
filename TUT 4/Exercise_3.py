while True:
    n=(input("Please enter an integer :"))
    try:
        n=int(n)
        break
    except ValueError:
        print("Requires a valid Intiger! Please try again")

print("You sucessfully entered an intiger")