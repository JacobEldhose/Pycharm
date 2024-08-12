lower = int(input("Enter the lower: "))
upper = int(input("Enter the upper: "))

sum_e = 0
sum_o = 0
while lower <= upper:
    if lower % 2 == 0:
        sum_e += lower
    else:
        sum_o += lower
    lower += 1
print(f"Sum of even numbers = {sum_e}")
print(f"Sum of odd numbers = {sum_o}")
