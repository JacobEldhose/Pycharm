"""
A school has following rules for grading system:
a. Below 25 - F
b. 25 to 45 - E
c. 45 to 50 - D
d. 50 to 60 - C
e. 60 to 80 - B
f. Above 80 - A
Ask user to enter marks and print the corresponding grade.
"""
mark = int(input("Enter the mark to be checked: "))
if mark < 25:
    print("You got an F grade")
elif 25 <= mark < 45:
    print("You got an E grade")
elif 45 <= mark < 50:
    print("You got an D grade")
elif 50 <= mark < 60:
    print("You got an C grade")
elif 60 <= mark < 80:
    print("You got an B grade")
else:
    print("You got an A grade")