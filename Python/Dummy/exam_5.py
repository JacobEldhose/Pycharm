num = 1
for i in range(1, 5):
    for j in range(1,i+1):
        if i<j:
            print(i,end=' ')
        else:
            print(j, end=' ')
    print()

# n = input("Enter the string: ")
# n = input("Enter the string: ")
# if n[0]!=0 and n[0]!=1 and n[0]!=2 and n[0]!=3 and n[0]!=4 and n[0]!=5 and n[0]!=6 and n[0]!=7 and n[0]!=8 and n[0]!=9:
#     for i in n:
#         if 'a'<=i<='z'or 'A'<=i<='Z'or i=='_':
#             print("valid identifier")
#             break
#         else:
#             print("Invalid")
#             break