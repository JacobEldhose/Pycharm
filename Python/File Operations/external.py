f = open('C:\\Users\\jacob\\Downloads\\sample4.txt', 'r')

# for i in f:
#     data = i.rstrip('\n').split(',')
#     if data[5] == "Chennai":
#         print(data[1:4])

for i in f:
    data = i.rstrip('\n').split(',')
    if data[5] == "Chennai" and data[3]>'23':
        print(data[1::2])