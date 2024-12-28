"""
Check triangle
"""
side_1 = int(input("Enter the length of side 1: "))
side_2 = int(input("Enter the length of side 2: "))
side_3 = int(input("Enter the length of side 3: "))
if side_2 == side_1 == side_3:
    print("This triangle is equilateral triangle")
elif side_1 == side_3 or side_2 == side_1 or side_2 == side_3:
    print(f"This triangle is isosceles triangle ")
else:
    print("This is scalene triangle")