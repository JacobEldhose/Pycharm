# create a program that takes a number as input (e.g., 2) and an alphabet letter (either uppercase or lowercase).
# The output should be the letter that is the given number of positions ahead of the input letter in the alphabet.
# For example, if the input is 2 and the letter is 'A', the output should be 'C'. Similarly, for lowercase letters,
# if the input is 2 and the letter is 'a', the output should be 'c'.

num = int(input())
alpha = input()
out = ''
cap = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i in range(len(cap)):
    if alpha.upper() == cap[i]:
        out = cap[i+num]
        break
if alpha.isupper():
    print(out.upper())
elif alpha.islower():
    print(out.lower())
