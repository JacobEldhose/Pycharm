lower = int(input("enter the lower limit: "))
upper = int(input("Enter the upper limit: "))

sum = 0

for i in range(lower, upper+1):
    if i % 2 == 1:
        sum += i

print(sum)
