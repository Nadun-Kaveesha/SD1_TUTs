response = input("Do you like Python? (yes/no): ")


response = response.lower()

if response == "yes" or response == "y":
     print("You are on the right course!")
elif response == "no" or response == "n":
    print("You might change your mind!")
else:
     print("I did not understand.")