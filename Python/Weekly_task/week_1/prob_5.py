"""Write a python program that takes 3 numbers as input from the user and
prints out the maximum and minimum numbers in the list"""
"""<-----------------------------METHOD 1 USING IF ELSE----------------------->"""
num1=int(input("Enter the 1st number:"))
num2=int(input("Enter the 2nd number:"))
num3=int(input("Enter the 3rd number:"))

if(num1>num2) and (num1>num3):
    print("MAXIMUM :",num1)
elif(num2>num3) and (num2>num3):
    print("MAXIMUM :", num2)
else:
    print("MAXIMUM :", num3)

if(num1<num2) and (num1<num3):
    print("MINIMUM :",num1)
elif(num2<num3) and (num2<num3):
    print("MINIMUM :", num2)
else:
    print("MINIMUM:", num3)

"""   <------------------------METHOD2 USING NESTED IF---------------------->
"""

"""SMALLEST & LARGEST"""

# num1=int(input("Enter 1st number :"))
# num2=int(input("Enter 2nd number :"))
# num3=int(input("Enter 3rd number :"))
#
# if num1>num2 and num1 > num3:
#     print(f"{num1} is the largest")
#     if(num2<num3):
#         print(f"{num2} is the smallest")
#     else:
#         print(f"{num3} is the smallest")
#
# elif(num2>num1 and num2 >num3):
#     print(f"{num2} is the largest")
#     if(num1<num3):
#         print(f"{num1} is the smallest")
#     else:
#         print(f"{num3} is the smallest")
# elif(num3 >num1 and num3>num2):
#     print(f"{num3} is the largest")
#     if(num1<num2):
#         print(f"{num1} is the smallest")
#     else:
#         print(f"{num2} is the smallest")
# else:
#     print("Equal")