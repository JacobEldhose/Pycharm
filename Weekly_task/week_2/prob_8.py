"""
3 input and opertation
"""
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
op = input("Enter operator: ")
if op == '+':
    result = num1 + num2
    print(f"Your answer is : {result}")
elif op == '-':
    result = num1 - num2
    print(f"Your answer is : {result}")
elif op == '*':
    result = num1 * num2
    print(f"Your answer is : {result}")
elif op == '/':
    result = num1 / num2
    print(f"Your answer is : {result}")
else:
    print("invalid Input")

