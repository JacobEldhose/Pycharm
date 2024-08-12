"""
a, b, c = 0, 0, 0 .
Write a python program to print all permutations using those three variables
"""

a = int(input("Enter the first number :"))
b = int(input("Enter the second number :"))
c = int(input("Enter the third number :"))
d = []
d.extend([a, b, c])
print(d)
for i in d:
    for j in d:
        for k in d:
            if i != j and i != k and j != k:
                print(i, j, k, end=" ")
                print()
