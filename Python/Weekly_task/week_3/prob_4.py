"""
Python program to check if a given number is an Armstrong number
"""
num = int(input("Enter the number to be checked"))
arm = 0
ref = num
count = 0

while ref > 0:
    ref = ref // 10
    count = count + 1
ref = num
while num > 0:
    temp = num % 10
    arm = arm + (temp ** count)
    num = num // 10

if arm == ref:
    print(f"{ref} is a armstrong number")
else:
    print(f"{ref} is a not armstrong number")