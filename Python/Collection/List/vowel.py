string = 'luminartechnolab'
vowels = 'aeiouAEIOU'
vowl = []
for i in string:
    for j in i:
        if i in vowels:
        vowl.append(i)

print(vowl)
print(len(vowl))
