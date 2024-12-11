lst = [1,3,5,6,8,9,6,4,3,2,4,5,8,9]

for i in range(len(lst)-1):
    if (lst[i-1]>=lst[i]<=lst[i+1]) | (lst[i-1]<=lst[i]>=lst[i+1]):
        print(lst[i])