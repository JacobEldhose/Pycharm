def big_odd(word):
    lst = [i for i in word if int(i)%1==1]
    lst = sorted(lst)
    print(lst)
    return lst[len(lst)-1]
lst = '23569'
print(big_odd(lst))