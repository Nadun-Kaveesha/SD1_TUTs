bill_amount = float(input("Enter the cost of the meal: "))

satisfaction_level = int(input("Enter your satisfaction level (1 = Totally satisfied, 2 = Satisfied, 3 = Dissatisfied): "))


if satisfaction_level == 1:
    tip_amount = 0.20 * bill_amount
elif satisfaction_level == 2:
     tip_amount = 0.15 * bill_amount
elif satisfaction_level == 3:
    tip_amount = 0.10 * bill_amount
else:
    print("Invalid satisfaction level.")

    print("Satisfaction level:", satisfaction_level)
    print("Tip amount:", tip_amount)