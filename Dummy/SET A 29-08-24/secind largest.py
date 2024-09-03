"""
Write a program to find the second largest number in a given list of integers.
Then, perform the following tasks:
Remove all occurrences of the second largest number from the list.
Calculate the sum of the remaining numbers in the list.
Sort the modified list in ascending order and print it.
"""

lst = list(map(int,input().split()))
lst1 = list(sorted(set(lst)))
while lst1[-2] in lst:
    lst.remove(lst1[-2])
print(sum(lst))
print(sorted(lst))