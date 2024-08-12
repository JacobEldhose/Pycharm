"""
Python program to check the validity of password input by users.
"""
passw = input("Enter the password")

leng = len(passw)
alpha = False
upper = False
num = False
spcl = False
for i in passw:
    if i.islower():
        alpha = True
    elif i.isupper():
        upper = True
    elif i.isnumeric():
        num = True
    elif not i.isalnum():
        spcl = True
if (8>= leng <=15) & (alpha==True) & (upper==True) & (num==True) & (spcl==True):
    print("Password is valid")
elif not alpha:
    print("password should have lower character")
elif not upper:
    print("password should have upper character")
elif not num:
    print("password should have numeric character")
elif not spcl:
    print("password should have special character")
else:
    print("Password should have 8-15 characters")