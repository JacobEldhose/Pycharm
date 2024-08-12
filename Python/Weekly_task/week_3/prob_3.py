"""
Python program that accepts a word from the user and reverses it.
"""
chars = input("Enter the string")
revers = ""
for i in range (len(chars)-1,-1,-1):
    revers = revers + chars[i]
print(revers)
