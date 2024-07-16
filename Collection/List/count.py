string = 'luminartechnolab'
vowels = 'aeiouAEIOU'
cons = []

for i in string:
    if i not in vowels:
        cons.append(i)
print(cons)
print(len(cons))