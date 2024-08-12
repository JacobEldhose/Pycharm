"""
Input
Current year from user
current date from user
current month from user

Birth year
birth month
birthdate

Output
Age
"""

c_year = int(input("Enter the current year"))
c_month = int(input("Enter the current month"))
c_day = int(input("Enter the current day"))

b_year = int(input("Enter the birth year"))
b_month = int(input("Enter the birth month"))
b_day = int(input("Enter the birth day"))
years = c_year-b_year
if c_month < b_month:
    years -= 1
else:
    if c_month == b_month:
        if c_day < b_day:
            years -= 1

print(f"You are {years} years")
