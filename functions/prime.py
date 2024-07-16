def prime():
    flag = 0
    num = int(input("Enter the number "))
    for i in range(2, num):
        if num % i == 0:
            flag = 1
            break
    if flag == 1:
        print("Not prime")
    else:
        print("Prime")


prime()