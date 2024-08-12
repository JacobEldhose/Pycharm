lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

f = list(map(lambda num: num**3,list(filter(lambda num : num%2 !=0,lst))))
print(f)