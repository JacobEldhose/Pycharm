lower = int(input("Enter lower"))
upper = int(input("Enter upper"))
sums = 0
while lower <= upper:
    if lower % 5 == 0:
        sums += lower
    lower += 1
print(f"Sum is {sums}")
