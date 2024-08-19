lst = [(i,'small') if 1 <= i <=15 else (i,'medium') if 16 <= i <= 35 else (i,'large') for i in range (1,40)]
print(lst)