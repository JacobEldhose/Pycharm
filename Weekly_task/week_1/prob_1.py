"""
Write a Python program to check if a given string is a valid identifier or not.
An identifier is valid if it starts with a letter (a-z, A-Z) or an underscore (_)
followed by zero or more letters, underscores, or digits (0-9).
"""
string = input("Enter the identifier")
flag = 0
identifier = 0
for i in string:
    if flag == 0:
        if (i >= '0' and i <= '9'):
            print("You cannot use digits at first")
            break
    if (i >= 'a' and i <= 'z') |  (i >= 'A' and i <= 'Z') | (i >= '0' and i <= '9') | (i == '_'):
        identifier = 1
    else:
        identifier = 0
        break

    flag += 1
if identifier >=1:
    print("Valid")
else:
    print("invalid")

