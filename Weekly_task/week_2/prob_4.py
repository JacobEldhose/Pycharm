"""
Age
"""
age = int(input("Enter your age: "))
gender = input("Enter your gender(M/F): ")
days = int(input("Enter the number of days you have worked: "))

if 18 <= age < 30:
    if gender.upper() == 'M':
        salary = 700 * days
    elif gender.upper() == 'F':
        salary = 750 * days
    else:
        print("Invalid gender")
elif 30 <= age <=40:
    if gender.upper() == 'M':
        salary = 800 * days
    elif gender.upper() == 'F':
        salary = 850 * days
    else:
        print("Invalid gender")
print(f"Your expected salary is {salary}")