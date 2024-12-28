"""Write a Python program to generate all possible valid identifiers of length n,
where n is provided by the user character of n number is given by the user.
"""


# Python keywords to check against
python_keywords = [
    "False", "None", "True", "and", "as", "assert", "async", "await", "break",
    "class", "continue", "def", "del", "elif", "else", "except", "finally",
    "for", "from", "global", "if", "import", "in", "is", "lambda", "nonlocal",
    "not", "or", "pass", "raise", "return", "try", "while", "with", "yield"
]

allcharactor = input("Enter your string value, we will find all the valid identifiers in it \n Enter Here: ")

def generate_identifiers(word, length):
    if length == 0:
        check = True
        for i in word:
            if not (i == '_' or 'A' <= i <= 'Z' or 'a' <= i <= 'z'):
                check = False
                break
        index = 0
        for i in word:
            if index >= 1:
                if not (i == '_' or 'A' <= i <= 'Z' or 'a' <= i <= 'z' or '0' <= i <= '9'):
                    check = False
                    break
            index += 1
        if word in python_keywords:
            check = False
        if check == True:
            print(word, end=" , ")
    else:
        for i in allcharactor:
            generate_identifiers(word + i, length - 1)

length = int(input("Enter the length of identifier you want: "))
generate_identifiers('', length)
