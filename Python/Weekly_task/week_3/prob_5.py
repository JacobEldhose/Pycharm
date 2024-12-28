"""
Python program to display all numbers within a range except the prime numbers.

"""
low = int(input("Enter the lower range "))
upp = int(input("Enter the upper range "))

for i in range(low, upp+1):
    flag = 0
    for j in range(2, i):
        if i % j == 0:
            flag = 1
            break
    if flag != 1:
        print(i)
