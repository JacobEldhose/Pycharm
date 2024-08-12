"""
1
2 2
3 3 3
4 4 4 4
3 3 3
2 2
1

"""
for i in range (1,5):
    for j in range(1,i+1):
        print(i,end=" ")
    print()
for i in range(3,0,-1):
    for j in range(i,0,-1):
        print(i,end=" ")
    print()