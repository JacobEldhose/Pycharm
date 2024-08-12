lst = [6, 10, 8, 12, 20, 4, 15, 4, 1]
lst1 = []
sums = sum(lst)

for i in lst:
    lst1.append(sums - i)

print(lst1)