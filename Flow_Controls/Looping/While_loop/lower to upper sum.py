lower = int(input("Enter the lower: "))
upper = int(input("Enter the upper: "))

sums = 0

while lower <= upper:
    if lower % 2 == 0:
        sums = sums + lower
    lower += 1
print(sums)
