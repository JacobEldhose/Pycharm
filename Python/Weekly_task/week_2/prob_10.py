"""
Take values of length and breadth of a rectangle from user and check if it is square or not.
"""
length = int(input("Enter the length: "))
breadth = int(input("Enter the breadth: "))
if length == breadth:
    print(f"This is a square")
else:
    print(f"It is not a square")