import sys

from calculator import add, subtract, multiply, divide

print("Simple Calculator")
operator = ['add', 'subtract', 'multiply', 'divide']
print("Please select operation -")
for i, op in enumerate(operator, 1):
    print(f"{i}. {op}")
choice = input("Enter the number of the operation you'd like to perform: ")
if choice.isdigit() and 1 <= int(choice) <= len(operator):
    operator = operator[int(choice) - 1]
    print(f"You selected: {operator}")
    print("Enter two numbers to perform the operation on:")
    try:
        num1 = float(input("Enter first number: "))
    except ValueError:
        print("Invalid input. Please make sure you enter a number.")
        num1 = float(input("Enter first number: "))
    try:
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input. Please make sure you enter a number.")
        num2 = float(input("Enter second number: "))
    if operator == 'add':
        print(f"{num1} + {num2} = {add(num1, num2)}")
    elif operator == 'subtract':
        print(f"{num1} - {num2} = {subtract(num1, num2)}")
    elif operator == 'multiply':
        print(f"{num1} * {num2} = {multiply(num1, num2)}")
    elif operator == 'divide':
        print(f"{num1} / {num2} = {divide(num1, num2)}")
    else:
        print("Invalid operator. Please restart the program and try again.")
        sys.exit(1)
else:
    print("Invalid choice. Please restart the program and try again.")
    sys.exit(1)
