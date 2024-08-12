lower = int(input("Enter lower"))
upper = int(input("Enter upper"))
while lower <= upper:
    if lower % 2 == 0:
        print(lower)
    lower += 1
