"""
Write a program to accept a number and check whether it's a perfect number or not.
Perfect  number is a number which is equal to the sum of its divisors.
For ex: 6 , its divisors are 1,2,3. So sum of divisors 1+2+3 is also 6
"""
num = int(input("Enter the num"))
sums = 0
for i in range (1,num):
    if num % i == 0:
        sums = sums + i
if sums == num:
    print(f"{sums} is a perfect number")
