"""
Write a Python script using list comprehension to perform the following
tasks on a given list of integers:
Create a new list containing the squares of all odd numbers from the original
list.
Create another list containing the cubes of all even numbers from the
original list.
Combine these two lists into a single list and sort it in descending order.
Print the final sorted list.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
"""
lst = list(map(int,input().split()))
lst1 = [i**2 for i in lst if i %2 !=0]
lst2 = [i**3 for i in lst if i %2 ==0]

lst3 = lst2 + lst1
print(sorted(lst3,reverse=True))