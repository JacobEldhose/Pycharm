"""
Write a program to check whether given year is leap year or not
"""
year = int(input("Enter the year to be checked: "))
if year % 4 == 0:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not leap year")