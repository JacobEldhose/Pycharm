f = open("C:\\Users\\jacob\\Downloads\\temper.txt", 'r')
dic = {}

for i in f:
    data = i.rstrip('\n').split(',')
    if data[0] not in dic:
        dic[data[0]] = data[1]
    else:
        if dic[data[0]] < data[1]:
            dic[data[0]] = data[1]
print(dic)