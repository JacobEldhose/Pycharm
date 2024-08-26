ls = ['hi',4,8.99,'apple',('t,b','n')]
lst = [tuple([i,ls[i]]) for i in range (len(ls))]
print(lst)