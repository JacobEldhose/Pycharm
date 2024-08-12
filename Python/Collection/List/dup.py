lst = [1, 1, 3, 3, 4, 5, 6, 10, 10, 10, 30, 2, 3, 4, 50]
dup = []
for i in lst:
    if i not in dup:
        dup.append(i)
print(dup)
