"""
Write a Python script to find all prime numbers in the range from 1 to 100
and add them to a list. Then, calculate the sum and the average of these
prime numbers, and print the list of prime numbers, the sum, and the
average.
"""

lst = []
flag = 0
for i in range(2,101):
    flag = 0
    for j in range(2,i):
        if i % j == 0:
            flag = 1
            break
    if flag == 0:
        lst.append(i)
print(lst)
print(sum(lst))
print((sum(lst)/len(lst)))