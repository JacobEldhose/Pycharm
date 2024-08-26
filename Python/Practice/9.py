lst1 = [1,2,3,4,5,6]
lst2 = [4,5,6,7,8,9]
lst = [(i,i) for i in lst1 if i in lst2]
print(lst)