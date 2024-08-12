lst = [10, 2, 5, 15, 11, 7, 20, 30, 23, 61, 75]
lst1 = []
for i in lst:

    for j in range(2,i):
        if i % j == 0:
            break
    else:
        lst1.append(i)
print(lst1)