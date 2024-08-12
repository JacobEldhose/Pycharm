"""
Count the total number of digits in a number
"""
num = int(input("Enter the number"))
count = 0
while num > 0:
    count +=1
    num = num // 10
print(f"count = {count}")