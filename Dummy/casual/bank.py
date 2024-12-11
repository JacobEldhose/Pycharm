# """Design a program for the bank domain where there are unlimited denominations of coins (e.g., 1, 2, 5, 10).
# The program takes an amount as input (e.g., 7) and calculates the minimum number of coins needed to sum up to that amount.
# For instance, if the input is 7, the output should be 2, as the minimum number of coins to make 7 is 2
# (using one 5-coin and one 2-coin)."""

l=[1,2,5,10]
t=int(input(""))
sum=0
for i in l[::-1]:
    while t>=i:
        t-=i
        sum+=1
if t==0:
    print(sum)
else:
    print("its not possible")