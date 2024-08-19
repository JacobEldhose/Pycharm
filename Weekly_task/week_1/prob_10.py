"""Write a function to calculate the factorial of a number recursively.
"""


def fact(num):
    f=1
    if num==1:
        return num
    else:
        return num*fact(num-1)

num=int(input("Enter the number:"))
print(fact(num))