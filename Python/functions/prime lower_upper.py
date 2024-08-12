def prime(lower, upper):
    for i in range(lower, upper+1):
        flag = 0
        for j in range(2, i):
            if i % j == 0:
                flag = 1
                break
        if flag == 0:
            print(i)


lower = int(input("Enter the lower: "))
upper = int(input("Enter the upper: "))

prime(lower, upper)