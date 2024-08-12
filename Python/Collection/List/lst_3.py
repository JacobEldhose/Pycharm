lst = [4, 2, 5, 8, 4, 6, 10, 1, 7, 10]
element = int(input("Enter the element"))

for i in lst:
    for j in lst:
        if i+j == element:
            print(f"({i},{j})")