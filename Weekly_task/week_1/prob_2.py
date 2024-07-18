"""
Write a Python program to find all the valid identifiers in a given string. Assume that identifiers are separated
by spaces.
"""


string = input("Enter the sentence")
identifier = ''
for i in string:
    if i != ' ':
        identifier += i
    else:
        flag = 0
        i_count = 0
        for j in identifier:
            if flag == 0:
                if '0' <= j <= '9':
                    print("You cannot use digits at first")
                    break
            if ('a' <= j <= 'z') | ('A' <= j <= 'Z') | ('0' <= j <= '9') | (j == '_'):
                i_count = 1
            else:
                i_count = 0
                break

            flag += 1
        if i_count >= 1:
            print(f"{identifier} is Valid")
        else:
            print(f"{identifier} is invalid")
        identifier = ''
if identifier:
    flag = 0
    i_count = 0
    for j in identifier:
        if flag == 0:
            if '0' <= j <= '9':
                print("You cannot use digits at first")
                break
        if ('a' <= j <= 'z') | ('A' <= j <= 'Z') | ('0' <= j <= '9') | (j == '_'):
            i_count = 1
        else:
            i_count = 0
            break

        flag += 1
    if i_count >= 1:
        print(f"{identifier} is Valid")
    else:
        print(f"{identifier} is invalid")
    identifier = ''

