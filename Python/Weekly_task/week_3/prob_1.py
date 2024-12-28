"""
Print numbers divisible by 3 or 5 from 1 to 20 using a for loop
"""
for i in range(1, 21):
    if i % 3 == 0 | i % 5 == 0:
        print(i)
