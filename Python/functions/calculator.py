def add(num1, num2):
    return num1 + num2


def sub(num1, num2):
    return num1 - num2


def mult(num1, num2):
    return num1 * num2


def div(num1, num2):
    return num1 / num2


print("1. Addition \n"
      "2. Subtraction \n"
      "3. Multiplication \n"
      "4. Division")

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))

choice = int(input("Enter you choice"))

if choice == 1:
    print(f"Sum = {add(num1, num2)}")

elif choice == 2:
    print(f"Subtraction = {sub(num1, num2)}")

elif choice == 3:
    print(f"Multiplication = {mult(num1, num2)}")

elif choice == 4:
    print(f"Division = {div(num1, num2)}")

else:
    print("Invalid option")
