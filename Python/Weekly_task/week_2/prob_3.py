"""
Write a program to find greatest number among three numbers
"""
num1 = int(input("Enter the 1st number "))
num2 = int(input("Enter the 2nd number "))
num3 = int(input("Enter the 3rd number "))
if num1 > num2 and num1 > num3:
    print(f"{num1} is greater")
elif num2 > num1 and num2 > num3:
    print(f"{num2} is greater")
elif num3 > num2 and num3 > num1:
    print(f"{num3} is greater")
elif num1 == num3 == num2:
    print("They are equal")