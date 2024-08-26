ls = ['apple','bannana','cherry']
v = 'aeiou'
lst = [''.join(['*' if j in v else j for j in i ]) for i in ls]
print(lst)