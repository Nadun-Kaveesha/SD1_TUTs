print('Welcome to calculatorr!!')
while True:

     expression = input("Enter an arithmetic expression (or 'exit' to quit): ")

if expression == 'exit':
     break

try:
         result = eval(expression)
         print(f"Result: {result}")
         
except (SyntaxError, NameError, TypeError):
        print("Invalid input. Please enter a valid arithmetic expression.")
