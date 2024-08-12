lst = ['apple', 'orange', 'grape', 'mango', 'mnp', 'kpl', 'ipl', 'isl']
new_lst = []
v = "aeiouAEIOU"
for i in lst:
    for j in i:
        if j in v:
            new_lst.append(i)
            break
        else:
            pass
print(new_lst)