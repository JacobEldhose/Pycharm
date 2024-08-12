lst = [1, 3, 4, 3, 2, 4, 5, 8, 9, 7, 5, 4, 3, 6, 9, 10, 11, 13, 10, 9, 7, 6, 8, 9]
lst1 = []


lst1.append(lst[0])
for i in range (1,len(lst)-1):
    if (lst[i-1] < lst[i] <lst[i+1]) | (lst[i-1] > lst[i] > lst[i+1]):
        continue
    else:
        lst1.append(lst[i])
print(lst1)
