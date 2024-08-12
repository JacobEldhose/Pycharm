lst = [1, 6, 8, 10, 11, 13, 15, 25, 40, 50, 35, 41, 37, 3]

n = int(input("Enter element to be searched"))

for i in lst:
    if i == n:
        print("Element found")
        break
else:
    print("not found")
