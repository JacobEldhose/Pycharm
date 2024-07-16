"""A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years. Ask useer for
their salary and year of service and print the net bonus amount"""

sal = int(input("Enter your current salary: "))
year = int(input("How many years have you worked in this company: "))

if year >= 5:
    print("Your bonus amount is: ", sal * 5/100)
else:
    print("Sorry you are under experienced")
