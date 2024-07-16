lower = int(input("enter the lower limit: "))
upper = int(input("Enter the upper limit: "))

sum_e = 0
sum_o = 0

for i in range(lower, upper+1):
    if i % 2 == 0:
        sum_e += i
    else:
        sum_o += i

print(f"Sum of even numbers = {sum_e}")
print(f"Sum of odd numbers = {sum_o}")
