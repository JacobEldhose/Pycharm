lst = ['apple','banana','cherry']
v="aeiou"
lst_v = ["".join([i for i in word if i not in v]) for word in lst]
print(lst_v)