num = int(input("Enter the number to be reversed number: "))
reverse = 0

while num > 0:
    temp = num % 10
    reverse = reverse*10 + temp
    num = num//10
print(reverse)
