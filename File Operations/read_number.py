f = open("sample_2", 'r')
l = []

for i in f:
    l.append(int(i.rstrip('\n')))
print(sum(l))
