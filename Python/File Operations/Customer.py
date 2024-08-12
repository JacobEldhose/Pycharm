f = open("C:\\Users\\jacob\\Downloads\\customer1.txt", 'r')
# for i in f:
#     data = i.rstrip('\n').split(',')
#     if data[3] > "50":
#         print(data[1:5])

# for i in f:
#     data = i.rstrip('\n').split(',')
#     if '25' < data[3] < '40':
#         print(data[1::2])

# for i in f:
#     data = i.rstrip('\n').split(',')
#     if data[-1] == 'india':
#         print(data[1:6])

# for i in f:
#     data = i.rstrip('\n').split(',')
#     if data[5] == 'india' and data[3] > '50':
#         print(data[1:4])

# for i in f:
#     data = i.rstrip('\n').split(',')
#     if data[-1] == 'uk':
#         print(data)

# for i in f:
#     data = i.rstrip('\n').split(',')
#     if data[-1] == 'india' and data[4] == 'Doctor':
#         print(data[1:5])

# for i in f:
#     data = i.rstrip('\n').split(',')
#     if data[4] == 'Pilot':
#         print(data[1:4])

# dic = {}
# for i in f:
#     data = i.rstrip('\n').split(',')
#     if data[4] in dic:
#         dic[data[4]] += 1
#     else:
#         dic[data[4]] = 1
# print(dic)

# dic = {}
# for i in f:
#     data = i.rstrip('\n').split(',')
#     if data[-1] in dic:
#         dic[data[-1]] += 1
#     else:
#         dic[data[-1]] = 1
# print(dic)