"""
Print numbers from 1 to 10. If a number is divisible by 4, stop the loop using a for loop and break statement:
"""
for i in range(1,11):
    if i % 4 == 0:
        break
    else:
        print(i)