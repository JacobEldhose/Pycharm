num = int(input("Enter the number: "))

fact = 1

for i in range(num, 0, -1):
    fact *= i

print(fact)
