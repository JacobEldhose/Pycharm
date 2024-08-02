f = open('spark', 'r')
lst = ''
dic = {}

for i in f:
    lst = i.rstrip('\n').split()

for j in lst:
    if j not in dic:
        dic[j] = 1
    else:
        dic[j] += 1
for k,v in dic.items():
    print(k,':',v)